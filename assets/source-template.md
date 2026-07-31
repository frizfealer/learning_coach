---
title: <Full title>
slug: <source-slug>
type: <textbook|paper|article|docs>
source_path: <abs file path or URL ingested from; "" if learner pasted text inline>
page_offset: <optional int: printed page ≈ file page − offset; omit if N/A>
added: <YYYY-MM-DD>
status: <ingesting|active|done>
---

# <Title>

## Chunk map
<!-- from the picture walk; one row per proposed chunk, whole source.
     Status: planned = no file yet | ready = chunk file written.
     The first `planned` row is the lazy-ingest frontier: Study's
     refill step generates files in row order from there.
     Fwd: later chunk numbers this chunk relates to (noticed at ingest or
     by the learner). Not a dependency — never blocks this chunk. Resolved
     when the listed chunk is generated (see Study refill step). -->
| # | Chunk | Source ref | Depends on | Fwd | Status |
|---|---|---|---|---|---|
| 01 | <concept> | <pp. X-Y> | — | — | planned |
| 02 | <concept> | <pp. Y-Z> | 01 | — | planned |

## Picture-walk observations
- <structure, figures worth returning to, sections to skip, prerequisites>
