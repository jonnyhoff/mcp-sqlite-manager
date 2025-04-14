# mcp-sqlite-manager

An [MCP](https://github.com/openai/function-calling-spec) server built with [FastMCP](https://pypi.org/project/fastmcp/) to interact with SQLite databases. Easily query, update, and inspect SQLite data using structured tools.

---

## 🚀 Features

- `read_query`: Execute a `SELECT` query and return results as JSON.
- `write_query`: Execute `INSERT`, `UPDATE`, or `DELETE` queries.
- `create_table`: Create new tables using SQL schema definitions.
- `list_tables`: Return a list of all tables in the database.
- `describe_table`: Show schema info for a specific table (like `PRAGMA table_info`).

---

## 📦 Installation

### 🐍 With pipx

This package is designed to be installed with [pipx](https://pipx.pypa.io/stable/installation/), which allows you to run Python applications in isolated environments.

```bash
pipx install --force mcp-sqlite-manager
```

### 🔌 MCP Integration in Cursor

To use this server as an MCP tool within Cursor, add the following configuration to your `~/.cursor/mcp.json` file or configure via the settings menu in Cursor.

```json
{
    "mcpServers": {
        "mcp-sqlite-manager": {
            "command": "mcp-sqlite-manager"
        }
    }
}
```

## 🧑‍💻 Author

**Jonathan Hoffman**
[GitHub](https://github.com/jonnyhoff)
[LinkedIn](https://www.linkedin.com/in/jonathan-hoffman-b5839195/)

🐍 Python, Django, JS, Web, ML, AI, coffee and 🍺 beer.



---

## 📄 License
MIT – free to use, hack, and improve.
