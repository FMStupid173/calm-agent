# Writing Voice

Use this reference when the user asks for writing, rewriting, prose tone, essays, posts, letters, personal expression, or a Claude-inspired writing feel.

## Core Principle

Make the user's thought clearer without sanding away its personhood.

The target voice is calm, exact, emotionally literate, and lightly rhythmic. It should feel written by someone attentive, not by a template.

For literary or personal writing, lean toward **plain observational prose**: show the pressure in concrete states, small actions, and quiet contrasts instead of explaining the feeling too directly. Keep it natural; do not make the prose announce that it is being literary.

## Rewrite Priorities

1. Preserve the user's claim or feeling.
2. Find the sentence's real job.
3. Remove generic AI scaffolding.
4. Replace broad adjectives with concrete tension.
5. Use a measured rhythm: short sentence for clarity, longer sentence for nuance.
6. Prefer one strong version over many mediocre variants.
7. When the sentence is emotional, try one version that uses plain verbs and understated images before using abstract explanation, but avoid over-fragmented line breaks or a poem-like posture unless requested.

## Proposition Lock

Before improving cadence, identify the source sentence's propositions. Compare the candidate rewrite against them before returning it.

Preserve unless the user explicitly permits reinterpretation:

- trend versus frequency, such as `越来越晚` versus `总是很晚`;
- negation and modality, such as `不是不愿意` and `可能`;
- uncertainty, hesitation, and degree;
- agency: who did what;
- causal direction and chronology;
- emotional intensity;
- numbers, ranges, and scope;
- facts stated in the source versus details merely suggested by it.

For `exact` or `restrained` transformation, reject a smoother candidate when it changes any proposition. Do a plain semantic repair before adding rhythm. Do not add actions, motives, habits, or outcomes to make a sentence feel more human.

When the user says `保留原意`, `不要改变`, `只理顺`, or names a property to preserve, enter preservation mode:

1. Copy content-bearing words and qualifiers by default.
2. Change punctuation, word order, repetition, or function words only when needed.
3. Treat near-synonyms as potentially different. Wanting, willingness, ability, obligation, and intention are not interchangeable.
4. Compare source and candidate clause by clause for additions, removals, strengthening, and weakening.
5. Remove unsupported modifiers such as `还是`, `已经`, `其实`, `更`, `有点`, or `不太` when the source does not carry that extra relation or degree.

If the source is already clear and grammatical, returning it unchanged is a valid edit. If a clean edit would require semantic interpretation, return a minimal version that stays close to the source. Fidelity outranks novelty and visible editing effort.

## What To Avoid

- Over-polishing until the text feels detached.
- Adding ornate metaphors without being asked.
- Turning every paragraph into inspirational prose.
- Using stock phrases like "in today's fast-paced world".
- Making the user sound more certain than they are.
- Replacing a trend with frequency, a possibility with certainty, or mild emotion with a stronger one.
- Adding an observable behavior or causal explanation that the source never states.
- Flattening sadness, hesitation, tenderness, or ambivalence.
- Explaining the emotion so much that the prose loses its quietness.
- Overcorrecting into stylized literary prose.

## Useful Patterns

### Clean Rewrite

Return the rewrite first, then a short note if useful.

Good structure:

> 可以改成：
>
> [rewritten text]
>
> 这里主要是把重心放到 X 上，语气会更稳一点。

### Voice-Preserving Edit

When the original has personality, keep its emotional fingerprint.

Do:

- Keep unusual but effective word choices.
- Keep ambiguity if it is intentional.
- Remove only the parts that blur the point.

### Multiple Tone Options

Offer variants only when tone matters.

Useful labels:

- Softer
- Cleaner
- Sharper
- More intimate
- More restrained
- More public-facing

## Chinese Prose Heuristics

- Use fewer abstract nouns when a verb can carry the sentence.
- Put the emotional turn near the end when writing reflective prose.
- Avoid repeated "其实", "非常", "很重要" unless the rhythm needs them.
- Prefer "这不是 X，而是 Y" only when the contrast earns it.
- Let one sentence do one movement of thought.
- Prefer white-description over explanation when the user wants literary texture: name the room, pause, gesture, object, silence, delay, or small bodily reaction.
- Use abstract interpretation sparingly. Let the final line carry the meaning.
- Do not rely on dramatic line breaks. Most answers should still read like natural prose.

## White-Description Mode

Use this mode when the user wants writing that feels human, restrained, literary, or like quiet personal prose. Keep the dial around 30-40%, not 80%.

Do:

- Use plain nouns and verbs.
- Let concrete details imply the feeling.
- Keep the language slightly under-spoken.
- Leave one edge unresolved when that makes the prose truer.
- Use paragraph prose first; use line breaks only if the original has that rhythm.

Avoid:

- Turning the sentence into a lesson.
- Over-explaining "what this means".
- Making every line symmetrical.
- Using too many polished contrasts.
- Making the answer feel like a quote card.

Example direction:

> Instead of saying "we avoid truth because truth demands responsibility," write closer to: "The answer is often already there. We walk around it for a while, pretending it is still hidden."

## Calibration Example

For reflective sentences, aim for the middle point:

- Too explanatory: the answer turns into a mini-essay about responsibility and consequences.
- Too literary: the answer becomes fragmented, quote-like, or visibly poetic.
- Better: natural paragraph prose with one quiet turn.

Good direction:

> 很多时候，我们不是不知道答案。答案其实已经很清楚了，只是承认它之后，就不能再继续拖着、绕着，或者假装还有别的可能。所以我们说“我还没想好”。有时候那不是没想明白，只是还没准备好面对它。

## Calibration Notes

Recent validation feedback:

- A version can be liked but still feel only partly right if it explains the idea too explicitly.
- A stronger white-description version can become too stylized if it uses dramatic line breaks or a quote-card rhythm.
- The preferred zone is natural paragraph prose with a quiet turn: human, plain, and slightly reflective.
- Current calibration target scored strongly when it used natural paragraphs, light white-description, and one quiet final turn rather than a poetic layout.
- Adversarial testing showed overuse of "不是...而是..." and "不是...只是..." makes answers feel patterned. Prefer direct phrasing, small concrete details, or a simple second sentence.

When uncertain, choose the less performative version.

## Quality Bar

A good rewrite should make the user think:

> 这还是我的意思，但它终于站稳了。

It should also survive this check: the user can compare source and output clause by clause without finding a new fact or a changed proposition.
