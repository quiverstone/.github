# quiverstone/.github

Organization-wide configuration for [Quiverstone](https://www.quiverstone.io) on GitHub.

## What lives here

| Path | Purpose |
| --- | --- |
| [`profile/README.md`](profile/README.md) | The public profile shown at [github.com/quiverstone](https://github.com/quiverstone) |
| `profile/assets/` | Self-hosted stat cards, regenerated daily |
| [`scripts/generate_stats.py`](scripts/generate_stats.py) | Renders the org stat and language cards from the GitHub GraphQL API |
| [`scripts/update_blog.py`](scripts/update_blog.py) | Pulls the latest posts from the [Quiverstone blog](https://www.quiverstone.io/blog/) feed |
| [`.github/workflows/profile.yml`](.github/workflows/profile.yml) | Daily refresh of stats and blog posts |
| [`.github/workflows/lint.yml`](.github/workflows/lint.yml) | Script checks and link checking on PRs |
| [`CONTRIBUTING.md`](CONTRIBUTING.md), [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md), [`SECURITY.md`](SECURITY.md), [`SUPPORT.md`](SUPPORT.md) | Default community health files for every public repo in the org |
| [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE), [`.github/pull_request_template.md`](.github/pull_request_template.md) | Default issue forms and PR template |

Any repository in the org that doesn't define its own version of a community health file or template
inherits the one here.

## Working on the profile

```bash
# Preview stat cards with sample data (no token needed)
python scripts/generate_stats.py quiverstone --mock --out /tmp/preview

# Render with live data
GITHUB_TOKEN=$(gh auth token) python scripts/generate_stats.py quiverstone

# Refresh the blog list in profile/README.md
python scripts/update_blog.py https://www.quiverstone.io/blog/ --count 5
```

Edit anything in `profile/README.md` freely, but leave the `BLOG-POST-LIST` markers in place — the
workflow rewrites the lines between them.

> **Note:** the org profile only renders while this repository is **public**.
