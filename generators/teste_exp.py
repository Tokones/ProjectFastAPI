from pathlib import Path
import sqlite3


db_path = Path(__file__).parent.parent.resolve() / "app" / "models" / "database.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

result = conn.execute("""SELECT * FROM exp ORDER BY level DESC LIMIT 5""")
columns = [desc[0] for desc in result.description]
rows = result.fetchall()[::-1]

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [row[0] for row in cursor.fetchall()]
print("Tables Found:")
for table in tables:
    print(f"— {table}")

for row in rows:
    for col_name, value in zip(columns, row):
        print(f"{col_name}: {value}")
    print(row)

print(db_path)