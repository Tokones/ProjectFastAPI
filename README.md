Thats the first version of my python monolith code before proper refactoring

Initialy the goal was to learn how to create and manipulate data with SQL using SQLite3 and Pandas, but as the database got a somewhat "gaming" nomenclature, more things were implemented.
After that, the goal changed to learn how to implement HTTP structure to create a model client-server to interact with backend script using the framework Fast API and SwaggerUI interface for simple API test and use.

The folder "generators" is used to create the database.db with all tables necessary to run the project, and can run by either generate_data.bat or gen_all.py. All the data that is created was just a placeholder to understand how to use SQL using SQLite3 and any user created will start from ID 501 onwards.

Framework/Library used:
- Fast API
- Pydantic
- JOSE (PyJWT)
- BCrypt
- SQLite3
- Pandas
- NumPy
- PostgreSQL (psycopg2)
- SwaggerUI (uvicorn)

The requirements to run the project is done with the line:
pip install -r requirements.txt

The swagger can be started with the line:
uvicorn app.main:app --reload

By entering the localhost homepage will be redirected to /docs.
http://localhost:8000/

The .env file was commited because there is no need to hide the passcode by the simple nature of this project.