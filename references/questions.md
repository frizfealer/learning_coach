# Question design

Questions are the primary artifact of this skill — notes exist to answer
them, not the reverse. Write 3–6 per chunk, at least one per level.

## The ladder

| Level | Tag | What it tests | Shape |
|---|---|---|---|
| Recall | `<!-- R -->` | Can they retrieve the mechanism/definition unaided | "What is… / How does… / Why does…" |
| Apply | `<!-- A -->` | Can they use it on a concrete case not in the text | Small worked problem, prediction, or debugging scenario |
| Transfer | `<!-- T -->` | Can they connect it across domains or chunks | "How is this like X in <their domain>? / What breaks if…?" |

At first exposure the ladder doubles as a boundary probe (Vygotsky's zone
of proximal development): ask up the rungs, stop at the first break in
fluency, teach from that rung. Order the stored questions accordingly —
easiest recall first, transfer last.

## Rules

1. Answerable from this chunk plus earlier chunks only — no forward
   references, no outside trivia.
2. The question must not embed its own answer ("Why does dropout prevent
   overfitting by randomly zeroing units?" is self-answering — cut the
   clause).
3. Prefer "why/how" over "what is" for recall where the source supports it —
   mechanism recall builds understanding, the glue of chunks. Never ask
   "define X in one sentence" — that makes the note's wording the answer
   key. Ask instead for a minimal pair ("which of these two snippets is
   dependency, which is obscurity, and what test did you apply?") or the
   test itself ("what would you check in a piece of code to decide whether
   X is present?"). Any wording that passes the substitution test is a
   full answer.
4. Apply questions should be small enough to attempt in chat, big enough that
   pattern-matching the note text does not solve them.
5. Transfer questions may reference the learner's strong domains from
   `vault.json` — this doubles as analogy reinforcement.
6. Number `Q1…Qn`; keep the level tag as an HTML comment so Obsidian renders
   clean.

## Example (chunk: backpropagation)

```markdown
## Questions
- [ ] Q1: Why does backprop compute gradients backward from the loss rather
      than forward from the inputs? <!-- R -->
- [ ] Q2: A 3-layer net trains fine, but gradients in layer 1 are ~1e-9 while
      layer 3 looks healthy. Walk through what backprop is doing that could
      cause this, and name one fix. <!-- A -->
- [ ] Q3: Backprop caches forward activations to reuse during the backward
      pass. What's the analogous trade-off in dynamic programming, and when
      would you refuse to pay the memory cost in each? <!-- T -->
```

Q1 forces the chain-rule-efficiency argument, not a definition. Q2 cannot be
answered by quoting the note. Q3 anchors to a domain the learner already
holds.
