from pathlib import Path
import re
import json
import argparse
import sys

p = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - (\[.*\]) "(?P<method>\S+) (?P<path>\S+) (?P<protocol>\S+)" (?P<status>\d+) \d+ (?P<latency_ms>\d+\.\d+)') 
required = ("method", "path", "status", "latency_ms")

def parse_access_line(line):
    """按照访问日志格式解析"""
    """ 10.0.0.8 - - [20/Sep/2026:12:00:03 +0800] "POST /chat HTTP/1.1" 200 880 0.210 """
    m = p.match(line)
    if m is None:
        return None
    record = m.groupdict()
    record['latency_ms'] = float(record['latency_ms']) * 1000
    record['request_id'] = "-"
    return record

def parse_jsonl_line(line):
    try:
        json_obj = json.loads(line)
    except json.JSONDecodeError:
        return None
    if any(key not in json_obj for key in required):
        return None

    return json_obj

def percentile(values, ratio):
    values = sorted(values)
    max_len = len(values)
    index = round((max_len - 1) * ratio)
    index = min(max(index, 0), max_len - 1)
    return values[index]

def main() -> int:
    parser = argparse.ArgumentParser(description='log stats')
    parser.add_argument("logfile", type=Path, help="path to log file")
    parser.add_argument("--path", default=None, help="path substring filter")
    parser.add_argument("--errors", action="store_true", help="only status >= 400")
    parser.add_argument("--slow", type=int, default=5, help="how many slowest")
    args = parser.parse_args()
    if args.slow < 1:
        print("--slow must be >= 1", file=sys.stderr)
        return 1
    if not args.logfile.is_file():
        print(f'file not found: {args.logfile}', file=sys.stderr)
        return 1

    log_path = args.logfile
    lines = log_path.read_text(encoding='utf-8').splitlines()
    parsed = skipped = 0
    all_logs = []
    parse_function = None
    for line in lines:
        line = line.strip()
        if parse_function is None:
            parse_function = parse_jsonl_line if line.startswith('{') else parse_access_line
        parsed_result = parse_function(line)
        if parsed_result is None:
            skipped += 1
        else:
            parsed += 1
            all_logs.append(parsed_result)
    print(f'file lines: {len(lines)}, parsed lines: {parsed}, skipped lines: {skipped}')

    path_substr = args.path
    errors_only = args.errors
    matched = []
    for record in all_logs:
        if path_substr and path_substr not in record['path']:
            continue
        if errors_only and int(record['status']) < 400:
            continue
        matched.append(record)

    if len(matched) == 0:
        print('没有对应记录')
        return 0

    counts = {}
    for record in matched:
        status = int(record['status'])
        counts[status] = counts.get(status, 0) + 1

    print('status')
    for status, count in sorted(counts.items()):
        print(f'{status}: {count}')

    print('latency_ms')
    latencies = [float(record['latency_ms']) for record in matched]
    print(f'p50  {percentile(latencies, 0.5)}')
    print(f'p95  {percentile(latencies, 0.95)}')
    print(f'max  {max(latencies)}')
    
    n = args.slow
    slowest = sorted(matched, key=lambda r: float(r['latency_ms']), reverse=True)[:n]

    print(f'slowest_{n}')
    for record in slowest:
        print(
            f'{float(record["latency_ms"]):7.1f}    {record["status"]}    '
            f'{record["method"]:6}  {record["path"]}    {record.get("request_id", "-")}'
        )

    return 0

if __name__ == '__main__':
    raise SystemExit(main())