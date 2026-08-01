# Writing chunk files

Two callers use this recipe: Ingest step 3, for the first ~2 sessions'
worth of rows, and Study's refill step (skeleton step 9) for every batch
after that. The rules are identical either way.

## Resolving and reading the source

Whenever chunk files are generated after the initial ingest — normally by
Study's refill step, or if the learner explicitly re-invokes ingest — read
`source_path` from `source.md` and deep-read from there; the learner never
re-specifies the file. The chunk map's Status column is the record of
progress: `ready` rows have files, and the frontier is the first `planned`
row. If `source_path` is missing or stale (inline-pasted text, moved file),
ask the learner for the material and write the new path in.

Deep-read only the section containing the rows being generated — not the
whole source.

## Inside each file

Order matters: **questions first** (read `references/questions.md` for the
recall→apply→transfer ladder), then notes (≤8 compressed numbered points),
then one backup analogy anchored in the learner's strong domains (delivery
rules: new-chunk protocol step 4). Use `assets/chunk-template.md` for the
file shape.

Record a `source_ref` (chapter / page range / section / figure) in each
chunk's frontmatter, so a miss can point back to exactly what to re-read.

A chunk with a `Fwd` entry may mention it in its notes in at most one line
("connects to <later topic> — deferred"); its questions must stay
answerable without the later material.

## After the batch is written

Flip the generated rows from `planned` to `ready` in the chunk map.

**Fwd back-links.** For each newly generated chunk NN, scan the chunk map's
`Fwd` column for rows listing NN. For each such row MM, add one
transfer-rung question to chunk NN's `## Questions` — "connect this back to
<concept>", naming row MM's chunk by its title — phrased so the learner
builds the connection, not told it. (Open seeds tagged `(→ chunk NN)` are
already handled by the learner-questions routing in SKILL.md; leave that as
is.)
