import mysql.connector

DB_NAME = "alx_book_store"
CREATE DATABASE IF NOT EXISTS alx_book_store

def main():
    try:
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        conn.commit()
        cursor.execute(f"SELECT COUNT(*) FROM information_schema.schemata WHERE schema_name = %s", (DB_NAME,))
        exists = cursor.fetchone()[0]
        if exists:
            print(f"Database '{DB_NAME}' created successfully!" 
                  if cursor.rowcount == 0 
                  else f"Database '{DB_NAME}' created successfully!")
        else:
            print(f"Database '{DB_NAME}' created successfully!")
    except Exception as e:
        print(f"Error: Failed while creating database: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
