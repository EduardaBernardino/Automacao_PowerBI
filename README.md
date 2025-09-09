Visão Geral
•	A automação tem como objetivo principal realizar a automação de dashboards no Power BI conforme atualizações geradas na ferramenta Salesforce.

Salesforce                                                  SQL Server                                                           Power BI 


Passo 1 - Preparação do Ambiente
Pré-Requisitos

o	Python + PIP
o	SQL Server Express + SSMS
o	Power BI Desktop
o	Power BI Service + Gateway
o	Driver ODBC para SQL Server

1.	Instalar o Python 3.x e as bibliotecas necessárias. (Utilizar Vs Code ou InteliJ mais prático)

   



2. Instalar o SQL Server Express + SSMS

   

Vídeo explicativo: https://www.youtube.com/watch?v=QOXiRS1yWhE&t=1024s

3. Instalar o Power BI Desktop.


4. Criar conta e configurar o Power BI Service. (Logar no PowerBI e criar o seu workspace)



5. Instalar e configurar o On-premises Data Gateway (necessário para atualização automática no Power BI).
  
  
  


No Power BI Desktop, conectar ao SQL Server (`Servidor: NOME_DO_SERVIDOR` Ex:  `Banco: BoasafraDB`).
2. Escolher modo de conexão: Import (mais comum) ou DirectQuery.
3. Publicar o relatório no Power BI Service.
4. Configurar o Gateway de Dados para permitir atualização automática.
5. Definir o agendamento de atualização no Power BI Service (ex: diariamente, de hora em hora, etc).

  
 
  

 

  

  

  
Passo 2 - Estrutura da API (extração do Salesforce)
A API foi estruturada em scripts Python que acessam o Salesforce, filtram os dados e preparam os arquivos para serem carregados no SQL Server.
Pasta zipada com os arquivos já criados( Obs: altere com suas credenciais onde está comentado no código em verde #) :

 AutomacaoBI.zip


Obs: Onde encontrar meu token do salesforce?
 
  

Instalar bibliotecas necessárias:
•	No VsCode ou InteliJ, para acessar o terminal:  ctrl + J 
•	Intale o pip digitando no terminal: python -m pip install pandas
Obs: Se der erro digite: py -m pip install pandas



•	Instale todas as bibliotecas:
py -m pip install simple-salesforce pandas openpyxl sqlalchemy pyodbc colorama
Se der erro: 
python -m pip install simple-salesforce pandas openpyxl sqlalchemy pyodbc colorama


Principais arquivos da API (você deve criar esses arquivos em alguma das ferramentas mencionadas)
  
• salesforce_utils.py → Contém funções de autenticação e consultas no Salesforce (SOQL).
• OpportunityLineItemFiltrado.py → Executa a extração dos dados filtrados, gera CSV e envia ao SQL Server.
• export_sf_report.py → Exporta relatórios do Salesforce diretamente (quando necessário).
• conexao.py / conectionsql.py → Configuração da conexão com o SQL Server.
• atualizar_api_sql.bat → Script em lote usado pelo Agendador de Tarefas do Windows para executar a automação periodicamente.
• log_atualizacao.txt → Log das execuções automáticas (útil para auditoria e troubleshooting).
Passo 3 - Banco de Dados (SQL Server)
1.	Criar o banco de dados Ex:`BoasafraDB` no SQL Server.

 


2. Criar a tabela Ex: `ApiTable` para receber os dados da API.


3 – Conectar API ao Banco de Dados (ODBC) :
•	Instale o ODBC server: https://learn.microsoft.com/pt-br/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver17

 
 



4. O script `OpportunityLineItemFiltrado.py` já está configurado para inserir os dados no SQL Server.
5. Testar com queries SQL, por exemplo:

   SELECT COUNT(*) FROM ApiTable;                    * Para contar o total de registros 
   SELECT SUM(TotalGeral__c) FROM ApiTable;               *Para calcular a soma do total geral

SELECT SUM(Quantity) AS SomaQuantidade FROM OpportunityLineItemFiltrado; *Para somar a quantidade de itens vendidos
 

 

Passo 4 - Automação da Carga de Dados
1.	No agendador de tarefas do Windows você irá configurar o período que você quer rodar o script em python, ou seja, o período de atualização dos dados. 
 

  


2.	Foi criado um arquivo `.bat` que executa o script Python automaticamente. Esse `.bat` foi configurado no Agendador de Tarefas do Windows para rodar em horários definidos.

Exemplo do arquivo `atualizar_api_sql.bat`:

@echo off
echo ================================
echo Iniciando execução: %date% %time%
python C:\caminho\OpportunityLineItemFiltrado.py
echo Execução concluída. Veja o log em: log_atualizacao.txt
echo ================================



Passo 5 - Monitoramento e Logs
• O arquivo log_atualizacao.txt registra cada execução.
• O SQL Server pode ser monitorado via Management Studio (SSMS).
• O Power BI Service fornece histórico de atualizações e alertas em caso de falha.



•	Nas próximas atualizações não será necessário instalar as bibliotecas novamente 

