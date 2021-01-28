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
    def __init__(self, connection, *args, **kwargs):
         Table.__init__(self, connection)
         self._db_metrics = kwargs.get('metrics_db')
    
    def result(self):
        connections = self._total_connections()
        self._long_queries()
        self._db_metrics.write([('connections', connections)])
    
    def _total_connections(self):
        '''
        return number of total connections
        '''
        try:
            result = list(self._connection.execute(
                f'SELECT count(*) AS total_conns FROM\
                 {self.PG_ACTIVITY_DATABASE};'))
            if len(result) > 0:
                return result[0][0]
            
        except Exception:
            raise PyPGException('unable to get total connections')
    
    def _info(self):
        try:
            result = self._connection.execute(
                f'SELECT datname, pid, backend_start FROM {self.PG_ACTIVITY_DATABASE} ORDER BY backend_start DESC;')
            for r in result:
                print(r)
        except Exception:
            raise PyPGException('unable to get total connections')
    
    def _long_queries(self, interval='2 minutes'):
        '''
        return number of lonq queries bases on interval
        '''
        result = self.query(f"SELECT \
                pid, \
                now() - {self.PG_ACTIVITY_DATABASE}.query_start AS duration, \
                query,state FROM {self.PG_ACTIVITY_DATABASE} WHERE (now() - {self.PG_ACTIVITY_DATABASE}.query_start) > interval '{interval}';")
        for r in result:
            print(r)


