import argparse
import sqlalchemy as db
from pg_stat_database import PgStatDatabase
from pg_stat_activity import PgStatActivity
from writer import Writer

parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, default='localhost')
parser.add_argument('--user', type=str)
parser.add_argument('--password', type=str)
parser.add_argument('--db', type=str)
args = parser.parse_args()
engine = db.create_engine(f'postgresql://{args.user}:{args.password}@{args.host}:5432/{args.db}')
connect = engine.connect()

engine_metrics = db.create_engine(f'postgresql://{args.user}:{args.password}@{args.host}:5432/{args.db}')
connect_metrics = engine.connect()
w = Writer(connect_metrics)
pgsd = [PgStatDatabase(connect, table_name='tracer', metrics_db=w), PgStatActivity(connect, metrics_db=w)]
for p in pgsd:
    p.result()