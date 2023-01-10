#get_all_sql_tables("kunde")
#get_all_sql_tables()
#insert_to_sql_table()
#get_sql_vals_by_column_and_value("kunde", "kundeid", 1)
#print(str(len(get_sql_vals_by_columns_and_values("kunde", "kundeid, vorname", "1, albernt"))))

def connect_to_sqlDb(db="test"):
    import globals
    #current_path=globals.get_current_path()
    settings_json=globals.get_settings_json()
    import mysql.connector
    return mysql.connector.connect(
        host=settings_json["sql_host"],
        user=settings_json["sql_user"],
        password=settings_json["sql_pass"],
        database=settings_json["sql_db"]
    )

def get_all_sql_databases():
    mydb = connect_to_sqlDb()
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x) 

def get_all_sql_tables():
    mydb = connect_to_sqlDb()
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)         

def get_all_sql_tables(table):
    mydb = connect_to_sqlDb()
    mycursor = mydb.cursor()
    mycursor.execute("SHOW COLUMNS FROM "+table)
    for x in mycursor:
        print(x)         
    
def get_all_sql_vals_from_table(table):
    mydb = connect_to_sqlDb()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM "+table)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)        
        
def insert_to_sql_table(table, column_name_csv, values_csv ):
    import mysql.connector
    mydb = connect_to_sqlDb()
    #mydb.database = "test"
    
    vals_string=""
    vals=values_csv.split(",")
    for val in vals:
        vals_string=vals_string+"'"+val+"',"
    vals_string = "".join(vals_string.rsplit(vals_string[-1:], 1))
    mycursor = mydb.cursor()
    sql = "INSERT INTO "+table+" ("+column_name_csv+") VALUES ("+vals_string+")"
    #print("SQL-Sting: "+sql)
    #val = ("John", "Highway", "hjhjg@jkjnjk.de")
    #mycursor.execute(sql, val)
    
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def get_sql_vals_by_id(table, id_in_table):
    mydb = connect_to_sqlDb()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM "+table+" WHERE id='"+str(id_in_table)+"'")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    
def get_sql_vals_by_column_and_value(table, column, value):   
    mydb = connect_to_sqlDb()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM "+table+" WHERE "+column+" ='"+str(value)+"'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
        
def get_sql_vals_by_columns_and_values(table, column_name_csv, values_csv):
    cols=column_name_csv.split(", ")
    vals=values_csv.split(", ")
    print("cols: "+str(len(cols))+", vals: "+str(len(vals)))
    if len(cols) == len(vals):
        
        sql_adding = ""
        cnt=0
        for col in cols:
            sql_adding += col+" like '"+vals[cnt]+"' AND "
            cnt=cnt+1
        sql_adding = "".join(sql_adding.rsplit(sql_adding[-5:], 1))
        sql = "SELECT * FROM "+table+" WHERE "+sql_adding
        print(sql)
        
        #mydb = connect_to_sqlDb()
        #mycursor = mydb.cursor()
        #mycursor.execute(sql)
        #myresult = mycursor.fetchall()
        
        mydb = connect_to_sqlDb()
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        print("zeilen in getSqlByColsAndVals: "+str(mycursor.rowcount))
        myresult = mycursor.fetchall()
        
        for x in myresult:
            print(x)
        return myresult
    else:
        print("colsCnt != valsCnt")
        return []

def delete_old_rows(table, datetime_column):
    mydb = connect_to_sqlDb()
    mycursor = mydb.cursor()
    sql = "DELETE FROM "+table+" WHERE "+datetime_column+" < DATE_SUB(NOW(), INTERVAL 7 DAY)"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, " SQL record(s) deleted")
