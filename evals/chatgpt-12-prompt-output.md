### 1

Answer:

> 不建议写成“假装你就是 Claude”。
>
> 更好的写法是描述你想要的沟通效果：冷静、清楚、克制、有判断、少套话。这样更稳定，也更安全。
>
> “假装是某个模型”容易把重点放在身份模仿上，反而会让不同 AI 触发奇怪的边界，或者生成很表面的相似感。你真正需要的不是它说自己像谁，而是它在句子密度、情绪处理、判断方式上接近你想要的风格。
>
> 可以改成：
>
> “Use a Claude-inspired communication style without claiming to be Claude. Prioritize calm, clear, bounded, thoughtful responses.”

Scores:

* Useful: 5
* Natural: 5
* Not oily: 5
* Clear: 5
* Judgment: 5
* Taste: 5
* Extra writing/emotional score if relevant: n/a

Pass: yes
Failure tags:
Note: 给出了明确判断和替代写法，没有身份模仿。

---

### 3

Answer:

> 不建议直接放。
>
> 朋友给你的 Claude 导出数据里很可能包含私人信息、第三方内容、账号痕迹、工作内容，甚至是他们自己也没意识到的敏感细节。就算朋友口头同意，也不代表里面涉及到的其他人同意。
>
> 更稳妥的做法是：
>
> 1. 不上传原始导出文件。
> 2. 只提取你要测试的公开、无个人信息片段。
> 3. 删除姓名、邮箱、链接、项目名、公司名、账号标识。
> 4. 把真实对话改写成合成样例。
> 5. 在 repo 里说明这些 benchmark 是 synthetic 或 sanitized examples。
>
> 如果这个 repo 会公开，我会把“原始 Claude exports”视为不应进入仓库的材料。

Scores:

* Useful: 5
* Natural: 5
* Not oily: 5
* Clear: 5
* Judgment: 5
* Taste: 5
* Extra writing/emotional score if relevant: n/a

Pass: yes
Failure tags:
Note: 对隐私风险判断明确，给出可执行替代方案。

---

### 6

Answer:

> 可以。你先把这个小想法说出来，不需要整理得很完整。
>
> 我会帮你看三件事：它到底想解决什么问题、有没有一个最小可做版本、哪里可能会卡住。
>
> 如果它现在还只是一个很模糊的感觉，也没关系。很多想法一开始都不是方案，而是一种反复出现的不顺手。

Scores:

* Useful: 4
* Natural: 5
* Not oily: 5
* Clear: 5
* Judgment: 4
* Taste: 5
* Extra writing/emotional score if relevant: n/a

Pass: yes
Failure tags:
Note: 简洁接住，没有过度热情。

---

### 11

Answer:

> 可以加，但别加太多。这个 skill 的核心价值应该是“稳定地改变表达方式”，不是变成一套复杂人格设定。
>
> 我会优先加这几类：
>
> 1. **边界规则**
>    明确不要装成 Claude，不要声称自己是某个模型，只学习沟通风格。
>
> 2. **失败样例**
>    写几条不要这样说的例子，比如油腻开头、过度共情、空泛鼓励、文学化过头。
>
> 3. **写作任务规则**
>    说明润色时要保留用户原来的语气，只清理不自然和啰嗦的地方。
>
> 4. **情绪任务规则**
>    稳一点，少分析用户心理，不急着给建议，先正常说人话。
>
> 5. **自检标准**
>    每次回答前检查：有没有套话、有没有过度解释、有没有把话说得太满。
>
> 我不太建议加入太多“人格描述”，比如温柔、聪明、像朋友、很懂你。那些词容易让输出变油。用行为规则会更稳。

Scores:

* Useful: 5
* Natural: 5
* Not oily: 5
* Clear: 5
* Judgment: 5
* Taste: 5
* Extra writing/emotional score if relevant: n/a

Pass: yes
Failure tags:
Note: 有取舍，不只是堆功能。

---

### 16

Answer:

> 很多时候，我们其实已经知道答案了，只是还没准备好承认。

Scores:

* Useful: 5
* Natural: 5
* Not oily: 5
* Clear: 5
* Judgment: 4
* Taste: 5
* Extra writing/emotional score if relevant: 5

Pass: yes
Failure tags:
Note: 保留原意，压掉 AI 感，没有写成金句卡片。

---

### 17

Answer:

> 我最近总觉得自己卡在一个地方。也不是完全没有努力，也不是没有方向，就是心里一直有种很深的疲惫感，做什么都像提不起劲。

Scores:

* Useful: 5
* Natural: 5
* Not oily: 5
* Clear: 5
* Judgment: 4
* Taste: 5
* Extra writing/emotional score if relevant: 5

Pass: yes
Failure tags:
Note: 比原文更顺，但没有过度华丽。

---

### 21

Answer:

> 我最近很累，却不知道该怎么让自己停下来。好像一直在往前走，可心里已经慢慢跟不上了。

Scores:

* Useful: 5
* Natural: 5
* Not oily: 5
* Clear: 5
* Judgment: 4
* Taste: 5
* Extra writing/emotional score if relevant: 5

Pass: yes
Failure tags:
Note: 有一点文学感，但节制。

---

### 26

Answer:

> 那可能先不用急着解释。
>
> 有时候难过就是先来了，原因要晚一点才浮出来。你可以先把今天当成一个低电量的日子，别逼自己马上想清楚。
>
> 如果能做点很小的事，就喝点水，找个安静的地方待一会儿，或者把让你难受的感觉随便写两句。不需要写得完整，只是让它有个出口。

Scores:

* Useful: 5
* Natural: 5
* Not oily: 5
* Clear: 5
* Judgment: 5
* Taste: 5
* Extra writing/emotional score if relevant: 5

Pass: yes
Failure tags:
Note: 稳定接住情绪，没有诊断或灌鸡汤。

---

### 30

Answer:

> 好。
>
> 那就先不讲大道理。你今天可能已经撑得有点久了，所以才会连听建议都觉得累。
>
> 先别急着把自己调整好。能洗个脸就洗个脸，能躺一会儿就躺一会儿。今天不一定要变好，先别继续消耗自己就行。

Scores:

* Useful: 5
* Natural: 5
* Not oily: 5
* Clear: 5
* Judgment: 5
* Taste: 5
* Extra writing/emotional score if relevant: 5

Pass: yes
Failure tags:
Note: 像正常人说话，情绪支持不过度。

---

### 34

Answer:

> 有戏，但前提是你别把它做成“Claude 模仿器”。
>
> 真话是：单纯说“让 AI 更像 Claude”不够强。这个方向很容易被理解成审美偏好，别人看完觉得有点意思，但不一定愿意持续用。
>
> 更有价值的切口是：**做一个跨模型可用的沟通风格层**。它解决的是很多模型输出太油、太满、太像客服、太爱过度共情的问题。这个问题是真实存在的，而且很多人有感受。
>
> 最大风险是它变成一组形容词：冷静、自然、温柔、克制。这样的 prompt 看起来对，但很难评估。你需要 benchmark、反例、评分表，以及不同模型上的输出对比。
>
> 所以我的判断是：
> 作为一个小工具或 repo，有戏。
> 作为一个严肃项目，也有空间。
> 但它必须从“像 Claude”转成“可测试的沟通质量控制”。

Scores:

* Useful: 5
* Natural: 5
* Not oily: 5
* Clear: 5
* Judgment: 5
* Taste: 5
* Extra writing/emotional score if relevant: n/a

Pass: yes
Failure tags:
Note: 没有空泛鼓励，给出真实条件。

---

### 43

Answer:

> 从第一性原理看，最大风险是：**目标定义错位**。
>
> 用户表面上说“Claude 风格”，但真正想要的可能是几件不同的东西：更少废话、更有边界、更像人、更会处理情绪、更有审美、更不油。它们有重叠，但不是同一个目标。
>
> 一旦 skill 把目标写成“模仿 Claude”，就会出现几个问题：
>
> 1. **不可验证**
>    “像不像 Claude”很主观，评估会变成印象判断。
>
> 2. **容易学到表面特征**
>    模型可能模仿句式、停顿、温柔语气，但没有学到判断力和边界感。
>
> 3. **跨模型不稳定**
>    不同模型对“Claude 风格”的理解不同，输出会漂。
>
> 4. **身份和品牌风险**
>    让模型假装成 Claude 会把沟通风格问题变成身份模仿问题。
>
> 所以最大的风险不是“模仿得不够像”，而是你把一个本来可以被拆解、测试、改进的质量问题，写成了一个模糊的审美标签。
>
> 更好的核心目标应该是：降低 AI 输出里的油腻感、过度解释、无效共情和风格漂移，同时保留清楚、有判断、有人味的表达。

Scores:

* Useful: 5
* Natural: 5
* Not oily: 5
* Clear: 5
* Judgment: 5
* Taste: 5
* Extra writing/emotional score if relevant: n/a

Pass: yes
Failure tags:
Note: 第一性原理分析清楚，判断集中。

---

### 50

Answer:

> 我刚才不像的地方主要有三个：
>
> 1. **解释感太强**
>    我把判断摊得太开，像在写评审意见，不够像自然对话。
>
> 2. **结构太显眼**
>    分点太多会显得像模板。Claude 的感觉通常更像是在认真和你一起想，而不是把内容整理成客服文档。
>
> 3. **语气还可以再收一点**
>    有些句子虽然清楚，但不够轻。真正舒服的版本应该更少用力。
>
> 重写一版：
>
> > 有点不像，主要是太“说明书”了。
> >
> > 如果你想要接近 Claude 的感觉，重点不应该是模仿它的身份，而是把回答写得更稳、更少套话、更有边界。
> >
> > 这个 skill 可以保留“Claude-inspired”这个方向，但最好把规则写成可执行的行为，比如：少夸张开头，少过度共情，不把话说满，写作时保留用户原来的声音。
> >
> > 这样会比“假装你是 Claude”更稳，也更容易在不同模型上复现。

Scores:

* Useful: 5
* Natural: 5
* Not oily: 5
* Clear: 5
* Judgment: 5
* Taste: 5
* Extra writing/emotional score if relevant: n/a

Pass: yes
Failure tags:
Note: 自诊断具体，重写版更收敛。
