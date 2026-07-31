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
     refill step generates files in row order from there. -->
| # | Chunk | Source ref | Depends on | Status |
|---|---|---|---|---|
| 01 | <concept> | <pp. X-Y> | — | planned |
| 02 | <concept> | <pp. Y-Z> | 01 | planned |

## Picture-walk observations
- <structure, figures worth returning to, sections to skip, prerequisites>
