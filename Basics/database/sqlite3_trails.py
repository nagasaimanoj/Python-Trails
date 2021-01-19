import sqlite3

conn = sqlite3.connect(':memory:')


def create_db():
    print('create db --------')

    conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')


def create():
    print('create --------')

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (1, 'Paul', 32, 'California', 20000.00 )")

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

    conn.commit()


def retrive():
    print('retrive --------')

    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
        print(row)


def update():
    print('update --------')

    conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
    conn.commit()


def delete():
    print('delete --------')

    conn.execute("DELETE from COMPANY where ID = 2;")
    conn.commit()


create_db()

create()
retrive()

update()
retrive()

delete()
retrive()
