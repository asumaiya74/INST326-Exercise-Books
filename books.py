"""Exercise 9 for INST 326 
Driver: Aysha Sumaiya
Navigator: Besufikad Tasissa
Assignment: Exercise 10
Date: 11/16/2021
Challenges Encountered: 
"""
#python books.py
import sqlite3 
import pandas as pd


class database_book:
    def __init__(self, database_name):
        """Create an database connection.

        Parameter:
            database_name(str): Name of the database to make connection
        """
        self.connection = sqlite3.connect(database_name)
        self.cursors = self.connection.cursor()
        self.database = []

    def load_data(self, filename):
        """Read the data from csv file & load them into connected database.

        Parameter:
            filename(str): Name of CSV file to read data from.
            table(str): creating table into the database 
        """
        table = "CREATE TABLE IF NOT EXISTS books" \
                "(Number INTEGER, " \
                "Title TEXT, " \
                "Author TEXT, " \
                "Year Of Publish INTEGER)"
        self.cursors.execute(table)


        filename = pd.read_csv("books.csv")
        for file in filename:
            self.database.append

        self.cursors.executemany("INSERT INTO books VALUES (?, ?, ?, ?)", self.database)
        self.connection.commit()

    def information(self):
        """ Print out the books information that is stored into the database. 

        each_row(str): fetching each row of the table. 
        """
        self.cursors.execute("SELECT * FROM books")
        each_rows = self.cursors.fetchall()
        print("%-8s%-50s%-35s%s" % ("Number", "Title", "Author", "Year Of Publish"))


        for rows in each_rows:
            print("%-8s%-50s%-35s%s" % (rows[0], rows[1], rows[2], rows[3]))


if __name__ == "__main__":
    """Creat an object of books.db that will take in the information from 
    csv file and load it into the database.
    """
    book = database_book("books.db")
    book.load_data("books.csv")
    book.information()
