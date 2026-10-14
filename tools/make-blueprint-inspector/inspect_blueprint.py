"""Summarise a Make.com scenario blueprint as safe-to-share Markdown + Mermaid.

Only structure is emitted: module types (app:action), router branches and
filter labels. Parameters, mappers, prompts, connection IDs, data store IDs,
webhook URLs and anything else that could hold a secret are never read into
the output. Filter labels are passed through a redactor as a second line of
defence.

Usage:
    python inspect_blueprint.py scenario.blueprint.json [--title "Name"] [--mermaid-only]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

_REDACTIONS = [
    (re.compile(r"https?://\S+"), "<url>"),
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"), "<email>"),
    # long strings mixing letters and digits look like keys; plain hyphenated words don't
    (re.compile(r"\b(?=[A-Za-z0-9_-]*\d)(?=[A-Za-z0-9_-]*[A-Za-z])[A-Za-z0-9_-]{24,}\b"), "<token>"),
    (re.compile(r"\b[0-9a-f]{8,}\b", re.I), "<id>"),
    (re.compile(r"\b\d{5,}\b"), "<id>"),
]


def redact(text: str) -> str:
    for pattern, repl in _REDACTIONS:
        text = pattern.sub(repl, text)
    return text.strip()


def load_flow(data: dict) -> tuple[str, list]:
    """Accept a raw blueprint, an export wrapper or an API response."""
    for key in ("response", "scenario"):
        if isinstance(data.get(key), dict):
            data = data[key]
    if isinstance(data.get("blueprint"), dict):
        data = data["blueprint"]
    if not isinstance(data.get("flow"), list):
        raise ValueError("no 'flow' list found: is this a Make blueprint?")
    return str(data.get("name", "")), data["flow"]


def walk(flow: list, depth: int = 0):
    """Yield (depth, module, route_index_path) for every module, routers included."""
    for module in flow:
        yield depth, module
        for route in module.get("routes") or []:
            yield from walk(route.get("flow") or [], depth + 1)


def filter_label(module: dict) -> str:
    flt = module.get("filter")
    if isinstance(flt, dict) and flt.get("name"):
        return redact(str(flt["name"]))[:80]
    return ""


def summarise(flow: list) -> dict:
    modules = [m for _, m in walk(flow)]
    apps = Counter(str(m.get("module", "?")).split(":")[0] for m in modules)
    actions = Counter(str(m.get("module", "?")) for m in modules)
    routers = [m for m in modules if str(m.get("module", "")).endswith(":BasicRouter")]
    filters = sum(1 for m in modules if filter_label(m))
    error_handlers = sum(1 for m in modules if m.get("onerror"))
    return {
        "modules": len(modules),
        "routers": len(routers),
        "branches": sum(len(r.get("routes") or []) for r in routers),
        "filters": filters,
        "error_handlers": error_handlers,
        "apps": apps,
        "actions": actions,
    }


def mermaid(flow: list, max_nodes: int = 120) -> str:
    lines = ["flowchart LR"]
    count = 0

    def node_id(m: dict) -> str:
        return f"m{m.get('id', id(m))}"

    def label(m: dict) -> str:
        text = str(m.get("module", "?")).replace('"', "'")
        f = filter_label(m)
        return f"{text}<br/><i>{f}</i>" if f else text

    def emit(seq: list, prev: str | None):
        nonlocal count
        for m in seq:
            if count >= max_nodes:
                return prev
            count += 1
            nid = node_id(m)
            lines.append(f'    {nid}["{label(m)}"]')
            if prev:
                lines.append(f"    {prev} --> {nid}")
            routes = m.get("routes") or []
            if routes:
                for route in routes:
                    emit(route.get("flow") or [], nid)
                return None  # a router ends the linear chain
            prev = nid
        return prev

    emit(flow, None)
    if count >= max_nodes:
        lines.append(f'    more["... truncated at {max_nodes} modules"]')
    return "\n".join(lines)


def render(title: str, flow: list) -> str:
    s = summarise(flow)
    out = [f"# {title or 'Make scenario'}", "",
           f"- Modules: **{s['modules']}** (routers: {s['routers']}, branches: {s['branches']})",
           f"- Modules with filters: {s['filters']}; modules with error handlers: {s['error_handlers']}",
           "", "## Apps used", "", "| App | Modules |", "|---|---|"]
    out += [f"| {app} | {n} |" for app, n in s["apps"].most_common()]
    out += ["", "## Actions", "", "| Action | Count |", "|---|---|"]
    out += [f"| `{a}` | {n} |" for a, n in s["actions"].most_common()]
    out += ["", "## Flow", "", "```mermaid", mermaid(flow), "```", ""]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("blueprint", type=Path)
    ap.add_argument("--title", default=None, help="override the scenario name")
    ap.add_argument("--mermaid-only", action="store_true")
    args = ap.parse_args(argv)
    # utf-8-sig: blueprints saved from PowerShell/Windows tools often carry a BOM
    name, flow = load_flow(json.loads(args.blueprint.read_text(encoding="utf-8-sig")))
    title = args.title or redact(name)  # an explicit --title is the author's own text
    sys.stdout.write(mermaid(flow) + "\n" if args.mermaid_only else render(title, flow))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
