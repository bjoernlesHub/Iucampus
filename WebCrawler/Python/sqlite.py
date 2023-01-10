import sqlite3
import datetime

def create_connection(path):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(str(path)+"\db.sqlite3")
    except Error as e:
        print(e)

    return conn
	
def delete_old_rows(path, table, datetime_column):
    try:
        sqliteConnection = create_connection(path)
        cursor = sqliteConnection.cursor()
        #fifteen_minutes_before=datetime.datetime.now() - datetime.timedelta(minutes=15)
        #sql = "DELETE FROM "+table+" WHERE "+datetime_column+" <= "+date('now', '-10 minutes')
        #seven_days_before=time('now', '-7 days')
        sql = "DELETE FROM "+table+" WHERE "+datetime_column+" <= time('now', '-7 days')"
        cursor.execute(sql)
        sqliteConnection.commit()
        print(cursor.rowcount, " SQLITE record(s) deleted because it's older ")
    except sqlite3.Error as error:
        print("Failed to delete from table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def get_sqlite_vals_by_columns_and_values(path, table, column_name_csv, values_csv):
    try:
        sqliteConnection = create_connection(path)
        cursor = sqliteConnection.cursor()
        #print("Connected to SQLite")

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
            #cur = conn.cursor()
            cursor.execute(sql)

            rows = cursor.fetchall()
            print("Found "+str(len(rows))+" rows (things that was found before).")
            #for row in rows:
                #print(row)
            return rows
        else:
            print("colsCnt != valsCnt")
        cursor.close()
        return []

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def insert_to_sqlite_table(path, table, column_name_csv, values_csv ):
    sqliteConnection = create_connection(path)
    cursor = sqliteConnection.cursor()
    #print("Connected to SQLite")
	
    vals_string=""
    vals=values_csv.split(",")
    for val in vals:
        vals_string=vals_string+"'"+val+"',"
    vals_string = "".join(vals_string.rsplit(vals_string[-1:], 1))
    sql = "INSERT INTO "+table+" ("+column_name_csv+") VALUES ("+vals_string+")"
    print(sql)
    count = cursor.execute(sql)
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

