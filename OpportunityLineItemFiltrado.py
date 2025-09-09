import pandas as pd
from sqlalchemy import create_engine
from salesforce_utils import get_salesforce, get_salesforce_report

# === Conexão Salesforce ===
sf = get_salesforce()
records = get_salesforce_report(sf)

print("🔌 Total de registros retornados:", len(records))

# === Normaliza em DataFrame ===
df = pd.json_normalize(records, sep=".")
df = df.drop(columns=[c for c in df.columns if "attributes" in c], errors="ignore")

# === Converte numéricos ===
for col in ["Quantity", "TotalGeral__c", "VariavelComercial__c"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# === Conexão com SQL Server ===
# Adapte o nome do servidor e banco
server = "SEU_SERVIDOR\\SQLEXPRESS"
database = "SEU_BANCO"
engine = create_engine(f"mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server") #Conexão da api com o ODBC

# === Salva dados na tabela ===
df.to_sql("ApiTable", engine, if_exists="replace", index=False)
print(" Dados atualizados no SQL Server.")
