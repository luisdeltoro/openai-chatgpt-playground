# openai-chatgpt-playground
A repository containing examples of how to use the openai API

This repository uses pants build system
See [pantsbuild.org](https://www.pantsbuild.org/docs) for much more detailed documentation.

# Pants cheatsheet

Targets are a way of setting metadata for some part of your code, such as timeouts for tests and 
entry points for binaries. Targets have types like `python_source`, `resources`, and 
`pex_binary`. They are defined in `BUILD` files.

Pants goals can be invoked on targets or directly on source files (which is often more intuitive and convenient).
In the latter case, Pants locates target metadata for the source files as needed.

## File specifications

Invoking goals on files is straightforward, e.g.,

```
pants test examples/chatgpt1/chatgpt_test.py
```

You can use globs:

```
pants lint examples/chatgpt1/*.py
```

But note that these will be expanded by your shell, so this is equivalent to having used

```
pants lint examples/chatgpt1/__init__.py examples/chatgpt1/chatgpt.py examples/chatgpt1/chatgpt_test.py
```

If you want Pants itself to expand the globs (which is sometimes necessary), you must quote them in the shell:

```
pants lint 'examples/chatgpt1/*.py'
```

You can run on all changed files:

```
pants --changed-since=HEAD lint
```

You can run on all changed files, and any of their "dependees":

```
pants --changed-since=HEAD --changed-dependees=transitive test
```

## Target specifications

Targets are referenced on the command line using their address, of the form `path/to/dir:name`, e.g.,

```
pants lint examples/chatgpt1:lib
```

You can glob over all targets in a directory with a single trailing `:`, or over all targets in a directory
and all its subdirectories with a double trailing `::`, e.g.,

```
pants lint examples::
```

## Globbing semantics

When you glob over files or targets, Pants knows to ignore ones that aren't relevant to the requested goal.
For example, if you run the `test` goal over a set of files that includes non-test files, Pants will just ignore
those, rather than error. So you can safely do things like

```
pants test ::
```

To run all tests.

# Example Goals

Try these out in this repo!

## List targets

```
pants list ::  # All targets.
pants list 'examples/**/*.py'  # Just targets containing Python code.
```

## Run linters and formatters

```
pants lint ::
pants fmt examples/chatgpt1::
```

## Run MyPy

```
pants check ::
```

## Run tests

```
pants test ::  # Run all tests in the repo.
pants test --output=all ::  # Run all tests in the repo and view pytest output even for tests that passed (you can set this permanently in pants.toml).
pants test examples/chatgpt1:tests  # Run all the tests in this target.
pants test examples/chatgpt1/chatgpt_test.py  # Run just the tests in this file.
pants test examples/chatgpt1/chatgpt_test.py -- -k test_generate_question  # Run just this one test by passing through pytest args.
```

## Create a PEX binary

```
pants package examples/chatgpt1/chatgpt.py
```

## Run a binary directly

```
pants run examples/chatgpt1/chatgpt.py
```

## Open a REPL

```
pants repl examples/chatgpt1:lib  # The REPL will have all relevant code and dependencies on its sys.path.
pants repl --shell=ipython examples/chatgpt1:lib --no-pantsd  # To use IPython, you must disable Pantsd for now.
```

## Build a wheel / generate `setup.py`

This will build both a `.whl` bdist and a `.tar.gz` sdist.

```
pants package examples/chatgpt1:dist
```

## Count lines of code

```
pants count-loc '**/*'
```
## Create virtualenv for IDE integration

```
pants export ::
```
