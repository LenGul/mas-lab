#  Copyright (c) 2026 Cisco Systems, Inc. and its affiliates
#  SPDX-License-Identifier: Apache-2.0
"""``mas-lab benchmark publish-hf`` command."""

from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import click


@click.command("publish-hf")
@click.argument("tarball", type=Path)
@click.option(
    "--repo-id",
    required=True,
    help="Hugging Face dataset repo id, e.g. <user-or-org>/<repo>.",
)
@click.option(
    "--path-in-repo",
    default=None,
    help=(
        "Destination path inside the HF dataset repo. "
        "Defaults to benchmarks/<experiment>/<short_id>/bundle.tar.gz "
        "based on the archive manifest."
    ),
)
@click.option(
    "--visibility",
    type=click.Choice(["private", "public"], case_sensitive=False),
    default="private",
    show_default=True,
    help="Repo visibility to create on Hugging Face. Default is private review-based publishing.",
)
@click.option(
    "--revision",
    default="main",
    show_default=True,
    help=(
        "Branch or commit SHA to target for the upload; when --create-pr is set "
        "it creates a reviewable revision from this base."
    ),
)
@click.option(
    "--create-pr/--no-create-pr",
    default=True,
    show_default=True,
    help="Create a review-based revision rather than pushing directly to the default branch.",
)
def publish_hf_cmd(
    tarball: Path,
    repo_id: str,
    path_in_repo: str | None,
    visibility: str,
    revision: str,
    create_pr: bool,
) -> None:
    """Upload a benchmark archive tarball to a Hugging Face dataset repo.

    Authentication uses the ``HF_TOKEN`` environment variable.
    """
    from mas.lab.benchmark.cli.export_import import publish_hf_command

    args = SimpleNamespace(
        tarball=tarball,
        repo_id=repo_id,
        path_in_repo=path_in_repo,
        visibility=visibility,
        revision=revision,
        create_pr=create_pr,
    )
    raise SystemExit(publish_hf_command(args))
