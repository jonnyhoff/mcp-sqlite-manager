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

### 🐍 With Poetry (for development)

```bash
git clone https://github.com/your-username/mcp-sqlite-manager.git
cd mcp-sqlite-manager
poetry install
```
### 📚 Build and Install the Package
```bash
poetry build
pip install dist/mcp_sqlite_manager-*.whl
```

### ▶️ Running the Server
From source:

```bash
poetry run python -m mcp_sqlite_manager
```
Or from a built package (with a `__main__.py` entry point):

```bash
python -m mcp_sqlite_manager
```
(Optional CLI if you set up an entry point):

```bash
mcp-sqlite-manager
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

Make sure the `mcp-sqlite-manager` command is available in your system's PATH, or provide the full path to the executable.

### 🧪 Example Usage
#### list_tables
```json
{
  "tool": "list_tables",
  "arguments": {
    "db_path": "example.db"
  }
}
```
#### create_table
```json
{
  "tool": "create_table",
  "arguments": {
    "db_path": "example.db",
    "schema": "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT);"
  }
}

```

---

## 🧰 Development Notes
- Python 3.10+
- Poetry for dependency and package management
- SQLite is used via the built-in `sqlite3` module
- Tools are stateless — the database path must be passed to every call

---

## 🧑‍💻 Author
Jonathan Hoffman
🧠 Backend dev | 🐍 Pythonist | 🌍 Jeffreys Bay, South Africa

---

## 📄 License
MIT – free to use, hack, and improve.
