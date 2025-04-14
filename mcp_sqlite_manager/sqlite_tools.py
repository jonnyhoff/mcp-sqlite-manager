import sqlite3
from fastmcp import FastMCP

mcp = FastMCP("mcp-sqlite-manager")

def get_connection(full_db_path: str):
    """
    Establishes a connection to the SQLite database.

    Args:
        full_db_path: The full path to the SQLite database file.

    Returns:
        A sqlite3 connection object.
    """
    # Consider adding error handling for invalid paths or connection issues
    return sqlite3.connect(full_db_path)

@mcp.tool()
def read_query(full_db_path: str, query: str) -> list[dict]:
    """
    Execute a SELECT query on the SQLite database.

    Args:
        full_db_path: The full path to the SQLite database file.
        query: The SELECT SQL query to execute.

    Returns:
        A list of dictionaries, where each dictionary represents a row.
    """
    # Log entry point
    print(f"ℹ️ Executing read query on {full_db_path}: {query}")
    try:
        with get_connection(full_db_path) as conn:
            conn.row_factory = sqlite3.Row  # Return rows as Row objects (dict-like)
            cursor = conn.execute(query)
            results = [dict(row) for row in cursor.fetchall()]
            # Log success
            print(f"✅ Read query successful. Fetched {len(results)} rows.")
            return results
    except sqlite3.Error as e:
        # Log error
        print(f"❌ Error executing read query on {full_db_path}: {e}")
        # Re-raise or return an error message/object
        raise ValueError(f"Error executing read query: {e}") from e


@mcp.tool()
def write_query(full_db_path: str, query: str) -> str:
    """
    Execute an INSERT, UPDATE, or DELETE query on the SQLite database.

    Args:
        full_db_path: The full path to the SQLite database file.
        query: The SQL query (INSERT, UPDATE, DELETE) to execute.

    Returns:
        A success message indicating the number of rows affected.
    """
    print(f"ℹ️ Executing write query on {full_db_path}: {query}")
    try:
        with get_connection(full_db_path) as conn:
            cursor = conn.execute(query)
            conn.commit()  # Ensure changes are saved
            affected_rows = cursor.rowcount
            result_message = f"Query executed successfully. Rows affected: {affected_rows}"
            print(f"✅ {result_message}")
            return result_message
    except sqlite3.Error as e:
        print(f"❌ Error executing write query on {full_db_path}: {e}")
        raise ValueError(f"Error executing write query: {e}") from e


@mcp.tool()
def create_table(full_db_path: str, table_sql: str) -> str:
    """
    Create a new table in the SQLite database using raw SQL.

    Args:
        full_db_path: The full path to the SQLite database file.
        table_sql: The `CREATE TABLE` SQL statement.

    Returns:
        A success message.
    """
    print(f"ℹ️ Attempting to create table in {full_db_path} with SQL: {table_sql}")
    try:
        with get_connection(full_db_path) as conn:
            conn.execute(table_sql)
            conn.commit()
            result_message = "Table created successfully."
            print(f"✅ {result_message}")
            return result_message
    except sqlite3.Error as e:
        print(f"❌ Error creating table in {full_db_path}: {e}")
        raise ValueError(f"Error creating table: {e}") from e


@mcp.tool()
def list_tables(full_db_path: str) -> list[str]:
    """
    List all tables in the SQLite database.

    Args:
        full_db_path: The full path to the SQLite database file.

    Returns:
        A list of table names.
    """
    print(f"ℹ️ Listing tables in {full_db_path}")
    try:
        with get_connection(full_db_path) as conn:
            cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
            # Fetchall returns tuples, extract the first element (table name)
            tables = [row[0] for row in cursor.fetchall()]
            print(f"✅ Found tables: {tables}")
            return tables
    except sqlite3.Error as e:
        print(f"❌ Error listing tables in {full_db_path}: {e}")
        raise ValueError(f"Error listing tables: {e}") from e


@mcp.tool()
def describe_table(full_db_path: str, table_name: str) -> list[dict]:
    """
    Get the schema information (columns, types, etc.) for a specific table.

    Args:
        full_db_path: The full path to the SQLite database file.
        table_name: The name of the table to describe.

    Returns:
        A list of dictionaries, where each dictionary describes a column.
        Keys include: 'cid', 'name', 'type', 'notnull', 'dflt_value', 'pk'.
    """
    # Basic sanitization to prevent trivial SQL injection - consider more robust validation
    if not table_name.isidentifier():
         print(f"❌ Invalid table name provided: {table_name}")
         raise ValueError(f"Invalid table name: {table_name}")

    print(f"ℹ️ Describing table '{table_name}' in {full_db_path}")
    try:
        with get_connection(full_db_path) as conn:
            # Set row_factory to sqlite3.Row to get dict-like row objects
            conn.row_factory = sqlite3.Row
            # Use parameter substitution for safety, although PRAGMA doesn't directly support it.
            # The isidentifier check above provides some safety.
            # A more robust solution might involve checking against list_tables.
            cursor = conn.execute(f"PRAGMA table_info({table_name});")
            # Convert Row objects to standard dicts
            schema_info = [dict(row) for row in cursor.fetchall()]
            print(f"✅ Schema for table '{table_name}': {schema_info}")
            return schema_info
    except sqlite3.Error as e:
        print(f"❌ Error describing table '{table_name}' in {full_db_path}: {e}")
        raise ValueError(f"Error describing table '{table_name}': {e}") from e


if __name__ == "__main__":
    mcp.run()
