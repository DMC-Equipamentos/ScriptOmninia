
import pandas as pd
import os

operators = [ # código do operador não aparece no arquivo do omnia novo
    (1, "Adriana"),
    (2, "Caio"),
    (3, "Luis Felipe"),
    (4, "Maria Luiza"),
    (5, "Marilene"),
    (6, "Milton")
]

def askForOperator():
    print(
        """
        Digite o código do operador:
        """
    )
    
    for i, name in operators:
        print(i, '-', name)
    
    code = 0
    first = True
    
    while not int(code) in [a for a,_ in operators]: # em loop até que o código seja válido
        
        if not first:
            print("Código inválido, tente novamente:")
        
        code = input()
        
        first = False
    
    # cria um dicionário para facilitar a busca
    op_dict = {a:b for a,b in operators}
    
    return op_dict[int(code)]

def detectVersionAndUniform(data):
    
    if 'DUT Serial' in data.columns: # arquivo novo!
        
        # modifica coluna com o número de série
        data['Serial Number'] = data['DUT Serial']
        del data['DUT Serial']
        
        data['Operator ID'] = askForOperator()
        
        data['PC File Name'] = data['Test File Name']
        del data['Test File Name']
        
        data['Pass/Fail'] = data['Status'].apply(lambda st: st.capitalize())
        
    return data


def readValidFile(path):
    
    extension = os.path.splitext(path)[-1]
    
    # HEADERS do arquivo (não deve ser alterado)
    # header = ["Date", "Time", "Omnia File Name", "PC File Name", 
    #         "File", "Step", "Test Type", "Pass/Fail", 
    #         "Test Result", "Meter 1", "Meter 2", "Meter 3", 
    #         "Timer", "Meter 4", "Meter 5", "Model Number", 
    #         "Serial Number", "Probe", "Measuring Device", 
    #         "Test Model #", "Test Serial #", "Calibration Due Date", 
    #         "Operator ID", "Step 2"]

    # lê arquivo csv (não utiliza o HEADER do arquivo, 
    # que vem faltando a última coluna)

    if extension in ['.csv', '.xls']:
        data = pd.read_csv(path, sep=None, engine='python')
                        # names = header, 
                        # header=None, skiprows=1)
    else :
        data = pd.read_excel(path, sep = None)
    
    data = detectVersionAndUniform(data)
    
    return data