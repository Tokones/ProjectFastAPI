from pathlib import Path
import sqlite3


db_path = Path(__file__).parent.parent.resolve() / "app" / "models" / "database.db"
conn = sqlite3.connect(db_path)

result = conn.execute("""
    SELECT * FROM Materials ORDER BY id DESC LIMIT 10
""")
columns = [desc[0] for desc in result.description]
rows = result.fetchall()[::-1]

for row in rows:
    print("Materials:")
    for col_name, value in zip(columns, row):
        print(f"{col_name}: {value}")
    print("-" * 30)


print(f"Database Path: {db_path}")
print(f"Existe? {db_path.exists()}")

conn.close()