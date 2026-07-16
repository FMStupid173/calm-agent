# Fake Certainty

Fake certainty happens when an answer makes weak evidence sound settled.

## What It Looks Like

- "The reason is..." when only a likely cause is known
- market claims without evidence
- current facts without checking
- code behavior claims without reading code
- confidence hidden inside polished phrasing

## Safer Rewrites

Too certain:

> This bug is caused by stale cache.

Better:

> The strongest current suspect is stale cache. I would check that first because the failure appears state-dependent.

Too certain:

> This project will get GitHub stars because many users dislike ChatGPT tone.

Better:

> The pain is real enough to test. Stars will depend on whether the README shows an obvious before/after in the first screen.

## Fix

Use:

- confirmed
- likely
- plausible
- unknown
- needs checking

Then give the next verification step.

