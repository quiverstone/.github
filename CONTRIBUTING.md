# Contributing to Quiverstone projects

Thanks for helping out! These guidelines apply to every public repository in the
[Quiverstone organization](https://github.com/quiverstone) unless a repository has its own `CONTRIBUTING.md`.

## Before you start

- **Check the repository's own guide first.** [armory](https://github.com/quiverstone/armory) has its own
  `CONTRIBUTING.md` and a CloudFormation standard enforced in CI, and [docs](https://github.com/quiverstone/docs)
  publishes `main` automatically, so every change there needs a pull request.

- **Bugs and small fixes** — open a pull request directly, or an issue first if you'd like a second opinion.
- **New features or bigger changes** — open an issue to discuss the approach before you write a lot of code.
- **Platform ideas** — share them on [our roadmap board](https://quiverstone.canny.io/changelog).
- **Security problems** — follow [SECURITY.md](SECURITY.md) instead of opening an issue.

## Making a change

1. Fork the repository and create a branch from the default branch.
2. Keep each pull request focused on one change.
3. Follow the existing style and run the repository's linters and tests.
4. Update documentation and examples affected by your change.
5. Open a pull request and fill in the template.

### AWS-specific expectations

- **Least privilege.** IAM policies, roles, and SCPs should grant only what's needed. Explain any wildcard.
- **No secrets, ever.** Never commit credentials, account IDs, External IDs, or customer names — use
  placeholders like `111111111111` and `example-org`.
- **Partition aware.** Prefer `${AWS::Partition}` / `data.aws_partition` over hard-coded `arn:aws:` so
  templates work in GovCloud.
- **Safe defaults.** Anything that deletes, detaches, or changes access should be opt-in and clearly documented.

## Commit messages

We like [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, `chore:`),
but a clear, descriptive message is what matters most.

## Code of conduct

Everyone participating is expected to follow our [Code of Conduct](CODE_OF_CONDUCT.md).
