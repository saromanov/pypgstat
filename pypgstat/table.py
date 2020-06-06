class Table:
    ''' base class for metric tables
    '''
    def __init__(self, connection, *args, **kwargs):
        self._connection = connection