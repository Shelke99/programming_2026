import numpy as np
from flask_restful import Resource, request
import common.config as config
import pandas as pd
import logging
from datetime import datetime



class RetrieveDistinctData(Resource):
    '''
        Retrieving the DISTINCT domain and sub_domain data from the web_bot.web_bot_scrape table
    '''
    def post(self):
        connection = None
        try:
            start_time = datetime.now()
            logging.info(f'Retrieve API Started.....{start_time}')
            table_name = 'web_bot.web_bot_scrape'

            # db connection
            db_start_time = datetime.now()
            connection = config.conn()
            db_established_time = datetime.now() - db_start_time
            logging.info('Database Connection Established')
            if "None" in str(connection):
                logging.info('Database Connection Failed')
                return {"res_status": False, "msg": "Database Connection Failed"}
            logging.info(f"Time Taken To Establish DB Connection...{db_established_time.total_seconds()} Seconds")

            query = f"SELECT DISTINCT ON (domain, sub_domain) domain, sub_domain, created_by, created_on FROM web_bot.web_bot_scrape ORDER BY domain, sub_domain, created_on DESC"

            logging.info(f"Retrieve Query...{query}")
            final_dataframe = pd.read_sql(query, connection)
            if final_dataframe.empty:
                return {"res_status": False, "status": 200, "msg": "No records found"}
            Rows = len(final_dataframe.index)
            logging.info("No.of records in dataframes: \n " + str(Rows))
            start_time_cal = datetime.now()
            final_dataframe = final_dataframe.fillna("Null")
            logging.info(
                "time taken to fill nulls in dataframe:" + str(datetime.now() - start_time_cal) + "/n")
            values_list = final_dataframe.values.tolist()
            start_time_cal = datetime.now()
            logging.info("time taken to convert dataframe to list along with clob and blob datatypes:" + str(
                datetime.now() - start_time_cal) + "/n")
            columns_list = final_dataframe.columns.values.tolist()

            start_time_cal = datetime.now()
            reps = {'nan': None, '-9999': None, '-9999.0': None, '1969-12-31': None, 'Nan': None, 'NaT': None,
                    'nat': None, -9999: None, -9999.0: None,
                    (datetime.strptime('1969-12-31', '%Y-%m-%d')).date(): None,
                    datetime.strptime('1969-12-31 00:00:00', '%Y-%m-%d %H:%M:%S'): None,
                    datetime.strptime('0001-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'): None,
                    pd.to_datetime('1969-12-31 23:59:59.999990001'): None,
                    pd.NaT: None, np.nan: None, 'Null': None}
            values_list = [[x if type(x) in [list] else reps.get(x, x) for x in a] for a in values_list]
            logging.info("time taken to convert nan to none :" + str(datetime.now() - start_time_cal) + "/n")
            start_time_cal = datetime.now()
            logging.info("converting dataframes to json..........\n"
                         "....................................................................")
            returning_lists = []
            for values in values_list:
                list1 = {}
                for column_name in range(len(values)):
                    print(type(values[column_name]))
                    if any(item in str(type(values[column_name])) for item in
                           ['pandas._libs.tslibs.timestamps.Timestamp','pandas.Timestamp', 'datetime', 'Date',
                            'pandas.core.series.Series']):
                        list1[columns_list[column_name]] = str(values[column_name].strftime("%d-%m-%Y %H:%M:%S"))

                    else:
                        list1[(columns_list[column_name])] = (values[column_name])

                returning_lists.append(list1)
            logging.info(
                "time taken to convert key and value pairs :" + str(datetime.now() - start_time_cal) + "/n")
            logging.info("Retrieving completed returning json..........\n"
                         "....................................................................")

            execution_time = datetime.now() - start_time
            logging.info(f'Retrieve Query API Completed In...{execution_time.total_seconds()} Seconds')

            return {"res_status": True, "data": returning_lists}
        except Exception as rd:
            print(str(rd))
            logging.error(f"Error Occurred While Retrieving Data..{str(rd)}")
            return {"res_status": False, "msg": str(rd)}
        finally:
            if connection:
                config.ConnectionPooling.postgres_pool['pool'].putconn(connection)

class deleteRecords(Resource):
    '''
        DeleteRecords Class To Delete Records Based on domain and sub_domain
    '''
    def post(self):
        db_conn = None
        try:
            start_time = datetime.now()
            logging.info(f'Delete API Started....{start_time}')
            data = request.get_json()
            domain = data['domain']
            sub_domain = data['sub_domain']

            # db connection
            db_conn_start_time = datetime.now()
            db_conn = config.conn()
            db_established_time = (datetime.now() - db_conn_start_time)
            if 'None' in str(db_conn):
                return {'res_status': False, 'msg': 'Database Connection Failed'}
            logging.info(f'Database Connection Established.......{db_established_time.total_seconds()}')
            cursor = db_conn.cursor()

            query = f"DELETE FROM web_bot.web_bot_scrape WHERE lower(domain) = '{domain.lower()}' and lower(sub_domain) = '{sub_domain.lower()}'"
            logging.info(f'query to delete data............... + {str(query)}')
            cursor.execute(query)
            db_conn.commit()

            execution_time = (datetime.now() - start_time)
            logging.info(f'Delete API Completed......{execution_time.total_seconds()}')
            return {'res_status': True, 'msg': 'Data Deleted Successfully'}

        except Exception as e:
            print(str(e))
            logging.error(f'Error Occurred While Deleting Data.......{str(e)}')
            return {'res_status': False, 'msg': str(e)}
        finally:
            if db_conn:
                config.ConnectionPooling.postgres_pool['pool'].putconn(db_conn)

