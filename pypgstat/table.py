from sqlalchemy.sql import text

class Table:
    ''' base class for metric tables
    '''
    def __init__(self, connection, *args, **kwargs):
        self._connection = connection
    
    def select_database(self, table_name:str, db_name: str) -> str:
       return dict(self._connection.execute(\
            text(f"SELECT * FROM {table_name} WHERE datname =:x"), x=db_name).fetchone())