from table import Table


class PgStatDatabase(Table):
    ''' implementation of handling 
    pg_stat_databaase table
    '''

    PG_STAT_DATABASE = 'pg_stat_database'

    def __init__(self, connection):
        Table.__init__(self, connection)
    
    def result(self):
        self._get_anomaly()
    
    def _get_anomaly(self):
        result = self._connection.execute(f'select datname, (xact_commit*100)/(xact_commit+xact_rollback) as c_ratio, deadlocks, conflicts, temp_files, pg_size_pretty(temp_bytes) as temp_size from {self.PG_STAT_DATABASE}')
        for r in result:
            print(result)
    
    def _get_basic_metrics(self):
        result = self._connection.execute(f'SELECT * FROM {self.PG_STAT_DATABASE}')
        for r in result:
            print(r)