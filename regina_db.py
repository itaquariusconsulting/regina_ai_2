import pyodbc

def get_connection():
    try:
        cn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=192.168.2.10;"   # instancia nombrada
            "DATABASE=CONTABILIDAD;"
            "UID=sa;"
            "PWD=Acb123456;"
            "Encrypt=yes;"                    # encriptación obligatoria
            "TrustServerCertificate=yes;"     # confiar en el certificado (si no tienes uno)
            "MARS_Connection=Yes;"            # permite múltiples resultados
            "Connection Timeout=5;"           # tiempo de espera en segundos
        )
        return cn
    except pyodbc.Error as e:
        print("Error al conectar a SQL Server:", e)
        return None
