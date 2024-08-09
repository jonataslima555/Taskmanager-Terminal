import sqlite3


def add_text(text):
    conn = sqlite3.connect('data.db')
    curs = conn.cursor()

    curs.execute("INSERT INTO text (texts) VALUES (?)", (text,))

    conn.commit()
    conn.close()



def edit_text(id, new_text):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE text SET texts = ? WHERE id = ?", (new_text, id))
    
    conn.commit()
    conn.close()


def remove_text(id):
    conn = sqlite3.connect('data.db')
    curs = conn.cursor()
    
    curs.execute("DELETE FROM text WHERE id = ?",(id,))

    conn.commit()
    conn.close()



try:
    test1 = add_text('Good Morning!')
    test2 = edit_text(1, 'Hi, World')
    test3 = remove_text(2)
    print("Test Successelly")
except:
    print("Test Fail")
