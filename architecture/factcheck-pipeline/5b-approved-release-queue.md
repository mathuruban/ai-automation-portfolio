# Fact-check pipeline stage 5b-approved-release-queue (generated)

- Modules: **7** (routers: 0, branches: 0)
- Modules with filters: 2; modules with error handlers: 0

## Apps used

| App | Modules |
|---|---|
| datastore | 4 |
| json | 2 |
| scenario-service | 1 |

## Actions

| Action | Count |
|---|---|
| `json:ParseJSON` | 2 |
| `datastore:UpdateRecord` | 2 |
| `datastore:SearchRecord` | 1 |
| `datastore:GetRecord` | 1 |
| `scenario-service:CallSubscenario` | 1 |

## Flow

```mermaid
flowchart LR
    m1["datastore:SearchRecord"]
    m2["json:ParseJSON"]
    m1 --> m2
    m6["datastore:GetRecord<br/><i>Exact Offswitch review reference</i>"]
    m2 --> m6
    m7["json:ParseJSON"]
    m6 --> m7
    m3["datastore:UpdateRecord<br/><i>Saved automated audiovisual review matches exact media</i>"]
    m7 --> m3
    m4["scenario-service:CallSubscenario"]
    m3 --> m4
    m5["datastore:UpdateRecord"]
    m4 --> m5
```
