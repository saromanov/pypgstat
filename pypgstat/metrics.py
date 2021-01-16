import argparse
import sqlalchemy as db
from pg_stat_database import PgStatDatabase

parser = argparse.ArgumentParser()
parser.add_argument('--host', action='store_true')
parser.add_argument('--pass', action='store_true')
parser.add_argument('--db', action='store_true')

engine = db.create_engine('postgresql://tracer:tracer@localhost:5432/tracer')
connect = engine.connect()

pgsd = PgStatDatabase(connect, 'tracer')
pgsd.result()