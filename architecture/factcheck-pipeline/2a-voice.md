# Fact-check pipeline stage 2a-voice (generated)

- Modules: **8** (routers: 0, branches: 0)
- Modules with filters: 2; modules with error handlers: 0

## Apps used

| App | Modules |
|---|---|
| datastore | 3 |
| scenario-service | 2 |
| dropbox | 2 |
| elevenlabs | 1 |

## Actions

| Action | Count |
|---|---|
| `scenario-service:StartSubscenario` | 1 |
| `datastore:ExistRecord` | 1 |
| `datastore:AddRecord` | 1 |
| `elevenlabs:createTextToSpeech` | 1 |
| `dropbox:uploadLargeFile` | 1 |
| `dropbox:createShareLink` | 1 |
| `datastore:UpdateRecord` | 1 |
| `scenario-service:ReturnData` | 1 |

## Flow

```mermaid
flowchart LR
    m28["scenario-service:StartSubscenario"]
    m30["datastore:ExistRecord<br/><i>Validate approved voice input</i>"]
    m28 --> m30
    m29["datastore:AddRecord<br/><i>Claim only missing key</i>"]
    m30 --> m29
    m31["elevenlabs:createTextToSpeech"]
    m29 --> m31
    m32["dropbox:uploadLargeFile"]
    m31 --> m32
    m35["dropbox:createShareLink"]
    m32 --> m35
    m33["datastore:UpdateRecord"]
    m35 --> m33
    m34["scenario-service:ReturnData"]
    m33 --> m34
```
