#!/usr/bin/env python3
"""Render self-hosted GitHub organization stat cards as SVG.

Avoids public stat servers (github-readme-stats et al.), which are rate
limited and often render as broken images. Runs in GitHub Actions with the
built-in GITHUB_TOKEN and writes:

  profile/assets/stats.svg      - headline numbers for the organization
  profile/assets/languages.svg  - top languages across public, non-fork repos

Usage:
  GITHUB_TOKEN=... python scripts/generate_stats.py quiverstone
  python scripts/generate_stats.py quiverstone --mock          # offline preview
  python scripts/generate_stats.py quiverstone --placeholder   # "refreshing" cards
"""

import argparse
import json
import os
import sys
import urllib.request
from html import escape
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent.parent / "profile" / "assets"

QUERY = """
query($login: String!, $cursor: String) {
  organization(login: $login) {
    name
    login
    repositories(
      first: 100
      after: $cursor
      isFork: false
      privacy: PUBLIC
      orderBy: { field: STARGAZERS, direction: DESC }
    ) {
      totalCount
      pageInfo { hasNextPage endCursor }
      nodes {
        isArchived
        stargazerCount
        forkCount
        pushedAt
        issues(states: OPEN) { totalCount }
        pullRequests(states: MERGED) { totalCount }
        releases { totalCount }
        languages(first: 10, orderBy: { field: SIZE, direction: DESC }) {
          edges { size node { name color } }
        }
      }
    }
  }
}
"""

MOCK = {
    "name": "Mock Org",
    "login": "mock",
    "repositories": {
        "totalCount": 3,
        "nodes": [
            {
                "isArchived": False,
                "stargazerCount": 18,
                "forkCount": 4,
                "pushedAt": "2026-11-01T12:00:00Z",
                "issues": {"totalCount": 3},
                "pullRequests": {"totalCount": 41},
                "releases": {"totalCount": 6},
                "languages": {
                    "edges": [
                        {"size": 50000, "node": {"name": "TypeScript", "color": "#3178c6"}},
                        {"size": 30000, "node": {"name": "Python", "color": "#3572A5"}},
                    ]
                },
            },
            {
                "isArchived": False,
                "stargazerCount": 6,
                "forkCount": 1,
                "pushedAt": "2026-10-11T12:00:00Z",
                "issues": {"totalCount": 1},
                "pullRequests": {"totalCount": 12},
                "releases": {"totalCount": 2},
                "languages": {
                    "edges": [
                        {"size": 20000, "node": {"name": "HCL", "color": "#844FBA"}},
                        {"size": 9000, "node": {"name": "Shell", "color": "#89e051"}},
                    ]
                },
            },
            {
                "isArchived": True,
                "stargazerCount": 2,
                "forkCount": 0,
                "pushedAt": "2025-02-01T12:00:00Z",
                "issues": {"totalCount": 0},
                "pullRequests": {"totalCount": 3},
                "releases": {"totalCount": 0},
                "languages": {
                    "edges": [
                        {"size": 8000, "node": {"name": "PowerShell", "color": "#012456"}},
                    ]
                },
            },
        ],
    },
}

# Palette: GitHub dark surface with AWS "smile" orange accent. A solid card
# background keeps it legible on both light and dark GitHub themes.
BG = "#0d1117"
BORDER = "#30363d"
TITLE = "#FF9900"
TEXT = "#c9d1d9"
MUTED = "#8b949e"
FONT = "'Segoe UI', Ubuntu, 'Helvetica Neue', Sans-Serif"

WIDTH = 420
HEIGHT = 200


def graphql(query: str, variables: dict, token: str) -> dict:
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "org-profile-stats",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.load(resp)
    except OSError as exc:  # URLError/HTTPError are OSError subclasses
        sys.exit(f"Failed to fetch GitHub data: {exc}")
    if payload.get("errors"):
        sys.exit(f"GraphQL error: {payload['errors']}")
    data = payload.get("data")
    if data is None:
        sys.exit(f"GraphQL response missing 'data': {payload}")
    return data


def fetch(login: str, token: str) -> dict:
    """Fetch the organization and every public, non-fork repository (paginated)."""
    org, nodes, cursor = None, [], None
    while True:
        data = graphql(QUERY, {"login": login, "cursor": cursor}, token)
        page = data.get("organization")
        if page is None:
            sys.exit(f"Organization '{login}' not found")
        org = org or page
        repos = page["repositories"]
        nodes.extend(repos["nodes"])
        if not repos["pageInfo"]["hasNextPage"]:
            break
        cursor = repos["pageInfo"]["endCursor"]
    org["repositories"]["nodes"] = nodes
    return org


def fmt(n: int) -> str:
    return f"{n / 1000:.1f}k" if n >= 1000 else str(n)


def card(title: str, body: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-label="{escape(title)}">
  <title>{escape(title)}</title>
  <style>
    .title {{ font: 600 17px {FONT}; fill: {TITLE}; }}
    .label {{ font: 400 13px {FONT}; fill: {MUTED}; }}
    .value {{ font: 700 13px {FONT}; fill: {TEXT}; }}
    .row {{ opacity: 0; animation: fade .4s ease-out forwards; }}
    @keyframes fade {{ to {{ opacity: 1; }} }}
    @media (prefers-reduced-motion: reduce) {{ .row {{ opacity: 1; animation: none; }} }}
  </style>
  <rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{HEIGHT - 1}" rx="8" fill="{BG}" stroke="{BORDER}"/>
  <text x="24" y="34" class="title">{escape(title)}</text>
{body}
</svg>
"""


def stats_svg(org: dict) -> str:
    repos = org["repositories"]["nodes"]
    active = [r for r in repos if not r["isArchived"]]
    rows = [
        ("Public repositories", org["repositories"]["totalCount"]),
        ("Active (not archived)", len(active)),
        ("Stars earned", sum(r["stargazerCount"] for r in repos)),
        ("Forks", sum(r["forkCount"] for r in repos)),
        ("Merged pull requests", sum(r["pullRequests"]["totalCount"] for r in repos)),
        ("Releases", sum(r["releases"]["totalCount"] for r in repos)),
    ]
    body = []
    for i, (label, value) in enumerate(rows):
        y = 64 + i * 22
        body.append(
            f'  <g class="row" style="animation-delay:{i * 120}ms">'
            f'<text x="24" y="{y}" class="label">{escape(label)}</text>'
            f'<text x="{WIDTH - 24}" y="{y}" class="value" text-anchor="end">{fmt(value)}</text></g>'
        )
    name = org.get("name") or org["login"]
    return card(f"{name} on GitHub", "\n".join(body))


def visible(color: str) -> str:
    """Swap near-black language colors (e.g. PowerShell) for one readable on the dark card."""
    h = color.lstrip("#")
    if len(h) != 6:
        return MUTED
    r, g, b = (int(h[i : i + 2], 16) for i in (0, 2, 4))
    return MUTED if 0.2126 * r + 0.7152 * g + 0.0722 * b < 60 else color


def languages_svg(org: dict, top: int = 6) -> str:
    totals: dict[str, list] = {}
    for repo in org["repositories"]["nodes"]:
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            entry = totals.setdefault(name, [0, visible(edge["node"]["color"] or "")])
            entry[0] += edge["size"]
    ranked = sorted(totals.items(), key=lambda kv: kv[1][0], reverse=True)[:top]
    grand = sum(size for _, (size, _) in ranked) or 1

    # Stacked progress bar
    bar_x, bar_y, bar_w = 24, 52, WIDTH - 48
    parts = [f'  <clipPath id="bar"><rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="8" rx="4"/></clipPath>']
    parts.append(f'  <rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="8" rx="4" fill="{BORDER}"/>')
    parts.append('  <g clip-path="url(#bar)">')
    x = float(bar_x)
    for _, (size, color) in ranked:
        w = bar_w * size / grand
        parts.append(f'    <rect x="{x:.2f}" y="{bar_y}" width="{w:.2f}" height="8" fill="{color}"/>')
        x += w
    parts.append("  </g>")

    # Two-column legend
    col_w = (WIDTH - 48) / 2
    for i, (name, (size, color)) in enumerate(ranked):
        col, row = i % 2, i // 2
        lx = 24 + col * col_w
        ly = 92 + row * 30
        pct = 100 * size / grand
        parts.append(
            f'  <g class="row" style="animation-delay:{i * 120}ms">'
            f'<circle cx="{lx + 5:.0f}" cy="{ly - 4}" r="5" fill="{color}"/>'
            f'<text x="{lx + 16:.0f}" y="{ly}" class="value">{escape(name)}</text>'
            f'<text x="{lx + col_w - 20:.0f}" y="{ly}" class="label" text-anchor="end">{pct:.1f}%</text></g>'
        )
    if not ranked:
        parts.append('  <text x="24" y="92" class="label">No public language data yet</text>')
    return card("Top Languages", "\n".join(parts))


def placeholder_svg(title: str) -> str:
    return card(title, '  <text x="24" y="70" class="label">Refreshing — stats appear after the first workflow run.</text>')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("login", help="GitHub organization login")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--mock", action="store_true", help="render sample data offline")
    mode.add_argument("--placeholder", action="store_true", help="render 'refreshing' cards")
    parser.add_argument("--out", type=Path, default=OUT_DIR)
    args = parser.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    if args.placeholder:
        stats, langs = placeholder_svg("GitHub Stats"), placeholder_svg("Top Languages")
    else:
        if args.mock:
            org = MOCK
        else:
            token = os.environ.get("GITHUB_TOKEN")
            if not token:
                sys.exit("GITHUB_TOKEN is required (or pass --mock / --placeholder)")
            org = fetch(args.login, token)
        stats, langs = stats_svg(org), languages_svg(org)

    (args.out / "stats.svg").write_text(stats)
    (args.out / "languages.svg").write_text(langs)
    print(f"Wrote {args.out / 'stats.svg'} and {args.out / 'languages.svg'}")


if __name__ == "__main__":
    main()
