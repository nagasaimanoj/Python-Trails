from datetime import datetime

file_name = input("enter output file name : ")
query = ""

while True:
    num = int(input("enter maximum number : "))
    y_or_n = input("this can lead to " + str(2 ** num) +
                   " records. do you still want to continue..?? (y / n) (default is n) : ")

    if y_or_n == 'y':
        query = "-- created on : " + str(datetime.now()) + "\n\n"
        query += "select a.* from(SELECT " + "\n"
        query += "(1 \n+ TWO_1.SeqValue "

        for i in range(1, num):
            j = 2 ** i
            query += " \n+ TWO_" + str(j) + ".SeqValue "

    query += ") SeqValue"
    query += " FROM " + "\n"
    query += "(SELECT 0 SeqValue UNION ALL SELECT 1 SeqValue) TWO_1" + "\n"

    for i in range(1, num):
        j = 2 ** i
        query += "CROSS JOIN (SELECT 0 SeqValue UNION ALL SELECT " + \
            str(j) + " SeqValue) TWO_" + str(j) + "\n"

    query += ") a order by a.SeqValue"

    file = open(file_name, 'w')
    file.write(query)
    file.close()
    if y_or_n != 'n':
        break
