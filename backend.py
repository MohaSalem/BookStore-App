import sqlite3

class Database:
    
    def __init__(self, db): # pass self to avoid TypeError: '...takes 0 positional arguments but 1 was given.'
        """
        Initialise the object, when calling the class. Connecting to the database.
        """
        self.conn=sqlite3.connect('books.db')
        self.cur = self.conn.cursor() # assigning cursor object to the class attribute.
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()
        # removed the close method.

    def insert(self,title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()
        #conn.close() # removing the close() 

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        # delete something from book.db where id is equal to something.
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()
        #conn.close()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
        self.conn.commit()
        #conn.close()

    def __del__(self):
        """
        Closing the database connection.
        """
        self.conn.close()