from asyncio import run
from database.connection import engine

from models.user import User

async def recreate_database_tables():
    async with engine.begin() as connection:
        for table in (User):
            print(f"Creating table: {table.__name__}")

            # Drop the table if it exists
            await connection.run_sync(table.metadata.drop_all)

            # Create the table
            await connection.run_sync(table.metadata.create_all)

            print(f"Created table: {table.__name__}")

if __name__ == '__main__':
    # Run the recreation process
    run(recreate_database_tables())
    