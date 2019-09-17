import mysql.connector
import random
import string

cnx = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="rootpassword",
  database="password"
)
n=int(input("Enter the length of the password (8-25)"))
cursor=cnx.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS pass (sl INT(12), pw VARCHAR(233))")
def randomstringsdigits(stringlength=n):
    lettersdigits=string.ascii_letters+string.digits+string.punctuation
    return''.join(random.choice(lettersdigits)for i in range (stringlength))

pwd=randomstringsdigits(n)
print("Generated password is:", pwd)
true = randomstringsdigits()
add_row=("INSERT INTO pass "
               "(sl,pw) "
               "VALUES (%s, %s)")
data_row=('1', '{}'.format(pwd))
cursor.execute(add_row, data_row)
cnx.commit()
b = 'yes'
while true:
    a = (input("Generate another password(YES/NO):"))
    if a == b:
        pwd1=randomstringsdigits()
        print("Your new password is:{}".format(pwd1))
        data_row1 = ('1', '{}'.format(pwd1))
        cursor.execute(add_row, data_row1)
        cnx.commit()
    else:
        print("exit")
        break


cursor.execute("SELECT * FROM pass")

for i in cursor:
  print(i)
