from simple_salesforce import Salesforce

def get_salesforce():
    """
    Conecta ao Salesforce usando credenciais do usuário.
    Adapte as variáveis abaixo com as credenciais do seu ambiente.
    """
    sf = Salesforce(
        username="SEU_USERNAME", #seu email
        password="SUA_SENHA", #sua senha
        security_token="SEU_TOKEN" #seu token único do salesforce
    )
    return sf


def get_salesforce_report(sf):
    """
    Executa a query SOQL para buscar os dados desejados.
    Adapte o SELECT conforme o relatório do seu Salesforce. 
    """
    query = """
    SELECT
        Opportunity.AnoSafra__c,
        Opportunity.Id,
        Opportunity.StageName,
        Opportunity.CreatedDate,
        Opportunity.Account.Name,
        Product2.Id,
        Product2.Name,
        Quantity,
        TotalGeral__c,
        VariavelComercial__c
    FROM OpportunityLineItem
    WHERE IsDeleted = false
    """
    results = sf.query_all(query)
    return results["records"]
