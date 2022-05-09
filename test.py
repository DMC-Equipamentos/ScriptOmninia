from OmniaScript import ominiascript
import pandas as pd


# lê arquivo csv
data = pd.read_csv('test.xls', sep='\t')

# filtra testes PASS
data = data[data['Test Result'] == 'Pass']

# Agrupa por equipamento e número de série
data_grouped = data.groupby(['PC File Name', 'Serial Number'])

# cria dados com os passos
steps_grouped = data_grouped['Step'].apply(list)

good_files = []

# faz verificação
for index, steps in steps_grouped.iteritems():
    
    # verifica se todos os testes estão presentes 
    tests = [i in steps for i in range(1,10)]
    if all(tests):
        good_files.append(index)
        print("ok")
    else:
        print('Verificar equipamento:', index[0], index[1])
        

# Grava separadamente os arquivos bons:
for equipment in good_files:
    
    # filtra dados do equipamento
    equip_data = data[data["PC File Name"] == equipment[0]][data['Serial Number'] == equipment[1]]
    
    equip_data.to_csv('{}{}.xls'.format(*equipment),sep="\t")