# FastAPI Template

This FastAPI template is designed to jumpstart your API development journey. It comes pre-configured with FastAPI, PostgreSQL, Async SQLAlchemy, and Async requests with AIOHTTP.

## Dependencies
- Docker
- Docker-compose
- Python >= 3.6
- Pipenv

## How to Run

### Setting up Environment

1. **Add Project Path:**
   Add the project path to the `PYTHONPATH` variable in the `.env` file.

2. **Start Pipenv Environment:**
   ```bash
   pipenv shell
   ```

3. **Select Python Interpreter:**
   Select the Python interpreter using the Visual Studio Code menu.

### Starting Services

4. **Start Docker Services:**
   Start the **postgres** database and **pgadmin**:
   ```bash
   docker-compose up -d
   ```

5. **Initialize Database:**
   Start the database (if necessary):
   ```bash
   python3 database/init_db.py
   ```

### Running the Application

6. **Start FastAPI Application:**
   Start the FastAPI application:
   ```bash
   uvicorn main:app --port 8080 --reload
   ```

7. **Access the Application:**
   Open your browser and navigate to:
   - Localhost: [http://127.0.0.1:8080/](http://127.0.0.1:8080/)
   - FastAPI Docs: [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)
   - PgAdmin: [http://127.0.0.1:5050](http://127.0.0.1:5050)
