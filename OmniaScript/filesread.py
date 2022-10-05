
import pandas as pd
import os


def readValidFile(path):
    
    extension = os.path.splitext(path)[-1]
    
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

    if extension in ['.csv', '.xls']:
        data = pd.read_csv(path, sep='\t',
                        names = header, 
                        header=None, skiprows=1)
    else :
        data = pd.read_excel(path, names = header, 
                        header=None, skiprows=1)
    
    return data