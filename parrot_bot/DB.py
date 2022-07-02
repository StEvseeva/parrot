import sqlite3


def add_user(name, id):
    cur.execute(f'INSERT INTO users(id, username) VALUES("{id}", "@{name}")')
    conn.commit()


conn = sqlite3.connect('../DB/Parrot_Bot.db')
cur = conn.cursor()



