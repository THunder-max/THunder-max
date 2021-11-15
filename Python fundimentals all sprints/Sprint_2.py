import MySQLdb
from MySQLdb import Error
from matplotlib import colors
import matplotlib.pyplot as plt
from numpy import array

def create_db_connection(host_name='DESKTOP-37VP4AN', user_name ='Ricky', user_password ='Citi202!rico',db_name = 'sprint_2'):
    connection = None
    try:
        connection = MySQLdb.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

#A function that will get a database connection ,query(SQL) and  execute it in the database
#Call this function when you are INSERTING or UPDATEING
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

#A function that will get a database connection ,query(SQL) and  execute it in the database and return data
#Call this function when you want data
def execute_get_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        return records
        #print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

db = create_db_connection()

execute_query(db,'DROP TABLE IF EXISTS PRODUCTS')
# cursor.execute("DROP TABLE IF EXISTS PRODUCTS")

sql = """CREATE TABLE PRODUCTS(

         PRODUCT_NAME  CHAR(20) NOT NULL,

         PRODUCT_AMOUNT INT )"""

execute_query(db,sql)

# cursor.execute(sql)

sql = """INSERT INTO PRODUCTS(PRODUCT_NAME,PRODUCT_AMOUNT)
                      VALUES ('Chips',5),
                      ('Cooldrinks',10),
                      ('Chocolates',15),
                      ('Pies',8),
                      ('Fruits',20),
                      ('Cupcakes',5),
                      ('Veggies',25)"""
execute_query(db,sql)

# cursor.execute(sql)
# db.commit()
# db.close()

# db = MySQLdb.connect("DESKTOP-37VP4AN","Ricky","Citi202!rico","sprint_2")
sql = 'SELECT PRODUCT_NAME FROM products;'
productsN = execute_get_query(db,sql)
arr = []
arr2 =[]
for i in productsN:
    arr.append(i[0])   
# cursor.execute(sql)
# x = cursor.fetchall()
sql ='SELECT PRODUCT_AMOUNT FROM products;'
productsA = execute_get_query(db,sql)
for i in productsA:
    arr2.append(i[0])

print(arr)
print(arr2)
# y = cursor.fetchall()
# cursor.execute(sql)
# plt.hist(productsA, bins = productsN)
# plt.xlabel('Product names')
# plt.ylabel('Product amount')
# plt.show()
plt.bar(arr, arr2)
plt.title("Sprint 2")
#plt.legend(5,5)
plt.xlabel('Product names')
plt.ylabel('Product amount')
plt.show()
