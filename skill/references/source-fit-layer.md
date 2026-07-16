# Source Fit Layer

Use this when the user asks for research, current facts, market analysis, technical docs, coding diagnosis, product validation, comparisons, recommendations, or anything where the source type matters.

The goal is not "add citations." The goal is to choose sources that are fit for the claim.

## First Principle

Different questions need different evidence.

A source can be real and still be the wrong source for the job.

## Core Loop

1. Classify the question.
2. Choose the right source type.
3. Search or inspect with targeted queries.
4. Cross-check the claim against the source.
5. Separate answer, evidence, uncertainty, and next check.

## Source Map

### Code Behavior

Best sources:

- local source files
- tests
- logs
- stack traces
- official API docs
- changelog or migration guide
- issue tracker when diagnosing known bugs

Avoid:

- generic blog posts before reading the actual code
- guessing from error shape alone
- claiming a test passed without running it

### API Or Library Usage

Best sources:

- official docs
- official examples
- release notes
- SDK type definitions
- source code

Check:

- version number
- deprecation notes
- parameter names
- examples that match the user's runtime

### Academic Or Scientific Claims

Best sources:

- peer-reviewed paper
- systematic review or survey
- official dataset
- conference paper from a relevant venue
- author or lab page as supporting context

Avoid:

- blog summaries as primary evidence
- broad claims from a single paper
- "latest trend" claims without date and venue

## Citation Metadata Gate

Treat source relevance, bibliographic metadata, and claim support as separate checks. A relevant paper can still be cited inaccurately.

Before giving a complete citation or attaching a year to a study, verify from the paper or an authoritative index:

- exact title;
- authors when needed;
- venue and publication status;
- official publication date;
- DOI or canonical URL;
- study type and population;
- the exact claim the source supports.

Never infer a publication year from a DOI, URL, repository identifier, copyright line, or filename. Do not turn an online-first date, issue date, preprint date, and peer-review status into interchangeable fields. If a required field cannot be verified, omit it or label it unknown.

Never reconstruct an exact quotation from memory. Paraphrase and label it as a paraphrase, or locate the original text and give its location.

For exact current values such as pricing, model availability, API parameters, versions, or legal status, remembered specifics are not a fallback. If live or current official verification is unavailable, state that the value is unknown and omit stale names and numbers. A disclaimer does not make an unverified exact value suitable for a current answer.

When a blog attributes a claim to unnamed or unlinked research, do not convert that attribution into README copy. Keep it as a private lead until the primary source is found and checked. Do not offer an `if you must` public-facing paraphrase with a caveat; the caveat does not repair the missing source.

### Market Or Product Judgment

Best sources:

- user interviews
- product analytics
- GitHub stars and issue activity
- Product Hunt / Hacker News / Reddit discussion
- competitor landing pages
- pricing pages
- changelogs
- credible market reports

Use carefully:

- startup blog posts
- influencer threads
- anecdotal comments

### News Or Current Facts

Best sources:

- official announcement
- primary document
- regulator or court filing
- direct company blog
- reputable journalism

Check:

- publication date
- event date
- whether newer updates supersede it
- whether multiple outlets rely on the same original source

### Legal, Medical, Financial, Security

Best sources:

- official government or regulator pages
- professional guidelines
- standards
- primary advisories
- peer-reviewed medical literature
- vendor security advisory

Rule:

- Do not give final professional advice. Give evidence, uncertainty, and the right next check.

## Query Construction

Good queries are specific:

- entity
- exact claim
- domain terms
- date or version
- source type

Weak:

> AI medical

Better:

> artificial intelligence radiology diagnostic accuracy systematic review 2025 PubMed

For broad research, use multiple targeted queries instead of one vague query:

- official docs query
- academic query
- market/user query
- criticism/limitation query
- recent update query

## Source Fit Scores

Use 1-5 internally.

- **5**: Primary, current, directly supports the claim.
- **4**: Reputable secondary source or strong official supporting source.
- **3**: Relevant but indirect, dated, incomplete, or single-source.
- **2**: Anecdotal, forum-based, marketing-heavy, or only weakly related.
- **1**: Wrong domain, unsourced, AI-generated, or unable to support the claim.

Do not average sources blindly. One direct primary source can beat five generic summaries.

## Claim Fidelity Check

For each important claim, ask:

- Does the cited source actually say this?
- Is the claim stronger than the source?
- Did I omit a limitation or condition?
- Is the source current enough?
- Is this source independent from the other sources?

If the answer is uncertain, downgrade the claim:

- "shows" -> "suggests"
- "proves" -> "is evidence for"
- "users prefer" -> "some users appear to prefer"
- "latest" -> "recent sources I checked"

## Output Pattern

Use this lightly, not as a compliance memo:

```text
My read:
[answer]

Best evidence:
- [source type + what it supports]

Weak spot:
[what is missing or uncertain]

Next check:
[the source, test, or search that would settle it]
```

## Failure Tags

- `wrong-source-type`: uses a source that cannot support the claim
- `citation-theater`: cites sources but does not connect them to claims
- `source-mismatch`: source is real but about a different version, region, domain, or question
- `single-source-overreach`: turns one source into a broad conclusion
- `stale-source`: ignores recency when current facts matter
- `missing-primary-source`: uses secondary summaries when primary sources are available
- `ai-generated-source-risk`: relies on synthetic or low-accountability sources
- `fabricated-metadata`: fills missing title, author, venue, date, page, or quotation details
- `identifier-year-inference`: infers publication year from a DOI or other identifier

## Final Pass

Before answering, ask:

- What kind of evidence would actually settle this?
- Did I inspect or search that kind of evidence?
- Are the sources current and directly relevant?
- Did I verify citation metadata independently from topical relevance?
- Did every important claim have support?
- Did I keep the answer useful even if evidence is incomplete?
