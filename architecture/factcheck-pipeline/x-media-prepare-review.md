# Fact-check pipeline stage x-media-prepare-review (generated)

- Modules: **4** (routers: 0, branches: 0)
- Modules with filters: 2; modules with error handlers: 0

## Apps used

| App | Modules |
|---|---|
| scenario-service | 2 |
| http | 1 |
| gemini-ai | 1 |

## Actions

| Action | Count |
|---|---|
| `scenario-service:StartSubscenario` | 1 |
| `http:DownloadFile` | 1 |
| `gemini-ai:uploadAFile` | 1 |
| `scenario-service:ReturnData` | 1 |

## Flow

```mermaid
flowchart LR
    m28["scenario-service:StartSubscenario"]
    m1["http:DownloadFile<br/><i>Only original Creatomate video</i>"]
    m28 --> m1
    m29["gemini-ai:uploadAFile"]
    m1 --> m29
    m2["scenario-service:ReturnData<br/><i>Uploaded bytes match downloaded bytes</i>"]
    m29 --> m2
```
