import pymysql
import yaml

def get_db():
    yaml_file = open('domain/server/db.yaml')
    db_config = yaml.load(yaml_file, Loader=yaml.FullLoader)
    conn = pymysql.connect(host=db_config['mysql_host'], user=db_config['mysql_user'], password=db_config['mysql_password'], db=db_config['mysql_db'])
    return conn