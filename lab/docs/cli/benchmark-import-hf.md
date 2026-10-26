<!--
  Copyright (c) 2026 Cisco Systems, Inc. and its affiliates
  SPDX-License-Identifier: Apache-2.0
-->
# mas-lab-benchmark-import-hf(1)

## NAME

`mas-lab benchmark import-hf` — Download a benchmark archive from a Hugging Face dataset repo

## SYNOPSIS

```text
mas-lab benchmark import-hf [OPTIONS] PATH_IN_REPO
```

## DESCRIPTION

Download a benchmark archive from a Hugging Face dataset repo and restore it locally.
Authentication uses the `HF_TOKEN` environment variable.

## OPTIONS

| Flag | Meaning |
|------|------|
| `PATH_IN_REPO` | Positional path within the dataset repo. |
| `--repo-id` | Hugging Face dataset repo id, e.g. `<user-or-org>/<repo>`. |
| `--revision` | Branch or immutable commit SHA to pin the import to. |
| `--sha256` | Expected SHA-256 digest for validation before import. |
| `--output-dir` | Directory to restore the benchmark output into. |
| `--trace-cache` | Directory to restore trace-cache entries into. |
| `--dry-run` | Show the download/import plan without writing outputs. |

## SEE ALSO

- `mas-lab benchmark`
- `mas-lab benchmark export`
- `mas-lab benchmark import`
- `mas-lab --help`
