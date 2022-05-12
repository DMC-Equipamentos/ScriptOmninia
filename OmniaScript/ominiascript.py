from datetime import datetime
import os
import pandas as pd
from . import config
import shutil

def readXlsFile(path):
    """
    Lê o arquivo do omnia
    """

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
    data = pd.read_csv(path, sep='\t',
                    names = header, 
                    header=None, skiprows=1)
    
    data = fixSerialNumberFromDF(data)
    
    return data

def fixSerialNumber(sn):
    return sn
    # if len(sn.split(" ")) > 1:
    #     return a.split(" ")[-1]  

def fixSerialNumberFromDF(dataframe):
    """
    Corrige o número de série, que algumas vezes é 
    escrito erroneamente
    """
    dataframe['Serial Number'] = dataframe['Serial Number'].apply(
        fixSerialNumber  
    )
    return dataframe

def filterPassedTests(data):
    # filtra testes PASS
    return data[data['Pass/Fail'] == 'Pass'] 

def groupSteps(data):
    """
    Retorna um dataframe dos passos realizados por equipamento (NS)
    """    
    # Agrupa por equipamento e número de série
    data_grouped = data.groupby(
        ['PC File Name', 'Serial Number']
    )

    # cria dados com os passos
    steps_grouped = data_grouped['Step'].apply(list)
    
    return steps_grouped

def getTestExpectedParams(test_file):
    """
    Retorna parametros esperadis
    """
    return config.CONFIG_TESTS.get(test_file)
    
    
def createResultsFolder():
    """
    Cria pasta para guardar todos os resultados
    """
    name = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    os.mkdir(name)
    os.mkdir(os.path.join(name, 'Resultados'))
    return name

def saveFilesSeparate(equipments, dataframe, folder):
    """
    Salva separado os arquivos necessários
    equipments: Tuple(omnia file, sn)
    """

    # Grava separadamente os arquivos bons:
    for equipment in equipments:
        
        # filtra dados do equipamento específico
        equip_data = dataframe[dataframe["PC File Name"] == equipment[0]][dataframe['Serial Number'] == equipment[1]]
        
        # retira testes duplicados mantendo o último
        equip_data = equip_data.drop_duplicates(subset=['Step'], keep='last')
        
        equip_name = getTestExpectedParams(equipment[0])[0]
        filename = '{}-{}.xls'.format(equip_name, equipment[1])
        
        # grava em um CSV
        equip_data.to_csv(os.path.join(folder,'Resultados', filename),sep="\t", index=False)
        
def moveOriginalFileToResults(file, folder):
    filename = os.path.basename(file)
    shutil.move(file, os.path.join(folder, filename))