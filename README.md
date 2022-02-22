pre-commit-exec
===============

This is a [pre-commit][] plugin which allows the execution of arbitrary
commands/scripts.  This plugin grants generic access to system commands and
repository scripts without the need to create a new repository. This is
particularly useful when a single check requires the combination of multiple
steps.  I.e. a [CI/CD][] workflow pattern.

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

This plugin supports 2 hooks: `command` and `shell`.  Both are handled by
[Python][]'s `subprocess.run()` interface.  The only difference between them is
that the `shell` hook grants access to various shell features.

From <https://docs.python.org/3/library/subprocess.html>:

>  This can be useful if you are using Python primarily for the enhanced
>  control flow it offers over most system shells and still want convenient
>  access to other shell features such as shell pipes, filename wildcards,
>  environment variable expansion, and expansion of ~ to a user’s home
>  directory. 

[//]: # (References)

[pre-commit]: https://pre-commit.com/
[git]: https://gitscm.org/
[HTML]: https://en.wikipedia.org/wiki/HTML
[subprocess]: https://docs.python.org/3/library/subprocess.html
[globbing]: https://en.wikipedia.org/wiki/Glob_(programming)
[Python]: https://python.org/
[CI/CD]: https://en.wikipedia.org/wiki/CI/CD
