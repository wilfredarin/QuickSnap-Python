from configs import env_variables
import mysql.connector
import json

# Utility methods to perform actions on databases


class DBActions:
    def fetch_database_info(database_name):
        with open(env_variables.DATABASE_CONFIGS_PATH, 'r') as config_file:
            config = json.load(config_file)
            return config[database_name]

    def fetch_databases_list():
        config = DBActions.fetch_database_info()
        return config[env_variables.DATABASE]

    def create_connection():
        """ 
        This method creates connection with the database
        param: 
            database_name: name of the database
        return: 
            Connection object or None
        """
        try:
            database_name = env_variables.QUICKSNAP_MAIN_DB
            configs = DBActions.fetch_database_info(database_name)
            print(database_name, configs)
            conn = mysql.connector.connect(
                host=configs[env_variables.HOST],
                user=configs[env_variables.USER],
                passwd=configs[env_variables.PASSWORD],
                database=configs[env_variables.DATABASE]
            )
            print("Connection Established")
            return conn
        except Exception as e:
            print(e)

    def check_if_table_exists_in_db(database_name, table_name):
        """
        This method checks if table_name is present in database_name
        params:
            database_name: name of the database
            table_name: name of the table which we are looking for
        return:
            true if present else false
        """
        conn = create_connection(database_name)
        sql_command = "SHOW TABLES FROM " + database_name + " LIKE '" + table_name + "';"
        print(sql_command)
        cursor = conn.cursor()
        cursor.execute(sql_command)
        if cursor.fetchone():
            return True
        else:
            return False

    def create_table(table_name):
        user_table = """
    CREATE TABLE IF NOT EXISTS user (
    user_id INT NOT NULL AUTO_INCREMENT,
    user_name VARCHAR(50) NOT NULL UNIQUE,
    gender VARCHAR(1),
    date_of_birth DATE,
    contact_number VARCHAR(75),
    email VARCHAR(255) NOT NULL UNIQUE,
    passwd VARCHAR(255) NOT NULL,
    created_at datetime DEFAULT NULL,
    updated_at TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW(),
    PRIMARY KEY(user_id),
    INDEX(user_id, user_name, email, contact_number)
    ) ENGINE = InnoDB;
        """

    def fetch_results_from_db(table_name, required_fields, where_clause):
        print("Fetching results from DB")
        conn = DBActions.create_connection()
        sql_command = "SELECT " + required_fields + " FROM " + \
            table_name + " WHERE " + where_clause + ";"
        cursor = conn.cursor()
        cursor.execute(sql_command)
        for result in cursor.fetchall():
            print(result)
        return cursor.fetchall()
