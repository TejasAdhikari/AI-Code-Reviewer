import psycopg2
import urllib.parse
from config import DATABASE_URL


def save_review(code, feedback):
    conn = None
    try:
        print("Connecting to the database.")
        print((f"Using DATABASE_URL: {DATABASE_URL}"))
        # Parse and reconstruct the DATABASE_URL with encoded password
        parsed = urllib.parse.urlparse(DATABASE_URL)
        encoded_password = urllib.parse.quote_plus(parsed.password)
        safe_url = f"postgresql://{parsed.username}:{encoded_password}@{parsed.hostname}:{parsed.port}/{parsed.path[1:]}"
        
        print(f"Attempting connection with parsed URL...")
        conn = psycopg2.connect(safe_url)
        print("Connected to the database.")
        
        cur = conn.cursor()
        
        print("Inserting data into code_reviews table...")
        cur.execute(
            "INSERT INTO code_reviews (code, feedback) VALUES (%s, %s)",
            (code, feedback)
        )
        conn.commit()
        print("Data inserted successfully.")

        # Select and print all rows from the code_reviews table
        cur.execute("SELECT id "
                    "FROM code_reviews "
                    "ORDER BY id DESC")
        rows = cur.fetchall()
        for row in rows:
            print(row)


        cur.close()
        return True
    except Exception as e:
        print(f"Database error: {str(e)}")
        return False
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")