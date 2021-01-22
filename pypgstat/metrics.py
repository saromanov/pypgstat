import argparse
import sqlalchemy as db
from pg_stat_database import PgStatDatabase
from pg_stat_activity import PgStatActivity

parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, default='localhost')
parser.add_argument('--user', type=str)
parser.add_argument('--password', type=str)
parser.add_argument('--db', type=str)
args = parser.parse_args()
engine = db.create_engine(f'postgresql://{args.user}:{args.password}@{args.host}:5432/{args.db}')
connect = engine.connect()

pgsd = [PgStatDatabase(connect, table_name='tracer'), PgStatActivity(connect)]
for p in pgsd:
    p.result()