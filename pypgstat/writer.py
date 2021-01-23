
class Writer:
    def __init__(self, connection):
        '''
        write data to backend
        '''
        self._connection = connection
    
    def write(self, data, *args, **kwargs):
        if len(data) == 0:
            return
        self._connection.execute('INSERT INTO pypgstat_metrics')
        