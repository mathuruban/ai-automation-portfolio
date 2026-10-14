# AI news video pipeline: master scenario (generated)

- Modules: **90** (routers: 1, branches: 17)
- Modules with filters: 21; modules with error handlers: 2

## Apps used

| App | Modules |
|---|---|
| datastore | 56 |
| http | 9 |
| ai-local-agent | 4 |
| apify | 4 |
| rss | 3 |
| creatomate | 3 |
| json | 2 |
| elevenlabs | 2 |
| dropbox | 2 |
| youtube | 2 |
| builtin | 1 |
| util | 1 |
| gemini-ai | 1 |

## Actions

| Action | Count |
|---|---|
| `datastore:UpdateRecord` | 28 |
| `datastore:SearchRecord` | 18 |
| `http:MakeRequest` | 7 |
| `datastore:ExistRecord` | 5 |
| `datastore:AddRecord` | 5 |
| `ai-local-agent:RunLocalAIAgent` | 4 |
| `apify:apifyApiCall` | 4 |
| `rss:ActionReadArticles` | 3 |
| `creatomate:RenderJSON` | 2 |
| `http:DownloadFile` | 2 |
| `builtin:BasicRouter` | 1 |
| `json:TransformToJSON` | 1 |
| `elevenlabs:createTextToSpeech` | 1 |
| `dropbox:uploadLargeFile` | 1 |
| `dropbox:createShareLink` | 1 |
| `util:FunctionSleep` | 1 |
| `creatomate:MakeApiCall` | 1 |
| `gemini-ai:createACompletionGeminiPro` | 1 |
| `json:ParseJSON` | 1 |
| `youtube:universal` | 1 |
| `youtube:uploadVideo` | 1 |
| `elevenlabs:listvoices` | 1 |

## Flow

```mermaid
flowchart LR
    m1["builtin:BasicRouter"]
    m710["rss:ActionReadArticles"]
    m1 --> m710
    m711["datastore:ExistRecord"]
    m710 --> m711
    m712["datastore:AddRecord<br/><i>Skip an exact URL already in Research Candidates</i>"]
    m711 --> m712
    m810["rss:ActionReadArticles"]
    m1 --> m810
    m811["datastore:ExistRecord"]
    m810 --> m811
    m812["datastore:AddRecord<br/><i>Skip an exact URL already in Research Candidates</i>"]
    m811 --> m812
    m910["rss:ActionReadArticles"]
    m1 --> m910
    m911["datastore:ExistRecord"]
    m910 --> m911
    m912["datastore:AddRecord<br/><i>Skip an exact URL already in Research Candidates</i>"]
    m911 --> m912
    m1210["datastore:SearchRecord"]
    m1 --> m1210
    m1211["datastore:UpdateRecord<br/><i>Official HTTPS sources only</i>"]
    m1210 --> m1211
    m1212["datastore:ExistRecord"]
    m1211 --> m1212
    m1213["http:MakeRequest<br/><i>Never overwrite an existing source job</i>"]
    m1212 --> m1213
    m1214["datastore:AddRecord<br/><i>Successful substantive source response</i>"]
    m1213 --> m1214
    m1215["datastore:UpdateRecord"]
    m1214 --> m1215
    m1512["datastore:SearchRecord"]
    m1 --> m1512
    m1513["datastore:UpdateRecord"]
    m1512 --> m1513
    m1518["http:MakeRequest<br/><i>Official HTTPS sources only</i>"]
    m1513 --> m1518
    m1514["ai-local-agent:RunLocalAIAgent<br/><i>Valid complete article-only source response</i>"]
    m1518 --> m1514
    m1515["datastore:SearchRecord"]
    m1514 --> m1515
    m1516["ai-local-agent:RunLocalAIAgent"]
    m1515 --> m1516
    m1517["datastore:UpdateRecord"]
    m1516 --> m1517
    m110["datastore:SearchRecord"]
    m1 --> m110
    m1190["datastore:SearchRecord"]
    m110 --> m1190
    m111["datastore:UpdateRecord"]
    m1190 --> m111
    m112["ai-local-agent:RunLocalAIAgent"]
    m111 --> m112
    m113["ai-local-agent:RunLocalAIAgent"]
    m112 --> m113
    m1611["json:TransformToJSON"]
    m113 --> m1611
    m114["datastore:UpdateRecord"]
    m1611 --> m114
    m1810["datastore:SearchRecord"]
    m1 --> m1810
    m1811["datastore:SearchRecord"]
    m1810 --> m1811
    m1812["datastore:ExistRecord"]
    m1811 --> m1812
    m1813["datastore:AddRecord<br/><i>Explicit active allocation, eligible fixed render package and unused Zurich day </i>"]
    m1812 --> m1813
    m1814["datastore:UpdateRecord"]
    m1813 --> m1814
    m1815["datastore:UpdateRecord"]
    m1814 --> m1815
    m210["datastore:SearchRecord"]
    m1 --> m210
    m211["datastore:UpdateRecord<br/><i>Reviewed media package, live budget, exact channel, no prior audio/render</i>"]
    m210 --> m211
    m212["elevenlabs:createTextToSpeech"]
    m211 --> m212
    m213["dropbox:uploadLargeFile"]
    m212 --> m213
    m214["datastore:UpdateRecord"]
    m213 --> m214
    m215["dropbox:createShareLink"]
    m214 --> m215
    m216["datastore:UpdateRecord"]
    m215 --> m216
    m217["datastore:UpdateRecord<br/><i>Approved source plus recorded cost preflight; no prior render</i>"]
    m216 --> m217
    m218["creatomate:RenderJSON"]
    m217 --> m218
    m219["datastore:UpdateRecord"]
    m218 --> m219
    m1816["util:FunctionSleep"]
    m219 --> m1816
    m310["datastore:SearchRecord"]
    m1 --> m310
    m311["datastore:UpdateRecord<br/><i>One explicitly approved repair, current budget and source, prior render present</i>"]
    m310 --> m311
    m312["creatomate:RenderJSON"]
    m311 --> m312
    m313["datastore:UpdateRecord"]
    m312 --> m313
    m1110["datastore:SearchRecord"]
    m1 --> m1110
    m1111["creatomate:MakeApiCall"]
    m1110 --> m1111
    m1112["datastore:UpdateRecord<br/><i>Exact requested render only</i>"]
    m1111 --> m1112
    m1710["datastore:SearchRecord"]
    m1 --> m1710
    m1713["http:MakeRequest<br/><i>Official HTTPS sources only</i>"]
    m1710 --> m1713
    m1711["datastore:UpdateRecord<br/><i>Valid complete article-only source response</i>"]
    m1713 --> m1711
    m1712["http:DownloadFile"]
    m1711 --> m1712
    m1714["gemini-ai:createACompletionGeminiPro"]
    m1712 --> m1714
    m1715["json:ParseJSON"]
    m1714 --> m1715
    m1716["datastore:UpdateRecord"]
    m1715 --> m1716
    m410["datastore:SearchRecord"]
    m1 --> m410
    m411["datastore:UpdateRecord<br/><i>Checked personal Short, complete metadata and no previous publication</i>"]
    m410 --> m411
    m1415["datastore:SearchRecord"]
    m411 --> m1415
    m412["http:MakeRequest"]
    m1415 --> m412
    m413["datastore:UpdateRecord<br/><i>Successful exact personal Buffer draft and preserved full QA receipt</i>"]
    m412 --> m413
    m1410["datastore:SearchRecord"]
    m1 --> m1410
    m1411["http:MakeRequest<br/><i>Validated stored Buffer ID</i>"]
    m1410 --> m1411
    m1412["datastore:UpdateRecord<br/><i>Exact personal draft, reviewed media and future time</i>"]
    m1411 --> m1412
    m1413["http:MakeRequest"]
    m1412 --> m1413
    m1414["datastore:UpdateRecord"]
    m1413 --> m1414
    m1310["datastore:SearchRecord"]
    m1 --> m1310
    m1311["http:MakeRequest<br/><i>Validated stored Buffer ID</i>"]
    m1310 --> m1311
    m1312["datastore:UpdateRecord"]
    m1311 --> m1312
    m510["datastore:SearchRecord"]
    m1 --> m510
    m511["youtube:universal"]
    m510 --> m511
    m512["datastore:UpdateRecord<br/><i>Exact channel + cooldown + no existing upload</i>"]
    m511 --> m512
    m513["http:DownloadFile"]
    m512 --> m513
    m514["youtube:uploadVideo"]
    m513 --> m514
    m516["datastore:UpdateRecord"]
    m514 --> m516
    m610["datastore:SearchRecord"]
    m1 --> m610
    m611["datastore:UpdateRecord"]
    m610 --> m611
    m612["apify:apifyApiCall"]
    m611 --> m612
    m613["apify:apifyApiCall"]
    m612 --> m613
    m614["apify:apifyApiCall"]
    m613 --> m614
    m615["apify:apifyApiCall"]
    m614 --> m615
    m616["datastore:UpdateRecord"]
    m615 --> m616
    m1010["datastore:SearchRecord"]
    m1 --> m1010
    m1011["datastore:UpdateRecord"]
    m1010 --> m1011
    m1012["elevenlabs:listvoices"]
    m1011 --> m1012
```
