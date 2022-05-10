from multiprocessing import cpu_count
from OmniaScript import ominiascript
import pandas as pd
from testsconfig import config
import os, sys
import re 

# HEADERS do arquivo (não deve ser alterado)
header = ["Date", "Time", "Omnia File Name", "PC File Name", 
          "File", "Step", "Test Type", "Pass/Fail", 
          "Test Result", "Meter 1", "Meter 2", "Meter 3", 
          "Timer", "Meter 4", "Meter 5", "Model Number", 
          "Serial Number", "Probe", "Measuring Device", 
          "Test Model #", "Test Serial #", "Calibration Due Date", 
          "Operator ID", "Step 2"]

# lê arquivo csv (não utiliza o HEADER do arquivo, 
# que vem faltando a última coluna)
data = pd.read_csv('Therapy.xls', sep='\t',
                   names = header, 
                   header=None, skiprows=1)

# Corrige número de série (SN - XXXXXXX) -> (XXXXXXX)
data['Serial Number'] = data['Serial Number'].apply(
    lambda a: a.split(" ")[-1]
)

# filtra testes PASS
data = data[data['Pass/Fail'] == 'Pass']

# Agrupa por equipamento e número de série
data_grouped = data.groupby(
    ['PC File Name', 'Serial Number']
)

# cria dados com os passos
steps_grouped = data_grouped['Step'].apply(list)

good_files = [] # Testes que deram certo
bad_files = [] # Testes que deram errado

# faz verificação
for index, steps in steps_grouped.iteritems():
    
    # Busca nas configuraçoes o equipamento, 
    # Caso não encontre, pula
    steps_verify = config.get(index[0], None)
    if steps_verify == None:
        continue
    
    # verifica se todos os testes estão presentes 
    tests = [i in steps for i in steps_verify]
    
    if all(tests): # passou em todos os testes
        good_files.append(index) # coloca em um vetor para utilizar depois
        
    else: # falhou em pelo menos 1 teste
        print('Verificar equipamento:', index[0], index[1])
        failed = list(
            map(lambda a: a[0], # mostra apenas o número do teste
                filter(lambda a: not a[1],  # filtra testes que não foram aprovados
                    zip(steps_verify, tests) # junta número do test e resultado
                )
            )
        )
        
        # mostra para o usuário os testes que estão faltantes (ou falharam).
        print(
            "Equipamento falhou no(s) teste(s):", 
            ", ".join(map(str, failed))
        )

# Grava separadamente os arquivos bons:
for equipment in good_files:
    
    # filtra dados do equipamento específico
    equip_data = data[data["PC File Name"] == equipment[0]][data['Serial Number'] == equipment[1]]
    
    # retira testes duplicados mantendo o último
    equip_data = equip_data.drop_duplicates(subset=['Step'], keep='last')
    
    # grava em um CSV
    equip_data.to_csv('results/{}{}.xls'.format(*equipment),sep="\t")