from table import Table

class PgStatDatabase(Table):
    ''' implementation of handling 
    pg_stat_databaase table
    '''
    def __init__(self, connection):
        Table.__init__(self)