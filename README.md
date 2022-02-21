pre-commit-exec
===============

This is a [pre-commit][] plugin which allows the execution of arbitrary
commands/scripts.  This plugin grants generic access to system commands and
repository scripts without the need to create a new repository. This is
particularly useful when a single check requires the combination of multiple
steps.

For example, in building a static website and testing the [HTML] links in the
generated website we can launch script handler, such as:
```
- repo: https://github.com/major0/pre-commit-exec
  rev: v0.1.0
  hooks:
    - id: command
      alias: link-check
      always_run: true
      name: Check site links
      args: ["sh", "scripts/link-check.sh"]
- repo: https://github.com/major0/pre-commit-exec
  rev: v0.1.0
  hooks:
    - id: command
      alias: link-check-all
      stages: [manual]
      name: Check all links
      args: ["sh", "scripts/link-check.sh", "--all"]
```

[//]: # (References)

[pre-commit]: https://pre-commit.com/
[git]: https://gitscm.org/
[HTML]: https://en.wikipedia.org/wiki/HTML
