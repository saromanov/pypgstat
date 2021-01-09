from table import Table
from sqlalchemy.sql import text

class PgStatDatabase(Table):
    ''' implementation of handling 
    pg_stat_databaase table

    https://postgrespro.ru/docs/postgrespro/9.5/monitoring-stats#pg-stat-database-view

    '''

    PG_STAT_DATABASE = 'pg_stat_database'

    def __init__(self, connection):
        Table.__init__(self, connection)
    
    def result(self):
        self._get_anomaly('tracer')
        print(self._get_basic_metrics("tracer"))
    
    def _get_anomaly(self, dbname:str):
        '''
        return anomalyes
        '''
        try:
            result = self._connection.execute(
                f'select datname, \
                CASE \
                    WHEN xact_commit+xact_rollback = 0 THEN 0 \
                    ELSE (xact_commit*100)/(xact_commit+xact_rollback) \
                END as c_ratio, \
                deadlocks, conflicts, temp_files, pg_size_pretty(temp_bytes) as temp_size \
                from {self.PG_STAT_DATABASE}')
            for r in result:
                print(result)
        except Exception:
            print('unable to get anomaly')
    
    def _get_basic_metrics(self, dbname:str):
        ''' return all metrics from pg_stat_database
        '''
        if not dbname:
            raise Exception('db name is not defined')
        return self.select_database(self.PG_STAT_DATABASE, dbname)