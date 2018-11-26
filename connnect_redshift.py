from sqlalchemy import create_engine
import pandas as pd

from settings import Config

url=Config.REDSHIFT_URL
login=Config.REDSHIFT_LOGIN
pwd=Config.REDSHIFT_PWD
port=Config.REDSHIFT_PORT
db=Config.REDSHIFT_DB


#engine = create_engine('postgresql://scott:tiger@hredshift_host:5439/mydatabase')
engine = create_engine(f'postgresql://{login}:{pwd}@{url}:{port}/{db}')
data_frame = pd.read_sql_query('SELECT * FROM shoes;', engine)
