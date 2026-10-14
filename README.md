# Tested examples: Python

A repository to copy for docs whose code examples say what they were tested with. Its docs, built with [Ascribe](https://ascribed-dev.com), show each example and the output it prints, and each code block names the versions of Python its example passed under. When an example changes and nobody tests it again, the line goes away and `ascribe check` says so.

| Path | What it is |
|---|---|
| `examples/` | Each example, a plain program in a file, and beside it the output it prints, `<name>.out.txt` |
| `tests/test_examples.py` | One test for each example: run it, and compare what it prints with its output file |
| `ascribe.examples.toml` | Which files are examples, the command that tests them, and what to note about where it ran |
| `examples.observations/` | What the test passed, and where: one file for each Python, written by `ascribe observe` |
| `docs/` | The docs: an Ascribe project that shows each example and its output |
| `.ascribe-version` | The release of `ascribe` CI installs |
| `.github/workflows/examples.yml` | The tests under each Python, a check of the observations, and the docs build, on every pull request and weekly |

Nothing here is written for Ascribe, and nothing needs Node: the tests are pytest, and `ascribe observe` writes the observations.

## Run it

Install `ascribe` without Node, with Homebrew or Ascribe's install script, at the release in `.ascribe-version`:

```sh
brew install ascribed-dev/tap/ascribe
# or
curl -fsSL https://ascribed-dev.com/install.sh | sh -s -- --version "$(cat .ascribe-version)"
```

Then, in a virtual environment of each Python you test with:

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -q                         # run each example
ascribe observe --name python-3-13          # under Python 3.13: test, then write examples.observations/python-3-13.toml
ascribe build --config docs                 # the docs, each code block with its tested line
```

`ascribe observe` runs the `test` line of `ascribe.examples.toml` as shell, as you, and writes the observation only when it passes. Run it once under each Python, with that Python's name: `python-3-12` and `python-3-13` here. Commit what it writes, as you would a lockfile.

## Add an example

1. Write `examples/<name>.py`, with the part the docs show between `# :snippet-start: <tag>` and `# :snippet-end:`.
2. Write what it prints in `examples/<name>.out.txt`. `pytest` runs it and compares.
3. Show both on a page under `docs/content/`:

   ```md
   @snippet: code:examples/<name>.py#<tag>

   @snippet {lang=text}: code:examples/<name>.out.txt
   ```

4. Run `ascribe observe --name python-3-12` under Python 3.12, and `--name python-3-13` under Python 3.13, and commit the two observations with the example.

An edit to an example without step 4 fails this repository's CI, at `ascribe observe --check`, which runs nothing and says which observation no longer matches. Locally, `ascribe check --config docs` reports `example-stale` at the `@snippet` line.

## Docs in another repository

Here the docs are beside the examples, and `docs/ascribe.toml` reads them through a source whose `path` is `..`. When your docs live in another repository, that source names this one instead, and the observations travel with the examples:

```toml
[sources.code]
git = "https://github.com/<you>/<this repository>.git"
branch = "main"
include = ["examples/**"]
```

Then `ascribe sources update` in the docs repository copies the examples and their observations, and says which went stale. The config and the observations stay here, and `ascribe observe` runs here. See [Show what an example was tested with](https://ascribed-dev.com/docs/examples/tested/).

## Ascribe's version

`.ascribe-version` pins the release CI installs. Move it to a new release. The observations stay current: an observation records the `ascribe` that wrote it, and goes stale only when an example changes.
