# Furação Bancada
processo = 'Furação Bancada'

from math import pi as PI

numero_furos = input("Digite a quantidade de furos que serão feitos:")
quantidade_ferramentas = input("Digite a quantidade de ferramentas usadas:")
diametro = input("Digite o diâmetro, em milímetros (mm), do furo:")
espessura = input("Digite a espessura da peça, em milímetros (mm):")

numero_furos = float(numero_furos)   #Número de furos do input
quantidade_ferramentas = float(quantidade_ferramentas) #Número de ferramentas do input
diametro = float(diametro) #Diâmetro dos furos em mm
espessura = float(espessura)  #Espessura dos furo em mm

tempo = (((espessura * 1) / ((30 * 1000) / (diametro * PI)) * 1 + (numero_furos * 0.4744444) + (quantidade_ferramentas * 0.1805)) * 0.01833333333) # Calculo de Tempo em horas

tempo_do_process = tempo #Salvando tempo no modelo

#Print Resultado
print_menu = ' ---- Calculo do Tempo do Processo Para Peça Unitária ------\n Processo: '+ processo
print_infos = ' \n Número de Furos: ' + str(numero_furos).replace(".", ",") + '\n Número de Ferramentas: ' + str(quantidade_ferramentas).replace(".", ",") + '\n Diâmetro do Furo (mm): ' + str(diametro).replace(".", ",") + '\n Espessura (mm): ' + str(espessura).replace(".", ",")
print_tempo = ' Tempo Salvo (Horas): ' + str(float("{0:.8f}".format(tempo))).replace(".", ",")
print_output = print_menu + '\n' + print_infos + '\n\n' + print_tempo 

print (print_output)