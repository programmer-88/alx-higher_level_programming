#!/usr/bin/python3

"""
Script that prints a list of states from the database hbtn_0e_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    HOST = 'localhost'
    PORT = 3306
    USER = argv[1]
    PASSWORD = argv[2]
    DATABASE = argv[3]

    db = MySQLdb.connect(
        host=HOST,
        port=PORT,
        user=USER,
        passwd=PASSWORD,
        db=DATABASE,
        charset="utf8"
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    
    cursor.close()
    db.close()
