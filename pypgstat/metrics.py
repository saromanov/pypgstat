import sqlalchemy as db
from pg_stat_database import PgStatDatabase

engine = db.create_engine('postgresql://tracer:tracer@localhost:5432/tracer')
connect = engine.connect()

pgsd = PgStatDatabase(connect)
pgsd.result()