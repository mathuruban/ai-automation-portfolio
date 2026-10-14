# make-blueprint-inspector

Turn a Make.com scenario export (`*.blueprint.json`) into a **safe-to-share** Markdown summary: module count, apps and actions used, router branches, filter labels and a Mermaid flow diagram.

Why: blueprints contain prompts, connection IDs, data store IDs and webhook URLs, so you can't paste one into a README or send it to a reviewer. This tool reads **structure only**. Parameters and mappers are never read into the output, and filter labels go through a redactor (URLs, emails, long key-like strings and IDs).

```bash
python inspect_blueprint.py my-scenario.blueprint.json --title "Lead intake"
python inspect_blueprint.py my-scenario.blueprint.json --mermaid-only
```

It accepts a raw blueprint, an export wrapper or an API response, with or without a UTF-8 BOM.

Tests: `python -m pytest`. The suite includes a leak test that plants secrets in parameters, mappers and filter names and asserts that none of them reaches the output.

Real outputs: [../../architecture](../../architecture/).

MIT licensed.
