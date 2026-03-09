# schemafi

Document your schema whenever you change it!

## Setup

Steps to follow to get started on this project:

- Make sure that `uv` is available on your machine
- Clone this repository and once it is downloaded, simply `cd` into schemafi directory and run `uv venv`. To activate your virtual environment run `source .venv/bin/activate`. Run `uv sync` which will simply install all required dependencies
- If you have the incorrect python version, please run `uv python install 3.12.11`

### Working with pre-commit

pre-commit is a set of hooks which will be triggered once you try to commit your changes, or, you can run it manually before you commit to make sure that your code is up to the standards.

#### How to set it up

- If you're using `uv`, simply run: `uv tool install pre-commit --with pre-commit-uv`
- Then simply run `pre-commit install`. If you receive an error that `pre-commit` command cannot be found, run `uv tool update-shell` and restart your terminal, once that's done, run `pre-commit install` and try the `pre-commit` command
- To bypass this, run every commit with the `--no-verify` flag
