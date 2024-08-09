import sqlite3

def create_data():
    
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS text (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                texts TEXT
            )
        ''')
        conn.commit()
        print("Table 'text' created successfully")
    except sqlite3.OperationalError as e:
        if 'table text already exists' in str(e):
            print("Table 'text' already exists")
        else:
            print("An error occurred:", e)
    finally:
        conn.close()
