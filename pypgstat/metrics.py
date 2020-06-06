import sqlalchemy as db

PG_STAT_DATABASE = 'pg_stat_database'
engine = db.create_engine('postgresql://tracer:tracer@localhost:5432/tracer')
connect = engine.connect()
connect.execute(f'SELECT * FROM {PG_STAT_DATABASE}')