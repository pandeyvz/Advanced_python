#PDBC-Python data base programming :-How to cummunicate with databases
#permanent storage area:- File system ,Databases,
#Temporary storage:-PVM memory areas(python virtual machines)
#File system :-best suitable to store very less amount of info
#Database:-used to store large amount of data , python provides inbuilt modules for various type of data bases
# For Oracle database :-     cx_Oracle :- To communicate bw python and oracle database
# For Microsoftsql server:-- pymssql
# for Mysql databse :-       pymysql
#
# Standard steps to communicate with database
#     --Import the database module
#     --Establish connection bw python program and db
#       con=cx_Oracle.connect(database information)
#     --To execute sql query and store results cusrsor object is required
#       cursor=con.cursor
#     --Execute your query
#       cursor.execute(sqlquery)--->A single query
#       cursor.executescript(sqlqueries)-->To execute a string of sql queries separted by;
#       cursor.executemany()--->To execute a parametrized query
#     --Fetch the results
#       cursor.fetchone()-->To fetch one row
#       cursor.fetchall()-->To fetch all rows
#       cursor.fetchmany(n)-->To fetch n rows
#     --auto commit is not available as per java so we have to use commit() and if u r not satisfied rollback()
#     --con.close  or cursor.close
# Method names :-connect() , cursor() , execute() , executescript() , executemany() , fetchone() , fetchall() , fetchmany(), commit(), rollback(), close()

#Working with Oracle database
# print(help('modules')) #To get all the modules details
import cx_Oracle
connect=cx_Oracle.connect( 'scott/tiger@localhost')
