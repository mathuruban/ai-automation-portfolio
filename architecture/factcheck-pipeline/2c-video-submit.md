# Fact-check pipeline stage 2c-video-submit (generated)

- Modules: **8** (routers: 0, branches: 0)
- Modules with filters: 2; modules with error handlers: 0

## Apps used

| App | Modules |
|---|---|
| datastore | 3 |
| scenario-service | 2 |
| json | 2 |
| elevenlabs | 1 |

## Actions

| Action | Count |
|---|---|
| `json:ParseJSON` | 2 |
| `scenario-service:StartSubscenario` | 1 |
| `datastore:ExistRecord` | 1 |
| `datastore:AddRecord` | 1 |
| `elevenlabs:universal` | 1 |
| `datastore:UpdateRecord` | 1 |
| `scenario-service:ReturnData` | 1 |

## Flow

```mermaid
flowchart LR
    m28["scenario-service:StartSubscenario"]
    m2["json:ParseJSON"]
    m28 --> m2
    m3["json:ParseJSON"]
    m2 --> m3
    m30["datastore:ExistRecord<br/><i>Bounded original silent video request</i>"]
    m3 --> m30
    m29["datastore:AddRecord<br/><i>Claim only missing key</i>"]
    m30 --> m29
    m1["elevenlabs:universal"]
    m29 --> m1
    m33["datastore:UpdateRecord"]
    m1 --> m33
    m34["scenario-service:ReturnData"]
    m33 --> m34
```
