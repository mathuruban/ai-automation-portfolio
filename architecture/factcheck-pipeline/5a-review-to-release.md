# Fact-check pipeline stage 5a-review-to-release (generated)

- Modules: **8** (routers: 0, branches: 0)
- Modules with filters: 1; modules with error handlers: 0

## Apps used

| App | Modules |
|---|---|
| datastore | 5 |
| json | 3 |

## Actions

| Action | Count |
|---|---|
| `json:ParseJSON` | 3 |
| `datastore:UpdateRecord` | 2 |
| `datastore:SearchRecord` | 1 |
| `datastore:GetRecord` | 1 |
| `datastore:AddRecord` | 1 |

## Flow

```mermaid
flowchart LR
    m1["datastore:SearchRecord"]
    m2["json:ParseJSON"]
    m1 --> m2
    m3["datastore:GetRecord"]
    m2 --> m3
    m4["json:ParseJSON"]
    m3 --> m4
    m5["datastore:UpdateRecord"]
    m4 --> m5
    m6["json:ParseJSON<br/><i>All actual audiovisual criteria pass for exact file</i>"]
    m5 --> m6
    m7["datastore:AddRecord"]
    m6 --> m7
    m8["datastore:UpdateRecord"]
    m7 --> m8
```
