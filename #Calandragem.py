#Tempo do processo de Calandragem é 12 segundos por curva no tubo.
processo = 'Calandragem'

quantidade = input("Digite o número de dobras por peça: ")
tempo_peca = 12           #tempo por peça segundos
tempo = (tempo_peca * int(quantidade))/3600    #conversao para horas 

tempo_do_process = tempo #Salvar dados no modelo

#Print Resultado
print_menu = ' ---- Calculo do Tempo do Processo Para Peça Unitária ------\n Processo: '+ processo
print_infos = ' Tempo Padrão do Processo por Peça (min): ' + str(tempo_peca).replace(".", ",")
print_tempo = ' Tempo Salvo (Horas): ' + str(float("{0:.8f}".format(tempo))).replace(".", ",")
print_output = print_menu + '\n' + print_infos + '\n\n' + print_tempo 

print (print_output)