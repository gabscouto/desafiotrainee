from q1.q1 import *
from q2.q2 import *
from q3.q3 import *



#Primeiro vamos filtrar o conjunto de dados com as infomaçoes que precisamos para responder as questoes
def format_dataset(file):
    dataset =  open(file, 'r', encoding='utf-8')
    filtered_set = []

    for lines in dataset:
        lines = lines.strip() #Removendo o /n ao final de cada linha
        columns = lines.split(";")

                        # Ano       Sigla      Estado       Municipio    Val. Serv.   Val. Total  PIB per capita
        formated_data = (columns[0], columns[1], columns[2], columns[3], columns[8], columns[10], columns[13] )
        filtered_set.append(formated_data)

    dataset.close()

    return filtered_set

# Temos uma estrutura que consiste em uma lista com os dados necessarios para responder as questões
# [( 0 ,         1      ,   2   ,     3    ,                   4                ,             5               ,       6       )]
# [(Ano, Sigla do Estado, Estado, Municipio, Valor adicionado bruto dos serviços, Valor adicionado bruto total, PIB per capita)]


#file_path = os.path.join('./dataset/', 'pib_municipio_2010_a_2018.txt' )
dataset = format_dataset('./dataset/pib_municipio_2010_a_2018.txt')


#Imprimindo saida da questao 1:
# path_q1 = os.path.join('./q1/', 'saida_q1.txt' )
q1_out = open('./q1/saida_q1.txt', 'w')
q1_out.write('Media do PIB per capita de Manaus de 2010 a 2018: %.2f' %q1(dataset))
q1_out.close()


#Imprimindo saida da questao 2:
# path_q2 = os.path.join('./q2/', 'saida_q2.txt' )
q2_out = open('./q2/saida_q2.txt', 'w')
q2_out.write(q2(dataset))
q2_out.close()


#Imprimindo saida da questao 3:
# path_q3 = os.path.join('./q3/', 'saida_q3.txt' )
q3_out = open('./q3/saida_q3.txt', 'w')
q3_out.write(q3(dataset))
q3_out.close()


