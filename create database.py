import mysql.connector

my=mysql.connector.connect(host='localhost',
                              user='root',
                              database='project',
                              password='password')

cursor=my.cursor()

if my.is_connected():
    print('Database connected')







#creating customer table
sql='''CREATE TABLE customer
       (customer_id char(4) PRIMARY KEY,
        username varchar(50),
        password varchar(30),
        first_name varchar(100),
        last_name varCHAR(100),
        date_of_birth DATE,
        contact_number varchar(10),
        address varCHAR(200),
        city varCHAR(100),
        state varCHAR(100),
        zipcode INT(6),
        gender varchar(6));'''
cursor.execute(sql)
mycon.commit()
mycon.close()
