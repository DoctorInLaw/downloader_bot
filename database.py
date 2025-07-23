import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS approved_users (user_id INTEGER PRIMARY KEY)')
        self.cur.execute('CREATE TABLE IF NOT EXISTS captions (key TEXT PRIMARY KEY, value TEXT)')
        self.cur.execute('CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT)')
        self.conn.commit()

    def add_user(self, user_id):
        self.cur.execute('INSERT OR IGNORE INTO approved_users VALUES (?)', (user_id,))
        self.conn.commit()

    def remove_user(self, user_id):
        self.cur.execute('DELETE FROM approved_users WHERE user_id = ?', (user_id,))
        self.conn.commit()

    def get_users(self):
        self.cur.execute('SELECT user_id FROM approved_users')
        return [row[0] for row in self.cur.fetchall()]

    def set_caption(self, key, value):
        self.cur.execute('INSERT OR REPLACE INTO captions (key, value) VALUES (?, ?)', (key, value))
        self.conn.commit()

    def get_caption(self, key):
        self.cur.execute('SELECT value FROM captions WHERE key = ?', (key,))
        row = self.cur.fetchone()
        return row[0] if row else ""

    def set_setting(self, key, value):
        self.cur.execute('INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)', (key, value))
        self.conn.commit()

    def get_setting(self, key):
        self.cur.execute('SELECT value FROM settings WHERE key = ?', (key,))
        row = self.cur.fetchone()
        return row[0] if row else None

db = Database()
