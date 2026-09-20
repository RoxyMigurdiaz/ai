# logstat

第 1 周小工具：解析访问日志 / JSONL，统计状态码、延迟分位数（p50/p95/max）和最慢请求。只依赖 Python 标准库。

## 运行

在本目录下：

```powershell
cd E:\ai\llm\week1
python logstat.py access.log
python logstat.py app.jsonl --slow 3
python logstat.py app.jsonl --path /chat --errors
```

| 参数 | 说明 |
|---|---|
| `logfile` | 日志文件路径（必填） |
| `--path` | 只保留 path 包含该子串的请求 |
| `--errors` | 只保留 status ≥ 400 |
| `--slow N` | 打印最慢的 N 条，默认 5 |

## 支持的格式

自动识别：首行非空内容以 `{` 开头按 JSONL，否则按访问日志。

**访问日志**（末尾耗时为秒，内部会换成毫秒）：

```text
10.0.0.8 - - [20/Sep/2026:12:00:03 +0800] "POST /chat HTTP/1.1" 200 880 0.210
```

**JSONL**（`latency_ms` 已是毫秒）：

```json
{"request_id": "req-002", "method": "POST", "path": "/chat", "status": 200, "latency_ms": 210.0}
```
