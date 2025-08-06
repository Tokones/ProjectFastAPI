from pathlib import Path
from generators.gen_exp import generate_exp_table_sql
from generators.gen_users import generate_user_and_gear_tables_sql
from generators.gen_mat import generate_material_table


def main():
    path = Path(__file__).parent.parent.resolve() / "app" / "models"
    generate_exp_table_sql(path)
    generate_user_and_gear_tables_sql(path)
    generate_material_table(path)
    
if __name__ == "__main__":
    main()