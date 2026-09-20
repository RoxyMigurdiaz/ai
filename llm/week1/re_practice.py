import re

"""
正则速查（本文件练手用）

【基本流程】
  p = re.compile(r"规则")   # r"" 原始字符串，\\d 写成 \\d 即可
  m = p.match(s)            # 必须从字符串开头匹配
  m = p.search(s)           # 在任意位置找第一处
  m is None                 # 没对上
  m.group() / m.group(0)    # 整段匹配到的文本
  m.group(1), m.group(2)    # 第 1、2 个捕获组（要有括号）
  m.groups()                # 所有捕获组构成的元组
  len(m.groups())           # 捕获组个数
  m.groupdict()             # 命名分组 -> 字典

【常用零件】
  abc       字面量
  \d       一个数字 0-9
  \d+      一个或多个数字
  \d{3}    刚好 3 个数字
  \S       一个非空白字符
  \S+      一截非空白（词、路径等）
  \s       一个空白
  .         任意一个字符（除换行）
  \.       真正的点号 .
  [\d.]+   数字或点，重复多次（可匹配 0.210）
  ^  $      行首 / 行尾

【分组】
  (规则)              捕获组，用 group(1)、group(2) 取
  (?P<名字>规则)      命名捕获组，用 group("名字") 或 groupdict()
  没有括号 = 没有捕获组，groups() 为空，只有 group(0)

【易错】
  规则里的空格是字面量：\d+ \. \d+ 匹配的是 "0 . 210"，不是 "0.210"
  小数应用 \d+\.\d+ 或 [\d.]+
  找串中间的内容用 search，不要用 match（除非模式从行首写起）
  先判断 m is not None，再调用 group()
"""

practice1 = {"str" : "latency 0.210 sec", "anser" : "0.210"}
practice2 = {"str" : "POST /chat HTTP/1.1", 
        "anser" : {"group1" : "POST", "group2" : "/chat"}}
practice3 = {"str" : "10.0.0.8 - - [20/Sep/2026:12:00:03 +0800] 'POST /chat HTTP/1.1' 200 880 0.210", 
        "anser" : {"group1" : "10.0.0.8",
                   "group2" : "20/Sep/2026:12:00:03 +0800"},
                   "group3" : "POST",
                   "group4" : "/chat",
                   "group5" : "HTTP/1.1",
                   "group6" : "200",
                   "group7" : "880",
                   "group8" : "0.210"}
        

def test_1():
    print('-' * 10, "test_1", '-' * 10)
    p = re.compile(r"\d+\.\d+")
    m = p.search(practice1["str"])
    if m is None:
        print("search failed!")
        return
    print(f'm.groups(): {m.groups()}, {m.group() == practice1["anser"]}' )

def test_2():
    print('-' * 10, "test_2", '-' * 10)
    p = re.compile(r"(?P<method>\S+) (?P<path>\S+)")
    m = p.search(practice2["str"])
    if m is None:
        print("search failed!")
        return
    print(f'm.groups(): {m.groups()}')
    if len(m.groups()) >= 2:
        print(m.group(1) == practice2["anser"]["group1"])
        print(m.group(2) == practice2["anser"]["group2"])
    else:
        print("wrong anser")

def test_3():
    print('-' * 10, "test_3", '-' * 10)
    p = re.compile(r"(\d+\.\d+\.\d+\.\d+) - - (\[.*\]) '(?P<method>\S+) (?P<path>\S+) (?P<protocol>\S+)' (?P<status>\d+) \d+ (?P<spend_time>\d+\.\d+)") 
    m = p.match(practice3["str"])
    if m is None:
        return None
    print(f'm.groups: {m.groups()}')
    print(f'm.groupdict(): {m.groupdict()}')


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()