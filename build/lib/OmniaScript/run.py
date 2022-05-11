from multiprocessing import cpu_count
from . import ominiascript as omnia
import pandas as pd
from . import config


def main():
    # lê arquivo original
    data = omnia.readXlsFile(config.OMNIA_FILE_NAME)
    
    # filtra testes PASS
    data_pass = omnia.filterPassedTests(data) 

    # agrupa o dataframe por equipamento mostrando os passos realizados
    steps_grouped = omnia.groupSteps(data_pass)

    good_files = [] # Testes que deram certo
    bad_files = [] # Testes que deram errado
    any_fail = False

    # faz verificação
    for index, steps in steps_grouped.iteritems():
        
        # Busca nas configuraçoes o equipamento, 
        # Caso não encontre, pula
        config_data = omnia.getTestExpectedParams(index[0]) # config.get(index[0], None)
        
        if config_data == None:
            continue # pula esse arquivo
        
        steps_verify = config_data[1] # steps

        # verifica se todos os testes estão presentes 
        tests = [i in steps for i in steps_verify]
        
        if all(tests): # passou em todos os testes
            good_files.append(index) # coloca em um vetor para utilizar depois
            
        else: # falhou em pelo menos 1 teste
            any_fail = True
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

    if any_fail:
        return
    
    folder = omnia.createResultsFolder()
    omnia.saveFilesSeparate(good_files, data, folder)
    omnia.moveOriginalFileToResults(config.OMNIA_FILE_NAME, folder)

if __name__ == "__main__":
    main()