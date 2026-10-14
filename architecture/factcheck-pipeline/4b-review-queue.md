# Fact-check pipeline stage 4b-review-queue (generated)

- Modules: **8** (routers: 0, branches: 0)
- Modules with filters: 3; modules with error handlers: 0

## Apps used

| App | Modules |
|---|---|
| datastore | 4 |
| json | 2 |
| gemini-ai | 2 |

## Actions

| Action | Count |
|---|---|
| `json:ParseJSON` | 2 |
| `gemini-ai:makeApiCall` | 2 |
| `datastore:AddRecord` | 2 |
| `datastore:SearchRecord` | 1 |
| `datastore:UpdateRecord` | 1 |

## Flow

```mermaid
flowchart LR
    m1["datastore:SearchRecord"]
    m2["json:ParseJSON"]
    m1 --> m2
    m3["gemini-ai:makeApiCall<br/><i>Owned uploaded media only</i>"]
    m2 --> m3
    m4["datastore:AddRecord<br/><i>Ready exact uploaded bytes, rights and source gates</i>"]
    m3 --> m4
    m5["gemini-ai:makeApiCall"]
    m4 --> m5
    m6["json:ParseJSON<br/><i>Completed actual media review</i>"]
    m5 --> m6
    m7["datastore:AddRecord"]
    m6 --> m7
    m8["datastore:UpdateRecord"]
    m7 --> m8
```
