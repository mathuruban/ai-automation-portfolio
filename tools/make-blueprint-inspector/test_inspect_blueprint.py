import json

import inspect_blueprint as ib

SECRET_FLOW = {
    "name": "Demo 9990001",
    "flow": [
        {"id": 1, "module": "gateway:CustomWebHook",
         "parameters": {"hook": 123456, "url": "https://hook.eu1.make.com/abcdefabcdefabcdefabcdef"}},
        {"id": 2, "module": "builtin:BasicRouter", "routes": [
            {"flow": [{"id": 3, "module": "openai-gpt-3:CreateCompletion",
                       "filter": {"name": "QA pass for ops@example.com"},
                       "mapper": {"prompt": "SYSTEM PROMPT sk-live-SECRETSECRETSECRETSECRET"}},
                      {"id": 4, "module": "youtube:uploadVideo", "onerror": [{"module": "builtin:Resume"}]}]},
            {"flow": [{"id": 5, "module": "datastore:AddRecord", "parameters": {"datastore": 424242}}]},
        ]},
    ],
}


def test_counts():
    _, flow = ib.load_flow({"blueprint": SECRET_FLOW})
    s = ib.summarise(flow)
    assert s["modules"] == 5
    assert s["routers"] == 1 and s["branches"] == 2
    assert s["filters"] == 1 and s["error_handlers"] == 1
    assert s["apps"]["datastore"] == 1


def test_no_secrets_leak():
    name, flow = ib.load_flow(SECRET_FLOW)
    out = ib.render(ib.redact(name), flow)
    for leak in ("424242", "123456", "hook.eu1", "SECRET", "SYSTEM PROMPT", "ops@example.com", "9990001"):
        assert leak not in out, leak
    assert "youtube:uploadVideo" in out and "QA pass" in out


def test_redact_keeps_plain_words():
    assert ib.redact("stage approved-release-queue-for-reviewers") == "stage approved-release-queue-for-reviewers"
    assert ib.redact("key Ab12Cd34Ef56Gh78Ij90Kl12Mn") == "key <token>"


def test_rejects_non_blueprint():
    try:
        ib.load_flow({"foo": 1})
    except ValueError:
        return
    raise AssertionError("expected ValueError")


def test_roundtrip_json(tmp_path):
    p = tmp_path / "bp.json"
    p.write_text(json.dumps({"response": {"blueprint": SECRET_FLOW}}), encoding="utf-8")
    assert ib.main([str(p), "--mermaid-only"]) == 0


def test_accepts_utf8_bom(tmp_path):
    p = tmp_path / "bom.json"
    p.write_bytes(b"\xef\xbb\xbf" + json.dumps(SECRET_FLOW).encode("utf-8"))
    assert ib.main([str(p)]) == 0
