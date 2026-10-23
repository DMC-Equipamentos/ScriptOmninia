from . import ominiascript as omnia
import pandas as pd
from . import config
import sys

def main():
    
    # encontra arquivos na pasta
    candidate_files = omnia.findValidFilesInCurrentFolder()
    n_files = len(candidate_files)
    
    if n_files == 0:
        print("Nenhum arquivo XLS encontrado")
        sys.exit(1)
    elif n_files > 1:
        print("Múltiplos arquivos XLS encontrados")
        sys.exit(1)
    
    omnia_file = candidate_files[0]
    
    # lê arquivo
    data = omnia.readOmniaFile(omnia_file)
    
    # mantém só a última execução de cada passo por equipamento,
    # para que a decisão use o mesmo dado que vai para o registro
    data_last = omnia.keepLastExecution(data)

    # agrupa o dataframe por equipamento mostrando os passos aprovados
    steps_grouped = omnia.groupPassedSteps(data_last)

    good_files = [] # Testes que deram certo
    any_fail = False
    not_configured = set()

    # faz verificação
    for index, steps in steps_grouped.items():
        
        # Busca nas configuraçoes o equipamento, 
        # Caso não encontre, avisa e pula
        config_data = omnia.getTestExpectedParams(index[0])
        
        if config_data is None:
            not_configured.add(index[0])
            continue # pula esse arquivo
        
        steps_verify = config_data[1] # steps

        # passos obrigatórios cuja última execução não foi aprovada
        failed = [i for i in steps_verify if i not in steps]
        
        if not failed: # passou em todos os testes
            good_files.append(index) # coloca em um vetor para utilizar depois
            
        else: # falhou em pelo menos 1 teste
            any_fail = True
            print('Verificar equipamento:', index[0], index[1])
            
            # mostra para o usuário os testes que estão faltantes (ou falharam).
            print(
                "Equipamento falhou no(s) teste(s):", 
                ", ".join(map(str, failed))
            )

    for test_file in sorted(not_configured):
        print("ATENÇÃO: arquivo de teste não cadastrado em config.py, "
              "equipamentos não separados:", test_file)

    if any_fail:
        return
    
    folder = omnia.createResultsFolder()
    omnia.saveFilesSeparate(good_files, data, folder)
    omnia.moveOriginalFileToResults(omnia_file, folder)

if __name__ == "__main__":
    main()