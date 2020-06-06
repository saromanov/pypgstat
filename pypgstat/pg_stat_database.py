from table import Table


class PgStatDatabase(Table):
    ''' implementation of handling 
    pg_stat_databaase table
    '''

    PG_STAT_DATABASE = 'pg_stat_database'

    def __init__(self, connection):
        Table.__init__(self, connection)
    
    def result(self):
        self._get_basic_metrics()
    
    def _get_basic_metrics(self):
        self._connection.execute(f'SELECT * FROM {self.PG_STAT_DATABASE}')