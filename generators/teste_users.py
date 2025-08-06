from pathlib import Path
import sqlite3


db_path = Path(__file__).parent.parent.resolve() / "app" / "models" / "database.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [row[0] for row in cursor.fetchall()]
print("Tables Found:")
for table in tables:
    print(f"— {table}")

print("Tables Structure:")
for table in tables:
    print(f"\n🔸 Tabela: {table}")
    cursor.execute(f"PRAGMA table_info({table})")
    columns = cursor.fetchall()
    for col in columns:
        cid, name, col_type, notnull, default, pk = col
        print(f"  • {name} ({col_type}){' [PK]' if pk else ''}")

result = conn.execute("""SELECT * FROM users ORDER BY ID DESC LIMIT 5""")
columns = [desc[0] for desc in result.description]
rows = result.fetchall()[::-1]

for row in rows:
    print("Users:")
    for col_name, value in zip(columns, row):
        print(f"{col_name}: {value}")
    print("-" * 30)

print(f"Database Path: {db_path}")
print(f"Existe? {db_path.exists()}")

conn.close()