# Scheduling

Leitner boxes: simple spaced repetition. Each chunk has one box, 0–4.

## Frontmatter fields

```yaml
box: 0            # 0 = new, never passed a re-derive
next_review: 2026-07-10   # ISO date; meaningless while box is 0
streak: 0         # consecutive fully-correct reviews at current box
weak: ["Q2: confuses retrieval direction"]   # missed id + one-line diagnosis, no commas
last_reviewed: null
created: 2026-07-10
```

## Intervals

After a fully-correct review at box b, the chunk moves to box b+1 (cap 4)
and `next_review` = today + interval of the NEW box:

| Box | Interval |
|---|---|
| 1 | +1 day |
| 2 | +3 days |
| 3 | +7 days |
| 4 | +21 days (repeats at +21) |

## Grading anchors

Grade each question on the **first unaided attempt**. Nothing after a
reveal or repair changes today's grade — a failed retrieval followed by
recognizing the answer is still a miss.

- **correct** — independent recall/explanation, at most minor omissions
- **partial** — needed a scaffold, or a load-bearing gap remains
- **miss** — no meaningful recall, or a central misconception

**Grade meaning, never wording.** The note's sentence is an answer key
for the concept, not a target string. **Substitution test**: used as a
rule, would the learner's wording make the same call as the note's on a
novel case? Same call → correct, even with zero shared words ("can't be
modified without reading other code" ≡ "in isolation"). Different call →
the case they'd get wrong is the gap; name that case, not the missing
words.

## Transitions

Chunk-level outcome = worst question grade in that review.

- New chunk passes its first re-derive (new-chunk protocol step 3) →
  `box: 1`, `next_review: today+1`.
- New chunk, boundary probe fluent through all questions (nothing to
  teach) → `box: 2`, `next_review: today+3` — already-known material
  skips the new-chunk pipeline instead of being ground through it.
- All correct → `streak` +1, then box +1 (cap 4) —
  **except 3→4, which requires `streak ≥ 2`**: two consecutive clean
  reviews, because a single pass can be luck or a familiar phrasing.
  Interval per table. Move resolved `weak` entries into the chunk's
  `## Misconception log` with today's date and the retest result — do NOT
  delete them; a misconception that happened once predicts future errors.
  Check `- [x]` any question answered correctly from memory for the first
  time.
- Worst grade partial → box unchanged, `streak: 0`,
  `next_review: today+1`, diagnosis appended to `weak`. No demotion — a
  scaffolded success is progress, not failure.
- Any miss → `box: 1`, `streak: 0`, `next_review: today+1`, append
  to `weak` as `"Qn: <one-line diagnosis>"` — what specifically broke
  ("confuses X with Y", "forgets the base case"), not just the id. Next
  session's scaffolding question is built from this line, so the
  diagnosis must name a broken distinction or misclassified case
  ("conflates absent info with hard-to-read info") — never missing
  wording ("didn't say obvious" fails the substitution test). Keep it
  under ~8 words and comma-free. Boxes fall hard on a true miss on
  purpose — relearning is cheaper than false confidence.
- Always set `last_reviewed: today`.

## Session composition

1. `scripts/due.py` orders due chunks by (box asc, next_review asc) — that
   ordering IS "hardest first".
2. If more than ~6 chunks are due, take the 6 hardest and tell the learner
   the rest are deferred to tomorrow — an overlong session beats retention
   out of itself.
3. New chunks come only after due items are handled, max
   `settings.new_per_session` (default 4).
4. Interleave: with ≥2 chunks active, alternate questions between them
   round-robin. With ≥2 sources due, alternate sources too.
5. A chunk is "handled" this session when its due questions were each asked
   once (plus re-asks of misses). Do not run a chunk to exhaustion.

## Pipeline refill

Generating a chunk file flips its map row `planned` → `ready`
(mechanics in `references/chunk-writing.md`). Two boundaries keep each
source's box-0 pool stocked:

- **Close (primary)** — Study step 9: box-0 pool below
  `new_per_session` with `planned` rows left → generate until the pool
  reaches `new_per_session`. A session is closed only once next
  session's new material exists.
- **Session start (guard)** — due.py reporting fewer box-0 chunks than
  `new_per_session` while `planned` rows remain means a Close refill
  was missed: refill before proceeding. Rare by design.

## due.py

```
python scripts/due.py <vault-path> [--date YYYY-MM-DD]
```

Read-only. Prints due chunks (hardest first, with overdue days and weak
ids), new chunks, the next upcoming review date, and totals. The `--date`
flag exists for testing and for "what's due tomorrow" questions.
