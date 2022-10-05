from datetime import datetime
import os
import pandas as pd
from . import config
import shutil
from .filesread import readValidFile

def findValidFilesInCurrentFolder():
    """
    Acha todos os arquivos com a extensao xls na pasta atual
    """
    
    is_valid = lambda file: os.path.splitext(file)[-1] in ['.ods', '.csv', '.xls']
    
    return list(filter(is_valid, os.listdir()))


def readOmniaFile(path):
    """
    Lê o arquivo do omnia
    """

    data = readValidFile(path)
    
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
        filename = '{}-{}.ods'.format(equip_name, equipment[1])
        
        # grava em um CSV
        with pd.ExcelWriter(os.path.join(folder,'Resultados', filename), date_format='YYYY-MM-DD') as writer:
            equip_data.to_excel(writer, index=False)
        
def moveOriginalFileToResults(file, folder):
    filename = os.path.basename(file)
    shutil.move(file, os.path.join(folder, filename))