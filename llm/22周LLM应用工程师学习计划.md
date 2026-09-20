# 22 周 LLM 应用工程师学习计划

- 时间投入：每周 12~18 小时（工作日 1~2h，周末 3~5h）
- 总周期：22 周，弹性到 24 周
- 建议开始：2026-09-21（下周一），结束约 2027-02-22；弹性到 2027-03-08
- 背景：C++ 基础扎实，数学不补；目标岗位偏实习 / 初级 LLM 应用 / AI 后端
- 原则：工作日写代码、调 bug；周末学新概念 + 做项目；每周必须有产出
- 网络：贯穿全周期，不单独停一个月学
- 周日固定：GitHub 提交 + 写 100 字总结 + 下周计划

---

## 一、先锁定技术栈（热门 + 零基础能跑通）

中途换框架最浪费时间。下面这套是 2026 年岗位里常见、文档多、Windows + conda 也能一周内跑起来的组合。原则：**热门里只选「pip/conda 装完就能用」的；要额外搭数据库、K8s、前端工程的一律后置。**

| 层 | 锁定 | 不学 / 后置（热但重） |
|---|---|---|
| 语言与包管理 | Python 3.12 + conda（一项目一环境，导出 `environment.yml`） | uv、poetry；不要混用 |
| Web | FastAPI + pydantic v2 + uvicorn | Django、Flask |
| 流式 | SSE | WebSocket 深挖 |
| 鉴权 | 先 API Key，第 9 周再 JWT | OAuth 全家桶 |
| LLM API | `openai` SDK + OpenAI 兼容协议。主账号：**阿里云百炼 / 通义**（聊天、embedding、rerank 一家齐）；第 3 周用 DeepSeek 练「只改 base_url」 | 同时接 5 家 SDK |
| Embedding | 通义 embedding API（不占显存） | 一上来本地部署 bge |
| 向量库 | 第 5 周 numpy 算余弦相似度（搞懂原理）；第 6 周 **Chroma**（`pip install` 即用） | pgvector / Milvus / Qdrant（要先装数据库） |
| 编排 | 先手写 ReAct；第 12 周 **LangGraph**（Agent 事实标准） | LangChain LCEL 链式全家桶、LlamaIndex（两套都学必乱） |
| 文档解析 | pymupdf（PDF）+ 纯 Markdown | Unstructured、Docling |
| 检索增强 | BM25（`rank_bm25`）+ 向量；rerank 用通义 API | 自己训 rerank 模型 |
| 评估 | 自建 50 条 + 检索命中率 / 忠实度；RAGAS 当加分 | 第 7 周被评估框架卡住 |
| 前端 | **Streamlit**（几行出聊天界面） | React / Next.js |
| 可观测 | 日志 + `request_id`；有余力再试 Langfuse | 一上来全套追踪平台 |
| 部署 | Docker Compose + Nginx | K8s |
| 本地模型 | **Ollama + Qwen3**（安装包，不用编译） | 三个推理引擎一起学 |
| 微调 | **Qwen3-8B-Instruct + QLoRA**（PEFT） | 14B/32B、全参微调 |
| 推理服务 | Ollama 跑通 → vLLM 提供 API；llama.cpp 留给 C++ 那一周 | 三者并行深挖 |
| 工具协议 | Function Calling；MCP 只做了解 | 以 MCP 当主路径 |
| 刷题 | 从第 1 周每周 3 题，第 19 周复习 | 第 19 周突击 100 题 |

### 为什么这样选（热门但不把新手淹死）

- **通义一家齐**：聊天、向量、rerank 同一把 Key，零基础少踩「embedding 维度对不上」。DeepSeek 用来证明 OpenAI 兼容协议，面试能讲。
- **Chroma 而不是 pgvector**：2026 年原型和教程的主流本地向量库，不用装 PostgreSQL。简历写 Chroma 完全够实习；有余力第 10 周再提一句「生产可换 pgvector」。
- **LangGraph 而不是 LangChain 链**：Agent 岗位问的是图 / 状态 / 重试。第 11 周先手写，第 12 周再迁到 LangGraph，既懂原理又能写热门关键词。
- **Qwen3 + Ollama**：中文资料最多、本地一键拉模型。微调用 8B，不要 2.5 旧版，也不要一上来 14B。
- **Streamlit**：RAG / Agent demo 的默认界面，别开前端工程。
- **先 API 后本地**：第 3~13 周全走云端 API，第 14 周才碰 GPU。没有显卡也能完成前两个项目。

账号与资源提前准备：

- GitHub、**阿里云百炼 API Key**、DeepSeek API Key、Docker Desktop、Ollama（第 16 周前装即可）
- 第 13 周末前准备 GPU：AutoDL / 阿里云 / Colab（微调 Qwen3-8B QLoRA，不要一上来 14B）
- 博客：掘金 / 知乎 / 个人 GitHub Pages，选一个坚持写

---

## 二、对原计划的补充（建议采纳）

原计划骨架是对的，下面几条能明显提高完成率和面试命中率。

### 1. 每周拆成「必做 / 应做 / 可砍」

12~18 小时撑不住「学一堆 + 做完整项目」。卡住时砍可砍项，不砍必做产出。

- 必做：能提交的代码 + 能演示的接口 / 脚本
- 应做：README、简单测试、一篇短文
- 可砍：第二种工具、完美 UI、完整 JWT、Nginx、RAGAS、C++ 网关的花活

### 2. 第 2 周原计划过载，拆开

原计划第 2 周同时上 FastAPI + SSE + JWT + Docker + Nginx，对 C++ 转 Python 的人偏满。

- 第 2 周必做：FastAPI 路由 + pydantic + SSE 流式聊天 + Docker 跑起来
- 第 2 周应做：API Key 鉴权
- 第 2 周可砍：JWT、Nginx → 挪到第 9 周部署时再做（那时更有意义）

### 3. 刷题从第 1 周开始，不要堆到第 19 周

第 19 周 12~18 小时刷 100 题不现实。改为：

- 第 1~18 周：每周 3 道（数组 / 哈希 / 双指针 / 栈 / 链表 / 二叉树 / BFS）
- 累计约 54 题后再在第 19 周补到 80~100，并复盘错题
- 题单锁 [LeetCode Hot 100](https://leetcode.cn/problem-list/2cktkvj/)，不要东刷西刷

### 4. 测试和成本从项目一开始就记

面试官会问延迟、价格、失败怎么办。从第 3 周起每个项目 README 固定三行：

- 延迟：首 token / 端到端 p50、p95
- 成本：每次请求大约多少 token、多少钱
- 失败：超时、限流、工具调用失败时怎么处理

pytest 不要等到第 10 周才写。第 6 周 RAG API 起，至少覆盖 `/ingest`、`/query` 各 2 个测试。

### 5. 三个项目的完成标准（宁少做好）

如果进度落后，砍项目 3 的复杂度，不要三个都半成品。

| 项目 | 完成线（能进简历） | 落后时的降级 |
|---|---|---|
| 项目 1 企业知识库 RAG | 上传文档、引用答案、评估报告、Docker Compose 可跑、有压测数字 | 不做混合检索 / rerank，保留引用和评估 |
| 项目 2 Agent 工作流 | 多工具、重试、流式、权限（能跑哪些工具）、至少 1 个 bad case 分析 | 不做 LangGraph，手写状态机也成立 |
| 项目 3 C++ 推理网关 | C++ HTTP 反代 + 连接池 + 转发到 vLLM，有延迟对比表 | 降级为「C++ 压测客户端 + 简短网关」，仍能讲差异化 |

### 6. 第 14~17 周先确认有卡，再开始微调

没有 GPU 就不要硬学训练细节。备选路径（同样能讲）：

- 用开源 LoRA 适配器加载演示
- 把时间加到 vLLM / llama.cpp 部署、量化对比、C++ 网关
- 面试叙事改成「推理部署 + 性能」而不是「我从零训了一个模型」

有卡则坚持 Qwen3-8B-Instruct + QLoRA，数据 500 条先跑通，质量比 2000 条脏数据重要。

### 7. 投递提前，不要第 21 周才找人

按 2026-09-21 开工，第 22 周约 2027-02 下旬，正好赶上春招实习 / 日常实习。

- 第 10 周：简历骨架（项目 1 就能写）
- 第 13 周：项目 2 补进简历
- 第 18 周：作品集 + 内推名单（同学、前同事、Boss/脉脉）
- 第 21 周：集中投 30~50 家，不是从零找岗位

岗位关键词：LLM 应用开发、RAG、AI 后端、算法工程（应用向）、大模型应用实习。

### 8. 面试会问、计划里要刻意练的点

原计划偏「能做出来」。补这几项，回答会明显更像做过生产：

- Prompt 注入 / 工具权限（Agent 不能随便跑删除、乱调外部 API）
- 引用幻觉：检索到了但模型没引用，或引用了错误 chunk
- 超时、重试、幂等、限流（网络贯穿的实战形态）
- 日志：request_id、token 用量、检索耗时、生成耗时分开打
- 系统设计口述：企业知识库的成本、延迟、更新（文档增删改）

### 9. 博客怎么写才有用

不要周记式「我学了什么」。每篇固定结构，可直接给面试官：

1. 问题是什么
2. 我怎么做的（架构图 / 关键代码路径）
3. 数字（延迟、召回、成本）
4. 踩坑与 bad case
5. 下一步

目标约 8 篇，而不是 22 篇水记录。建议篇目见文末。

### 10. 进度检查点（决定是否顺延）

| 节点 | 通过标准 | 未通过就怎样 |
|---|---|---|
| 第 4 周末 | 命令行机器人能流式 + 工具调用 demo 能跑 | 第 5 周继续补，RAG 最多顺延 1 周 |
| 第 10 周末 | 项目 1 能演示、有评估数字、Docker 可启动 | 动用弹性周，Agent 后移 |
| 第 13 周末 | 项目 2 能演示多工具 + 流式 | 微调可缩短为「部署别人的 LoRA」 |
| 第 17 周末 | 本地或云上能提供一个推理 API，并有延迟数字 | 砍 C++ 网关花活，保作品集时间 |
| 第 20 周末 | 简历一页、三个项目都能讲 10 分钟 | 第 21 周少投，先补项目故事 |

总周期尽量不超过 24 周。某周卡住可以顺延，但只顺延一次、只顺延当前阶段。

---

## 三、总阶段

- 第 1~2 周：网络 + Python + FastAPI
- 第 3~4 周：LLM API + Prompt + Function Calling
- 第 5~7 周：RAG 基础
- 第 8~10 周：RAG 进阶 + 部署 + 评估打磨
- 第 11~13 周：Agent
- 第 14~17 周：微调 + 推理部署（发挥 C++ 优势）
- 第 18~20 周：作品集 + 八股 + 模拟面试
- 第 21~22 周：投递 + 面试复盘

---

## 第 1~2 周：网络 + Python + FastAPI

### 第 1 周：HTTP + Python 过渡

学：

- HTTP 方法、状态码、Header、Body、REST、JSON、curl
- Python 对比 C++：list/dict、推导式、生成器、类型标注、conda 环境

产出：

- 用 curl 调公开 API（推荐 `https://httpbin.org` 和 GitHub REST）
- 用 Python 重写一个自己熟悉的 C++ 小工具（文件处理 / 日志解析即可，别新开大项目）
- 笔记《一次 HTTP 请求发生了什么》（从 DNS、TCP、TLS、请求行、到响应体）
- 本周 3 道 LeetCode

必做 / 应做 / 可砍：

- 必做：curl 调通 + Python 小工具能跑 + 笔记
- 应做：把小工具放到 GitHub，README 写清怎么运行
- 可砍：TLS 握手细节、自己实现 HTTP 解析器

### 第 2 周：FastAPI + SSE + 鉴权 + Docker

学：

- FastAPI 路由、请求体、响应模型、pydantic
- SSE 流式输出；API Key（本周）/ Bearer / JWT（可挪第 9 周）
- Docker 端口；Nginx 反向代理（可挪第 9 周）；WebSocket 简介（只看差异，不实现）

产出：

- 流式聊天接口（先 mock 分词输出，第 3 周再接真模型）
- API Key 鉴权；Docker 跑起来
- 短博客：SSE 和普通 HTTP 有什么区别

必做 / 应做 / 可砍：

- 必做：`POST /chat` SSE + Dockerfile 能 `docker run` 访问
- 应做：API Key 中间件、`.env`、README
- 可砍：JWT 登录页、Nginx；留下接口注释，第 9 周接上

---

## 第 3~4 周：LLM API + Prompt

### 第 3 周：LLM API 基础

学：`openai` SDK（OpenAI 兼容）、token、temperature、top_p、流式解析、超时重试。本周主用 **通义**，再用 DeepSeek 只改 `base_url` 和 `api_key` 验证同一套代码。

产出：命令行聊天机器人，支持流式输出和错误重试；记录一次请求的 token 与耗时

### 第 4 周：Prompt + Function Calling

学：Prompt 模板、Few-shot、JSON mode、Function Calling、工具定义与参数校验

产出：天气 / 计算器工具调用 demo（天气可 mock）；博客《一次 Function Calling 的完整往返》

补充：工具失败时模型怎么看到错误并重试，这是后面 Agent 的核心，本周就要写出来。

---

## 第 5~7 周：RAG 基础

### 第 5 周：RAG 基础 1

学：pymupdf 解析 PDF、Markdown 切分、chunk 策略（按标题、按长度、重叠）、通义 embedding API、余弦相似度（numpy 手算，搞懂再谈库）

产出：最小 RAG，本地上传一份 PDF 命令行问答

补充：chunk 先锁 400~800 汉字、overlap 10%~20%。本周不要上向量数据库，用 `numpy` 存向量、算相似度即可。

### 第 6 周：RAG 基础 2

学：向量库 **Chroma**（持久化目录）、top-k 检索、Prompt 拼接、引用来源

产出：RAG API：`POST /ingest`、`POST /query`，答案里带 chunk 引用；至少 4 个 pytest

补充：Chroma 一个 `PersistentClient(path="chroma_db")` 就能存盘，不要并行再装 Postgres。

### 第 7 周：RAG 评估

学：构建 50 条评估集、召回率、忠实度、答案正确率、LLM as Judge；RAGAS 作加分

产出：评估报告、bad case 分析、博客

补充：50 条自己写，覆盖「答案在文档里 / 不在文档里 / 需要跨段」。先算「检索命中率」（标准答案所在 chunk 是否进 top-k），再谈生成质量。

---

## 第 8~10 周：RAG 进阶 + 部署

### 第 8 周：RAG 进阶

学：混合检索 BM25 + Chroma 向量、通义 rerank API、查询改写、缓存

产出：同一评估集上的召回率对比表；更新 README

补充：一次只改一个变量。先 BM25+Chroma 向量，再用通义 rerank API。缓存用「问题归一化后的哈希」，别一上来 Redis。

### 第 9 周：RAG 部署

学：FastAPI 异步、Docker Compose、Nginx、日志、环境变量、限流、JWT（若第 2 周没做）

产出：能访问的在线 demo（本机映射或一台云主机）；压测延迟；博客

补充：压测用 wrk / hey / locust 任一。数字写进 README：并发、QPS、p95。日志带 `request_id`。

### 第 10 周：项目 1 打磨

做：代码重构、pydantic、测试、README 架构图、录屏 2~3 分钟

产出：项目 1 完成——企业知识库 RAG；简历骨架第一版

---

## 第 11~13 周：Agent

### 第 11 周：Agent 基础

学：ReAct、Function Calling、多工具、错误重试、权限（白名单工具、超时、禁止危险操作）

产出：数据分析 Agent 雏形：CSV → SQL 或 Python → 图

### 第 12 周：Agent 进阶

学：把第 11 周手写循环迁到 **LangGraph**（State、Node、边、重试）；记忆、流式 SSE；MCP 只看 30 分钟介绍，不实现

产出：多工具 + 重试 + 流式工作流；Streamlit 能看到每一步调用了哪个工具

### 第 13 周：Agent 部署 + 项目 2

做：FastAPI + Streamlit、Docker、几条评估用例（任务成功 / 工具选错 / 中途失败恢复）

产出：项目 2 完成——Agent 工作流；博客；准备 GPU 账号给下周用

---

## 第 14~17 周：微调 + 推理部署（C++ 优势）

### 第 14 周：微调基础

学：LoRA / QLoRA 原理、数据构造、Qwen3-8B-Instruct、PEFT、训练脚本

产出：500~2000 条领域数据（先 500 高质量）；LoRA 微调跑通一个 epoch 也算

### 第 15 周：微调评估

学：base vs LoRA、指标、过拟合、合并模型

产出：微调评估报告（同一 30 条问题对比）；博客

### 第 16 周：推理部署

学：先 **Ollama 拉 Qwen3** 聊天跑通，再 vLLM 提供 OpenAI 兼容 API；量化只看 GGUF（Ollama）和 AWQ（vLLM）在显存 / 延迟上的差别

产出：本机 `ollama run qwen3` 能聊；再起一个 vLLM API；压测表（不同并发）

### 第 17 周：C++ 推理网关（差异化）

做：C++ HTTP 服务或网关、反向代理、连接池、把请求转到 vLLM；Python 只做编排

产出：C++ 网关 + vLLM 后端；直连 vs 经网关的延迟对比；项目 3

补充：网关价值讲「连接复用、超时、鉴权、限流、日志」，不要做成不完整的自研推理引擎。

---

## 第 18~20 周：作品集 + 八股 + 模拟面试

### 第 18 周：作品集 + 博客

做：整理 3 个项目 README、架构图、指标、bad case、博客合集；GitHub 主页 pinned

产出：GitHub 作品集；简历初稿（一页）；列出 20 个内推 / 投递目标

### 第 19 周：八股 + 刷题

学：HTTP / SSE / JWT / Docker / Nginx；RAG / Agent / Transformer / Attention

产出：累计刷题到 80~100；八股笔记（用自己项目里的数字举例）

### 第 20 周：模拟面试 + 项目深挖

做：STAR、项目问答、系统设计（企业知识库、成本 / 延迟 / 更新）

产出：模拟面试 3 次（一次录音复盘即可）；简历定稿

---

## 第 21~22 周：投递 + 复盘

### 第 21 周：投递

做：内推、实习 / 初级 LLM 应用 / AI 后端；投递记录表（公司、岗位、渠道、时间、反馈）

产出：投 30~50 家；每投 10 家跟进一次

### 第 22 周：面试复盘 + 补漏

做：根据面试反馈补短板；继续投

产出：复盘表（题目、我的回答、更好的回答）；持续面试

---

## 四、网络怎么贯穿

- 第 1~2 周：HTTP / REST / SSE / 鉴权 / Docker 基础（Nginx、JWT 可落到第 9 周）
- 第 3 周：流式解析、超时重试
- 第 5~10 周：RAG 服务、鉴权、部署、压测
- 第 11~13 周：SSE、并发、工具调用超时
- 第 14~17 周：反向代理、推理服务、延迟与吞吐
- 第 18~20 周：集中复习网络八股，全部用自己项目里的数字回答

这样到第 6 周写 RAG API 时已经熟悉 HTTP / SSE，到第 10 周部署也练过，到第 17 周反向代理和压测也做过。网络是练出来的，不是看出来的。

---

## 五、第 1 周每日拆解（约 14 小时）

假设工作日晚上 1.5h，周六 4h，周日 3.5h。可按自己班次平移，但不要把编码全堆到周日。

| 日 | 时长 | 做什么 | 当天结束标准 |
|---|---|---|---|
| 一 | 1.5h | 确认 conda、Git；建环境 `llm-w1`（Python 3.12）；用 C++ 对比着写 list/dict/函数；curl 调 httpbin 的 GET/POST | `conda activate llm-w1` 后 Python 能跑；curl 能看到 JSON |
| 二 | 1.5h | HTTP 方法、状态码、Header vs Body；写笔记大纲；LeetCode 1 题 | 能口述 GET 和 POST 的区别 |
| 三 | 1.5h | REST 与 JSON；用 curl 调一个真 API（GitHub 或天气）；保存请求 / 响应到文件 | 有一份「请求原文 + 响应原文」 |
| 四 | 1.5h | Python 推导式、生成器、类型标注、异常；开始重写 C++ 小工具 | 小工具能处理一个样例文件 |
| 五 | 1.5h | 把小工具补完；写 README；LeetCode 1 题 | GitHub 仓库能 clone 后运行 |
| 六 | 4h | 系统看一遍 HTTP 请求链路（DNS/TCP/TLS/HTTP）；补笔记成文；再练 5 个 curl 场景（重定向、自定义 Header、401） | 《一次 HTTP 请求发生了什么》初稿 |
| 日 | 3.5h | 改笔记；LeetCode 1 题；GitHub 提交；100 字总结；写下周计划 | 本周三个产出都在仓库里 |

第 1 周参考（只看文档，不追课）：

- [MDN HTTP](https://developer.mozilla.org/zh-CN/docs/Web/HTTP)
- Python 官方教程「数据结构」一章
- conda：`create` / `activate` / `env export`；包用 `conda install` 或环境内 `pip install`，不要混乱装到 base

---

## 六、第 2 周每日拆解（约 15 小时）

| 日 | 时长 | 做什么 | 当天结束标准 |
|---|---|---|---|
| 一 | 1.5h | FastAPI 官方教程：路由、Path、Query；hello world | 浏览器或 curl 能打到 `/health` |
| 二 | 1.5h | pydantic 模型、请求体、响应模型、校验错误 | 非法 JSON 返回 422 |
| 三 | 1.5h | SSE：`StreamingResponse`，mock 按 token 吐文字；curl `-N` 看流 | curl 能一块块刷出文本 |
| 四 | 1.5h | API Key 中间件；`.env`；错误码整理 | 没 Key 是 401，有 Key 能聊 |
| 五 | 1.5h | 写 Dockerfile；本机 `docker run -p 8000:8000`；LeetCode 1 题 | 容器外能访问 `/health` 和 `/chat` |
| 六 | 4h | 补日志和 README；录 30 秒演示；了解 JWT 和 Nginx 即可（实现可留第 9 周）；若有余力再加 Nginx 反代 | Docker 演示可重复 |
| 日 | 3.5h | 写短博客《SSE 和普通 HTTP》；LeetCode 2 题；提交 + 100 字总结 + 下周计划 | 第 2 周必做全部完成 |

若周六提前做完必做，再加：JWT 登录或 Nginx。加不完不算失败。

---

## 七、周日仪式（每周同样三件事）

1. GitHub 至少一次有意义的提交（不是空 README）
2. 100 字总结：做成了什么、卡在哪、数字是多少
3. 下周计划：只写必做，应做和可砍分开

建议在仓库里放 `weekly/YYYY-MM-DD.md`，投递和面试时就是时间线证据。

---

## 八、建议的 8 篇博客（不要写 22 篇流水账）

1. 一次 HTTP 请求发生了什么
2. SSE 和普通 HTTP 有什么区别
3. 一次 Function Calling 的完整往返
4. 我的 RAG chunk 策略和召回数字
5. 企业知识库：延迟、成本、bad case
6. Agent 工具失败之后怎么办
7. QLoRA 前后对比（或：Qwen3-8B 量化部署的显存与延迟）
8. 为什么用 C++ 做推理网关（有对比表）

---

## 九、卡住时怎么砍（保 24 周上限）

- 第 2 周炸了：保 FastAPI + SSE，JWT/Nginx 全部后移
- 第 7~8 周评估做不动：50 条集 + 检索命中率即可，RAGAS 放弃
- 第 12 周 LangGraph 看不懂：手写状态机，简历照样写 Agent
- 第 14 周没 GPU：改走「Ollama + vLLM 部署 + C++ 网关」，微调只学原理
- 第 17 周网关太大：做最小反向代理 + 延迟表，把时间还给作品集
- 整体落后超过 2 周：放弃「三个大项目」，保项目 1 质量 + 项目 2 能演示

---

## 十、第 1 周开工清单

- [ ] 确认 conda、Git、Docker Desktop、VS Code / Cursor；新建 Python 3.12 环境，不要用 base
- [ ] 注册 GitHub、**阿里云百炼** API Key（聊天 + embedding）；DeepSeek Key 第 3 周对照着用
- [ ] 新建仓库 `llm-learning` 或按项目分仓，先有一个就行
- [ ] 选一个要重写的 C++ 小工具（必须是你已经写过的）
- [ ] 周日晚上把本文件里「第 1 周每日」勾完
