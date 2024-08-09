import sqlite3, os

def add_text(text):
    conn = sqlite3.connect('data.db')
    curs = conn.cursor()

    curs.execute("INSERT INTO text (texts) VALUES (?)", (text,))
    print('Add text success')
    conn.commit()
    conn.close()


def edit_text(id, new_text):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE text SET texts = ? WHERE id = ?", (new_text, id))
    
    conn.commit()
    print('Text edit success')
    conn.close()


def remove_text(id):
    conn = sqlite3.connect('data.db')
    curs = conn.cursor()
    
    curs.execute("DELETE FROM text WHERE id = ?",(id,))
    print('Remove text success')
    conn.commit()
    conn.close()


def view_db(table):
    conn = sqlite3.connect('data.db')
    curs = conn.cursor()
    
    curs.execute(f"SELECT * FROM {table}")
    resul = curs.fetchall()

    for line in resul:
        print(line)
    
    conn.close()


def menu():
    user = input(
        "1: Add Task\n2: Edit Task\n3: Remove Task\n4: View Tasks\n5: Exit\nType here:"
        )
     
    if user == '1': # Add
        os.system('cls')
        add_user_text = input('Type Task: ')
        add_text(add_user_text)
        os.system('cls')
        print('Task add sucess...')
        return menu()
    
    elif user == '2': # Edit
        os.system('cls')
        view_db('text')
        add_user_text = int(input('Type Id to edit: '))
        if add_user_text:
            user = input('Type the edit: ') 
            edit_text(add_user_text, user)
        os.system('cls')
        print('Task add sucess...')
        return menu()
    
    elif user == '3': # Remove
        os.system('cls')
        view_db('text')
        remove = int(input('Type Id to remove: '))
        remove_text(remove)
        return menu()
    
    elif user == '4': # View
        os.system('cls')
        view_db('text')
        print("All tasks...")
        return menu()

    elif user == '5': # Exit
        exit()
    
    elif user != '1' and '2' and '3' and '4' and '5': # Tratament
        os.system('cls')
        print('Typing 1 or 5 please...')
        return menu()
    



