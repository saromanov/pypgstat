
class PgStatLocks(Table):
    """
    Showing statistics for locks
    """
    PG_STAT_DATABASE = 'pg_locks'
    def __init__(self, connection, *args, **kwargs):
        Table.__init__(self, connection)
        self._table_name = kwargs.get('table_name')
        self._db_metrics = kwargs.get('metrics_db')
