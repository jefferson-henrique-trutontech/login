import sqlite3 as sql


class Database():
    def __init__(self):
        self.db = sql.connect('login.db')
        self.cur = self.db.cursor()
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS login(username text unique, senha text)')

    def adicionarUsuario(self, username, passw):
        if username != '' or passw != '':
            self.cur.execute(
                f'INSERT INTO login VALUES ("{username.lower()}", "{passw}")')
            self.db.commit()

    def verUsuarios(self):
        res = self.cur.execute('SELECT * FROM login')
        return res.fetchall()
