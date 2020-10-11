from table import Table
from sqlalchemy.sql import text

class PgStatActivity(Table):
    '''
    implementation of handling pg_stat_activity
    '''
    def __init__(self, connection):
         Table.__init__(self, connection)