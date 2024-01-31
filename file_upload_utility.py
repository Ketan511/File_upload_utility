"""provides the utility as follows 
Whenever the above utility is executed with necessary arguments it will take a directory as 
an argument, and read all files from the directory, and upload them to the corresponding 
MySQL table specified in config.
"""
import os
from argparse import ArgumentParser, Namespace
import json
import pandas as pd
# import pymysql
import sqlalchemy

def read_mysql_config_from_json(json_file_path):
    """Function Reads data from json and returns object"""
    with open(json_file_path, 'r') as json_file:
        mysql_config = json.load(json_file)
    return mysql_config

def find_mysql_config_file(files,source_dir):
    """Function gives config file to connect with MySQL"""
    for file in files:
        if file == 'mysql_config.json':
            return os.path.join(source_dir, file)
    return None

def mysql_connection(mysql_config, args):
    """MySql connection and loading data from csv to sql"""
    engine = None
    try:
        # Create SQLAlchemy engine from configuration
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{mysql_config['user']}:{mysql_config['password']}@{mysql_config['host']}:{mysql_config['port']}/{mysql_config['database']}")
        print("Connected to MySQL!")

        for file in os.listdir(args.source_dir):
            if file.endswith('.csv'):
                csv_file_path = os.path.join(args.source_dir, file)

                # Read CSV into Pandas DataFrame
                df = pd.read_csv(csv_file_path)

                # Load Pandas DataFrame to MySQL using SQLAlchemy engine
                df.to_sql(name=args.destination_table, con=engine, if_exists='append', index=False)

                print(f"Loaded {file} into MySQL.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if engine is not None:
            engine.dispose()
            print("Engine closed.")



def main():
    parser = ArgumentParser(
        usage="%(prog)s:Upload CSV files to MySQL"
    )

    parser.add_argument('source_dir', help='provide source directory', type=str)
    parser.add_argument('destination_table', help='provide desitnation table name', type=str)
    args: Namespace = parser.parse_args()


    
    if args.source_dir and os.path.exists(args.source_dir):
        
        source_dir=args.source_dir
        files = os.listdir(args.source_dir)
            
        mysql_config_file = find_mysql_config_file(files,source_dir)
        if mysql_config_file:
            mysql_config = read_mysql_config_from_json(mysql_config_file)
            mysql_connection(mysql_config,args)
        else:
            print("MySQL config file not found ")
    else:
        print(f"Error: The provided source directory '{args.source_dir}' is invalid or does not exist.")
        return
    
if __name__ == "__main__":
    main()
