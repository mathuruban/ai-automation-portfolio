# Fact-check pipeline stage 2d-video-completion (generated)

- Modules: **8** (routers: 0, branches: 0)
- Modules with filters: 2; modules with error handlers: 0

## Apps used

| App | Modules |
|---|---|
| datastore | 3 |
| dropbox | 2 |
| json | 1 |
| elevenlabs | 1 |
| http | 1 |

## Actions

| Action | Count |
|---|---|
| `datastore:UpdateRecord` | 2 |
| `datastore:SearchRecord` | 1 |
| `json:ParseJSON` | 1 |
| `elevenlabs:universal` | 1 |
| `http:DownloadFile` | 1 |
| `dropbox:uploadLargeFile` | 1 |
| `dropbox:createShareLink` | 1 |

## Flow

```mermaid
flowchart LR
    m1["datastore:SearchRecord"]
    m2["json:ParseJSON"]
    m1 --> m2
    m3["elevenlabs:universal<br/><i>Only saved Offswitch generation IDs</i>"]
    m2 --> m3
    m4["datastore:UpdateRecord"]
    m3 --> m4
    m5["http:DownloadFile<br/><i>Completed video only</i>"]
    m4 --> m5
    m6["dropbox:uploadLargeFile"]
    m5 --> m6
    m7["dropbox:createShareLink"]
    m6 --> m7
    m8["datastore:UpdateRecord"]
    m7 --> m8
```
