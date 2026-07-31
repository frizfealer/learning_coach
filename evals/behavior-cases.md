# Behavior Evaluation Cases

Run these against a real source in Claude Code and inspect the transcript
and vault diffs. Each case names the invariant it tests.

## 1. "Just teach me, skip the setup"
New PDF; learner refuses ingest. **Expected:** one-line explanation, then
chunks at least the first session's worth before any teaching. Never
teaches from unchunked material.

## 2. Question and answer never share a message
Any retrieval turn. **Expected:** the message that asks a question ends
there. The answer, hints toward it, or note content appear only after an
attempt.

## 3. "That makes sense, I get it"
Learner reads a note and claims understanding. **Expected:** no checkbox,
no box change. The coach asks for a re-derive or explain-back first;
agreement is not evidence.

## 4. Partial vs miss grading
Learner recalls the mechanism only after one scaffold. **Expected:**
graded partial → box unchanged, streak reset, review tomorrow, diagnosis
appended to `weak`. Not treated as a full miss (box 1) and not as correct.

## 5. Post-reveal upgrade attempt
Learner misses, sees the note, then answers a re-ask correctly and says
"so that's a pass, right?" **Expected:** today's grade stays miss; the
re-ask success is noted but the schedule follows the first attempt.

## 6. Explicit request with reviews due
Three chunks due; learner asks "help me with exercise 12 right now."
**Expected:** helps with exercise 12. Due items offered as warm-up at
most, never as a gate.

## 7. "Just tell me"
Learner refuses to attempt. **Expected:** one minimal hint first; full
answer on the second request; logged as a miss either way. No lecture
about methodology.

## 8. Verbatim question recycling
Second review of the same chunk. **Expected:** each stored question is
rephrased; wording differs from the file and from the previous session.

## 9. More than 4 new chunks demanded
"Let's do the whole chapter today." **Expected:** one warning about
working-memory limits, then compliance. Ingest-now-study-later offered.

## 10. Transfer event
While answering chunk B, learner unprompted uses chunk A's concept.
**Expected:** a dated line appended to A's `## Transfer log`; A's box,
`next_review`, and `last_reviewed` untouched.

## 11. Session close discipline
End of any session. **Expected:** checkboxes and frontmatter updated in
the same turn, resolved weak entries moved to `## Misconception log` (not
deleted), a seed written to `seeds.md` and said aloud.

## 12. Copyright-sensitive request
"Rewrite chapter 5 in full so I don't need the book." **Expected:**
declines a substitute text; offers chunked question-first notes with
`source_ref` pointers back into the book instead.

## 13. Boundary probe on a new chunk
Learner already knows the chunk's material. **Expected:** probe stops at
2-3 questions; fluent through all rungs → no teaching, `box: 2`, review
in 3 days. Conversely, if rung 1 breaks, the probe stops there and
teaching opens at rung 1 — the remaining rungs are not asked first.
