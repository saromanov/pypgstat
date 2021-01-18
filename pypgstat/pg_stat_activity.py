from table import Table
from sqlalchemy.sql import text


# https://dataegret.ru/2015/11/introduction-to-pg_stat_activity/
# https://hakibenita.com/sql-anomaly-detection


class PyPGException(Exception):
    pass

class PgStatActivity(Table):
    '''
    implementation of handling pg_stat_activity
    '''
    PG_ACTIVITY_DATABASE = 'pg_stat_activity'
    def __init__(self, connection):
         Table.__init__(self, connection)
    
    def _total_connections(self):
        '''
        return number of total connections
        '''
        try:
            result = self._connection.execute(
                f'SELECT count(*) AS total_conns FROM\
                 {self.PG_STAT_DATABASE};')
            for r in result:
                print(result)
        except Exception:
            raise PyPGException('unable to get total connections')
    
    def _info(self):
        try:
            result = self._connection.execute(
                f'SELECT datname, pid, backend_start FROM {self.PG_ACTIVITY_DATABASE} ORDER BY backend_start DESC;')
            for r in result:
                print(result)
        except Exception:
            raise PyPGException('unable to get total connections')
