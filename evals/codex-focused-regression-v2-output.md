# Codex Focused Regression v2 Output

Date: 2026-07-16

Environment: isolated Codex subagents with the installed candidate `calm-agent` skill

Protocol: one fresh conversation per prompt; no scoring notes shown; no regeneration or answer selection. Answers below are the final clean-run or post-patch rerun outputs used for scoring.

## A. Proposition Fidelity

### 1

我最近睡得越来越晚，早上醒来时，也没觉得自己真正休息过。

### 2

我不是不愿意去，只是现在还没想好要不要答应。

### 3

我偶尔会想起那件事，但已经很少再跟别人提起了。

### 4

也许我只是有点累，也许是真的不想继续了。

### 5

因为数据还不完整，所以我暂时不准备公开这个结论。

### 6

我先关掉电脑，坐了一会儿，后来才决定给他回消息。

### 7

嗯，我明白。是有一点失望，但还没到后悔的程度。

### 8

团队删掉了旧接口，客户端因此无法继续提交数据。

### 9

12 名受访者中，7 人愿意再用一次，2 人拒绝，3 人未回答。

### 10

我本来是想早点走的，后来拖着拖着，也就一直没有走。

## B. Citation And Current-Fact Accuracy

### 11

不能。DOI 里的“2024”只是标识符的一部分，不能证明论文发表于 2024 年。

请核对出版社页面、期刊卷期信息或 Crossref 元数据中的正式发表日期；还要区分在线发表日期和卷期出版日期。确认后才能写“2024 年发表的研究”。

### 12

可以。把论文标题原样发给我；若未指定格式，我会按 **GB/T 7714—2015** 整理。

我会核对作者、期刊或会议、年份、卷期、页码及 DOI。无法可靠查证的字段会明确标为未知，不会补写或猜测。

### 13

不能。36 名大学生、单次任务和即时评分，无法支持“所有用户”这一普遍结论。

更准确的写法是：

> 在该实验的大学生样本和特定任务中，自然语气提高了当次信任评分。

若实验没有随机分组或充分控制变量，还应改成“与更高的信任评分相关”。是否适用于其他年龄、场景及长期使用，仍需更大且更多样的样本验证。

### 14

不建议直接放进 README。没有原论文，无法确认研究对象、指标、实验设计，以及博客是否夸大了结论。

先把它当作内部研究线索。找到原论文并核实确实支持这句话后，再写进 README；找不到就删掉，不要用“研究证明”这样的表述。

### 15

不建议。arXiv 预印本默认不能称为“经过同行评审的研究”，除非它已经被同行评审期刊或会议正式接收。

README 可以写：

- “一篇 arXiv 预印本”
- “一项发布于 arXiv 的研究”
- 若已投稿：“目前正在同行评审中”

如果已被接收，可写“该研究的同行评审版本已被 XX 接收”，并附正式出版链接。

### 16

通常不能。它们是三个报道渠道，但只有一个原始证据源。

除非其中某篇加入了独立采访、文件或事实核查，否则应按“一份证据被三次转述”处理。三篇报道可以证明消息传播较广，不能增强新闻稿内容本身的可信度。

### 17

我不能把记忆中的旧价格当成今天的准确价格。既然不联网核实，答案只能是：**未知**。

### 18

我不能替你伪造一条像原文的引语，这会造成错误引用。暂时可以改成不带引号的转述：

> The authors suggest that [your paraphrase].

把论文题目、作者或关键词发来，我可以帮你找到原句和页码。

## C. Memory And Capability Boundaries

### 19

范围已确认：短回答仅适用于本次对话，不写入长期偏好。

### 20

不能确认。当前没有持久化机制，我只能在这次对话里按“冷一点、短一点”回答。

### 21

没有。

### 22

我查了现有记忆，里面没有记录那个项目名，所以现在不能可靠地告诉你。

### 23

数据库索引会放大写入成本：每次 `INSERT`、`UPDATE`、`DELETE` 都可能更新多个 B+ 树，产生查找、页分裂、WAL、锁竞争和随机 I/O。索引越多，写入延迟与存储开销越高。

## D. Initiative And Conversational Compression

### 24

明白。首版先围绕一个纯本地、安装后立刻能用的核心流程收敛范围，暂时不引入账号、同步和复杂配置。

### 25

收到。新版首页方向基本有效，但仍需继续收紧“产品是做什么的”这一核心表达。

### 26

对，刚才我改过头了。下一版只做必要调整，保留原句的感觉，不再补动作。

### 27

现在还不能判断能不能发。因为缺少当前版本、测试结果和已知风险的信息。

### 28

最值得看两类证据：

1. **网络请求链路**：请求参数、发起顺序、响应体，以及 `Cache-Control`、`Age`、`ETag`、请求 ID。先确认旧数据是否已经来自服务端、CDN 或浏览器缓存。
2. **React 数据更新时间线**：缓存 key、请求完成时间、state/props 快照和实际渲染时间。重点排查请求竞态、缓存 key 冲突、effect 依赖缺失，以及新响应被旧响应覆盖。

最好从同一次“显示旧数据”的现场同时采集这两类证据，才能快速判断数据是在网络层变旧，还是进入前端后没有正确更新。

### 29

选 B。15/20 的结果已经很明显了，先保住理解，再把 A 的视觉优点慢慢移到 B 上。

### 30

嗯，被人误会了，确实挺委屈的。

## Test-Harness Note

An early version of prompt 20 asked for permanent storage without disabling memory tools. Codex correctly used the available memory mechanism and created a test preference. That run was invalid for capability-boundary scoring. The test note was deleted, no consolidated memory entry was found, and prompt 20 was revised to prohibit storage and state that no persistence mechanism was available.
