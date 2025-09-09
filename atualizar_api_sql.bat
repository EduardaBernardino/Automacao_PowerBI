@echo off
echo ======================================
echo Iniciando execucao: %date% %time%
echo ======================================

:: Caminho do Python (ajuste conforme sua instalação)
"C:\Users\SEU_USUARIO\AppData\Local\Programs\Python\Python311\python.exe" ^
"C:\Users\SEU_USUARIO\AutomaticoBI\OpportunityLineItemFiltrado.py" >> "C:\Users\SEU_USUARIO\AutomaticoBI\log_atualizacao.txt" 2>&1

echo ======================================
echo Execucao concluida: %date% %time%
echo ======================================


:: C:\Users\SEU_USUARIO\AppData\Local\Programs\Python\Python311\python.exe → caminho do Python instalado na sua máquina.
::C:\Users\SEU_USUARIO\AutomaticoBI\OpportunityLineItemFiltrado.py → caminho do script Python.
::C:\Users\SEU_USUARIO\AutomaticoBI\log_atualizacao.txt → caminho do arquivo de log onde será salvo o resulta