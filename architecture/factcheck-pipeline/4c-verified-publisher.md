# Fact-check pipeline stage 4c-verified-publisher (generated)

- Modules: **22** (routers: 1, branches: 5)
- Modules with filters: 9; modules with error handlers: 0

## Apps used

| App | Modules |
|---|---|
| datastore | 9 |
| scenario-service | 6 |
| http | 6 |
| builtin | 1 |

## Actions

| Action | Count |
|---|---|
| `http:MakeRequest` | 6 |
| `datastore:UpdateRecord` | 5 |
| `scenario-service:ReturnData` | 5 |
| `datastore:ExistRecord` | 2 |
| `datastore:AddRecord` | 2 |
| `scenario-service:StartSubscenario` | 1 |
| `builtin:BasicRouter` | 1 |

## Flow

```mermaid
flowchart LR
    m28["scenario-service:StartSubscenario"]
    m30["datastore:ExistRecord<br/><i>Current original approved content only; future slot</i>"]
    m28 --> m30
    m31["datastore:ExistRecord<br/><i>No existing publication claim</i>"]
    m30 --> m31
    m1["http:MakeRequest<br/><i>No prior copy of media</i>"]
    m31 --> m1
    m29["datastore:AddRecord<br/><i>Verified brand channel ready</i>"]
    m1 --> m29
    m32["datastore:AddRecord"]
    m29 --> m32
    m40["builtin:BasicRouter"]
    m32 --> m40
    m50["http:MakeRequest<br/><i>instagram reel release</i>"]
    m40 --> m50
    m51["datastore:UpdateRecord"]
    m50 --> m51
    m52["scenario-service:ReturnData"]
    m51 --> m52
    m60["http:MakeRequest<br/><i>tiktok reel release</i>"]
    m40 --> m60
    m61["datastore:UpdateRecord"]
    m60 --> m61
    m62["scenario-service:ReturnData"]
    m61 --> m62
    m70["http:MakeRequest<br/><i>youtube reel release</i>"]
    m40 --> m70
    m71["datastore:UpdateRecord"]
    m70 --> m71
    m72["scenario-service:ReturnData"]
    m71 --> m72
    m80["http:MakeRequest<br/><i>instagram story release</i>"]
    m40 --> m80
    m81["datastore:UpdateRecord"]
    m80 --> m81
    m82["scenario-service:ReturnData"]
    m81 --> m82
    m90["http:MakeRequest<br/><i>facebook reel release</i>"]
    m40 --> m90
    m91["datastore:UpdateRecord"]
    m90 --> m91
    m92["scenario-service:ReturnData"]
    m91 --> m92
```
