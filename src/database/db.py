import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
        print(config('PGSQL_HOST'))
        print(config('PGSQL_USER'))
        print('contra: ',config('PGSQL_PASSWORD'))
        print(config('PGSQL_DATABASE'))
        print(config('PGSQL_PORT'))
        return psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE'),
            port=config('PGSQL_PORT')
        )
    
    except DatabaseError as ex:
        raise ex