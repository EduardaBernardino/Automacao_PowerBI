from sqlalchemy import create_engine

def get_sql_engine():
    """
    Cria a conexão com o SQL Server.
    Adapte o servidor, banco e driver conforme seu ambiente.
    """
    server = "SEU_SERVIDOR\\SQLEXPRESS"
    database = "SEU_BANCO"
    driver = "ODBC Driver 17 for SQL Server" 

    connection_string = f"mssql+pyodbc://@{server}/{database}?driver={driver}"
    engine = create_engine(connection_string)
    return engine
