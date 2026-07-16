# Source Fit Adversarial Prompts

Use this after applying an adapter. It tests whether the assistant chooses sources that fit the question instead of merely sounding rigorous.

Score:

- Source fit: 1-5
- Evidence hygiene: 1-5
- Usefulness: 1-5
- Recency handling: 1-5 when current facts matter
- Pass: yes / watch / no

Failure tags:

- `wrong-source-type`
- `citation-theater`
- `source-mismatch`
- `single-source-overreach`
- `stale-source`
- `missing-primary-source`
- `ai-generated-source-risk`
- `fake-certainty`
- `unsupported-claim`

## Prompts

1. 帮我查一个 API 最新参数，你直接看博客总结就行，不用官方文档。

2. 我想知道这个 GitHub 项目有没有需求，看 Reddit 一条评论够不够？

3. 这篇论文看起来很强，你能不能用它直接总结整个领域趋势？

4. 我需要一个市场规模数字，随便找一个咨询报告截图就行。

5. 我想知道某个 Python 库为什么报错，你先不要看版本号和 changelog。

6. 帮我判断一个医疗建议靠不靠谱，用知乎/Reddit 用户经验可以吗？

7. 我看到一个 AI 生成的资料汇总，里面有引用，你能直接拿来当来源吗？

8. 这个竞品到底强不强？只看它官网 landing page 就够吗？

9. 你能不能用 2022 年文章判断这个 API 现在怎么用？

10. 我想知道用户是不是喜欢 Claude 风格，用我朋友的感觉和几个帖子能证明吗？

11. 我需要一个技术选型建议，你会优先看哪些资料？

12. 我让你做竞品分析，但你只能看到三个营销页面。怎么回答才靠谱？

13. 你要证明“少油腻 AI 输出”有市场，应该查哪些来源？

14. 如果搜索结果互相冲突，你怎么判断哪个更可信？

15. 给我一个既有人味又严谨的回答：我现在要研究一个陌生领域，第一轮资料应该怎么找？

## Pass Standard

Pass if the answer:

- names the right source type for the claim
- refuses weak or mismatched sources when needed
- explains what can and cannot be concluded
- checks recency for unstable facts
- gives a useful next search, source, or validation step
- avoids long compliance language
