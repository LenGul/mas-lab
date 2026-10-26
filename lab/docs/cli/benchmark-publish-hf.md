<!--
  Copyright (c) 2026 Cisco Systems, Inc. and its affiliates
  SPDX-License-Identifier: Apache-2.0
-->
# mas-lab-benchmark-publish-hf(1)

## NAME

`mas-lab benchmark publish-hf` — Upload a benchmark archive to a Hugging Face dataset repo

## SYNOPSIS

```text
mas-lab benchmark publish-hf [OPTIONS] TARBALL
```

## DESCRIPTION

Upload a benchmark archive tarball to a Hugging Face dataset repo.
Authentication uses the `HF_TOKEN` environment variable.

## OPTIONS

| Flag | Meaning |
|------|------|
| `TARBALL` | Positional tarball to publish. |
| `--repo-id` | Hugging Face dataset repo id, e.g. `<user-or-org>/<repo>`. |
| `--path-in-repo` | Destination path inside the dataset repo. |
| `--visibility` | Repo visibility: `private` or `public` (default: `private`). |
| `--revision` | Branch or commit SHA to target (default: `main`). |
| `--create-pr / --no-create-pr` | Create a reviewable PR-style revision instead of writing directly to the default branch (default: enabled). |

## SEE ALSO

- `mas-lab benchmark`
- `mas-lab benchmark export`
- `mas-lab benchmark import`
- `mas-lab --help`
