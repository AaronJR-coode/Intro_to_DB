import mysql.connector

DB_NAME = "alx_book_store"
CREATE DATABASE IF NOT EXISTS alx_book_store

def main():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="kundakite@22"
        )
    except Error as err:
         print(f"Error: Could not connect to MySQL server - {err}")
        return
        
    try:
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        conn.commit()
        exists = cursor.fetchone()[0]
        if exists:
            print(f"Database '{DB_NAME}' created successfully!" 
                  if cursor.rowcount == 0 
                  else f"Database '{DB_NAME}' created successfully!")
        else:
            print(f"Database '{DB_NAME}' created successfully!")
    except Error as err:
        print(f"Error: Failed while creating database - {err}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
