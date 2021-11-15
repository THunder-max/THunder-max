import MySQLdb
from MySQLdb import Error

def create_db_connection(host_name='DESKTOP-37VP4AN', user_name ='Ricky', user_password ='Citi202!rico',db_name = 'sprint_3'):
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
# 1st table and contents for chips
sql = 'SELECT * FROM CHIPS;'
t1 = execute_get_query(db,sql)
print("Table exists , as follows:")
print(t1)

# 2nd table and contents for Cooldrinks 
sql = 'SELECT * FROM CHOCOLATE;'
t2 = execute_get_query(db,sql)
print("Table exists , as follows:")
print(t2)

# 3rd table and contents for Chocolate
sql = 'SELECT * FROM COOLDRINKS;'
t3 = execute_get_query(db,sql)
print("Table exists , as follows:")
print(t3)

# 4th table and contents for pies
sql = 'SELECT * FROM CUPCAKES;'
t4 = execute_get_query(db,sql)
print("Table exists , as follows:")
print(t4)

# 5th table and contents for fruits
sql = 'SELECT * FROM FRUITS;'
t5 = execute_get_query(db,sql)
print("Table exists , as follows:")
print(t5)

#6th table and contents for cupcakes 
sql = 'SELECT * FROM PIES;'
t6 = execute_get_query(db,sql)
print("Table exists , as follows:")
print(t6)

# 7th table and content for veggie types
sql = 'SELECT * FROM VEGGIES;'
t7 = execute_get_query(db,sql)
print("Table exists , as follows:")
print(t7)