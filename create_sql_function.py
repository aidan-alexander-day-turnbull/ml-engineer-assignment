"""
This script contains 4 functions with the following functionality:
1. establish postgres connection
2. retrieve client information
3. update client information
4. locally test the above functions

Written By : Aidan Turnbull
Last Update : May 14th, 2025
"""
# import libraries
import psycopg2 # pip install pyscopg2-binary
import yaml # pip install PyYAML

def establish_postgres_connection():
    """
    This function returns a connection to the clientdb postgres server.

    :return: connection object
    """
    try:
        # import yaml file
        data = yaml.safe_load(open('secrets.yaml'))

        # connect to postgres database
        postgres_connection = psycopg2.connect(
        database = data.get('database'),
        user = data.get('user'),
        password = data.get('password'),
        host = data.get('host'),
        port = data.get('port')
        )

        # update console
        print("successfully connected to postgres database")

        # return successful connection
        return postgres_connection

    except Exception as error:
        # update console
        print("could not connect to postgres database")
        print(error)

        # terminate
        return 0


def retrieve_client_information(postgres_connection, client_id, encryption_key):
    """
    This function selects information based on a client id.

    :param postgres_connection: connection object
    :param client_id: integer
    :param encryption_key: string
    :return: query result
    """
    try:
        # establish cursor for database
        cursor = postgres_connection.cursor()

        # create query based on parameters
        select_query = ("SELECT client_id AS CLIENT_ID, PGP_SYM_DECRYPT(encrypted_clientname, '"
                        + encryption_key
                        +  "') AS CLIENT_NAME, PGP_SYM_DECRYPT(encrypted_email, '"
                        + encryption_key
                        + "') AS EMAIL, PGP_SYM_DECRYPT(encrypted_password, '"
                        + encryption_key
                        + "') AS PASSWORD, created_on AS CLIENT_SINCE FROM dbo.client_credentials_final WHERE client_ID = "
                        + str(client_id))

        # execute query
        cursor.execute(select_query)

        # package result
        client_info = cursor.fetchall()

        # update console
        print("successfully retrieved data")

        # return result
        return client_info

    except Exception as error:
        # update console
        print("could not retrieve data")
        print(error)

        # terminate
        return 0

def update_client_information(postgres_connection, client_id, column, new_info):
    """
    This function updates client information in the database based on client id

    :param postgres_connection: connection object
    :param client_id: integer
    :param column: string
    :param new_info: string
    :return: integer
    """
    try:
        # import yaml file
        data = yaml.safe_load(open('secrets.yaml'))

        # establish cursor for database
        cursor = postgres_connection.cursor()

        # fetch encryption key
        encryption_key = data.get('encryption_key')

        # create query based on parameters
        update_query = ("UPDATE dbo.client_credentials_final SET encrypted_"
                        + column
                        + " = PGP_SYM_ENCRYPT('"
                        + new_info
                        + "', '"
                        + encryption_key
                        + "') WHERE client_id = "
                        + str(client_id))

        # execute query
        cursor.execute(update_query)

        # update console
        print("successfully updated data")

        return 1

    except Exception as error:
        # update console
        print("could not update data")
        print(error)

        # terminate
        return 0


def function_tests():
    """
    This function locally tests 3 functions:
    (establish_postgres_connection, retrieve_client_information, and update_client_information)
    :return: integer
    """
    # import yaml file
    data = yaml.safe_load(open('secrets.yaml'))

    # fetch encryption key
    encryption_key = data.get('encryption_key')

    # connect to postgres database
    connection = establish_postgres_connection()

    # retrival test
    retrival_test = retrieve_client_information(connection, 3, encryption_key)
    print(retrival_test)

    # update test
    update_test = update_client_information(connection, 3, 'password', 'newPassword')

    # update confirmation test
    update_confirmation = retrieve_client_information(connection, 3, encryption_key)
    print(update_confirmation)

    return 1

if __name__ == '__main__':
    function_tests()


