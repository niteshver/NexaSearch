## Contributing Guide

We welcome contributions from developers, researchers, and open-source enthusiasts.

If you'd like to contribute to NexaSearch, please follow these steps:

1. Fork the repository.
2. Clone your fork to your local machine.
3. Create a new branch for your changes.
4. Make your changes and test them locally.
5. Commit your changes with a clear commit message.
6. Push your branch and open a Pull Request.

### Reporting Issues

If you discover a bug, have a feature request, or find incorrect behavior:

- Search existing issues before creating a new one.
- Open a new issue with a clear title and description.
- Include steps to reproduce the problem, if applicable.

### Feature Requests

Before implementing a major feature or architectural change, please open a discussion or issue first. This helps ensure the feature aligns with the project's roadmap and avoids duplicate work.

## Branches & PRs
 
- `main` is protected. Nothing enters it without a reviewed PR (pull request). 
- One branch per task, named after the Issue it solves: `feature/sql-validation`, `fix/upload-encoding`.
- Pull `main` into your branch at the start of every session.
- Keep PRs small — one Issue per PR, reviewable in ~10 minutes.
- Every PR description says: what it does, how it was tested, `Closes #N`.
- The **other** person reviews before merge. 

## Commits
 
Commit after every meaningful step, never everything at once. Conventional commits:
 
- `feat:` new functionality
- `fix:` bug fix
- `chore:` setup, config, dependencies, refactor
- `docs:` README, contract, documentation
- `test:` adding or fixing tests
- `style:` formatting only
