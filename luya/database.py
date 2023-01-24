
import sqlite3



class DataBaseSensor:
    def __init__(self):
        self.NAME_DB = '/home/user/Desktop/DataBaseSensor.db'
        self.NAME_TABLE = "Sensor"
        self.con = sqlite3.connect(self.NAME_DB)
        self.cur = self.con.cursor()


    def drop_table(self,table:str):
        """
       delete table in the db
       :param table: name of the table
        :return:
        """
        self.cur.execute(f''' DROP TABLE {table}''')
        self.con.commit()

    def create_table(self,table:str):
        """
        create new table in DB where to store each new values
        :param table: name of the table
        :return:
        """
        self.cur.execute(f'''CREATE TABLE {table}
                         (id integer primary key,
                          datetime_ DATE, 
                          temperature REAL )''')
        self.con.commit()

    def print_all_info_from_table(self):
        """
        return all info from the db-node table
        :return: nothing
        """
        self.cur.execute(f"select * from {self.NAME_TABLE}")
        result = self.cur.fetchall()
        print('INFO:')
        for node in result:
            print(node)
        return

    def adding__new_date(self, date:str, temperature:float):
        """
        create a new row
        :param date: str '2023-01-08 01:00'
        :param temperature: float
        :return:
        """

        self.cur.execute(f'''INSERT INTO {self.NAME_TABLE} (datetime_ ,temperature)
                               VALUES (?,?);''',
                         (date,temperature))
        self.con.commit()

    def close(self):
        """
        close connection to the DB IMPORTANT
        """
        self.con.close()

    def clear_table(self,table):
        """
        clear the rows into table
        :param table: name of the table
        :return:
        """
        self.cur.execute(f"""DELETE FROM {table}""")
        self.con.commit()



