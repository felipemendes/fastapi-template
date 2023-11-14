# FastAPI Template

This FastAPI template is designed to jumpstart your API development journey. It comes pre-configured with FastAPI, PostgreSQL, Async SQLAlchemy, and Async requests with AIOHTTP.

## Dependencies
- Docker
- Docker-compose
- Python >= 3.6
- Pipenv

## How to Run

### Setting up Environment

**Add Project Path:**
   Add the project path to the `PYTHONPATH` variable in the `.env` file.

**Start Pipenv Environment:**
   ```bash
   pipenv shell
   ```

**Select Python Interpreter:**
   Select the Python interpreter using the Visual Studio Code menu.

### Starting Services

**Start Docker Services:**
   Start the **postgres** database and **pgadmin**:
   ```bash
   docker-compose up -d
   ```

**Connect to PgAdmin**
1. Open your web browser and go to `http://127.0.0.1:5050`
2. Log in using the default credentials (username: `admin@gmail.com`, password: `admin`).
3. Create a new connection:
   - Name: Choose a name for your connection.
   - Port: `5432`
   - Database: `fastapi-template`
   - Username: `admin`
   - Password: `admin`

**Initialize Database:**
   Start the database (if necessary):
   ```bash
   python3 database/init_db.py
   ```

### Running the Application

**Start FastAPI Application:**
   Start the FastAPI application:
   ```bash
   uvicorn main:app --port 8080 --reload
   ```

**Access the Application:**
   Open your browser and navigate to:
   - Localhost: [http://127.0.0.1:8080/](http://127.0.0.1:8080/)
   - FastAPI Docs: [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)
   - PgAdmin: [http://127.0.0.1:5050](http://127.0.0.1:5050)

![Screenshot 2023-11-13 at 22 12 50](https://github.com/felipemendes/fastapi-template/assets/3712089/9f137725-313e-43f1-8dd3-83613c6e9a2c)
