class Table:
    ''' base class for metric tables
    '''
    def __init__(self, connection):
        self._connection = connection