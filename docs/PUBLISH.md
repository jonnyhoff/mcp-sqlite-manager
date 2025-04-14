# Publish the package to PyPI

## Build the package

```bash
make build
```

## Install the package

```bash
make install-dist
```

## Test the package

1. Reload the installed MCP in the Cursor MCP settings.
2. Ask the agent to query and describe the test database.
3. Ask the agent to insert a new row into the test database.
4. Ask the agent to query and describe the test database again.

## Publish the package to PyPI

Make sure you've added your PyPI credentials to the poetry config.

```bash
poetry config pypi-token.pypi <your-pypi-token>
```

Then publish the package to PyPI:

```bash
make publish
```
