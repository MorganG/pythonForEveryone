import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS CountsUS''')

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE CountsUS (org TEXT, count INTEGER)''')

#CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    #pieces = line.split()
    #email = pieces[1]
    o = line.split('@')
    org = o[1]
    org = org.strip()

    #cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    #row = cur.fetchone()
    #if row is None:
    #    cur.execute('''INSERT INTO Counts (email, count)
    #            VALUES (?, 1)''', (email,))
    #else:
    #    cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
    #                (email,))
    #conn.commit()


    cur.execute('SELECT count FROM CountsUS WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO CountsUS (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE CountsUS SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()




# https://www.sqlite.org/lang_select.html
#sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

cur.execute('''
CREATE TABLE Counts AS SELECT org, count FROM CountsUS ORDER BY count ASC''')

sqlstr2 = 'SELECT org, count FROM CountsUS ORDER BY count DESC'

#for row in cur.execute(sqlstr):
#    print('email:',str(row[0]),'email count:', row[1])

for row in cur.execute(sqlstr2):
    print('Organization:',str(row[0]),'email count:', row[1])

cur.close()
