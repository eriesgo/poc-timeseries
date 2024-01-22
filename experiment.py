import os
import psycopg2
from psycopg2 import sql

def create_station_table(connection):
    with connection.cursor() as cursor:
        # Define the SQL query to create the 'station' table
        create_table_query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS station (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            )
        """)

        # Execute the SQL query
        cursor.execute(create_table_query)

    # Commit the transaction
    connection.commit()

def main():
    # Retrieve the TimescaleDB password from the environment variable
    timescaledb_password = os.environ.get("TIMESCALEDB_PASSWORD")

    if not timescaledb_password:
        raise ValueError("TIMESCALEDB_PASSWORD environment variable not set.")

    # Retrieve the TimescaleDB host from the environment variable
    timescaledb_host = os.environ.get("POSTGRES_HOST")

    if not timescaledb_host:
        raise ValueError("POSTGRES_HOST environment variable not set.")

    # Connect to the TimescaleDB database
    connection = psycopg2.connect(
        host=timescaledb_host,
        port=5432,
        user="postgres",
        password=timescaledb_password,
        database="timeseries"
    )

    try:
        # Call the function to create the 'station' table
        create_station_table(connection)

        print("Table 'station' created successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        connection.close()

if __name__ == "__main__":
    main()
