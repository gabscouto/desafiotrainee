def filtro_ano(year, set):
    return [data for data in set if (data[0] == year)]

def estado_media(state, set):
    state_pibs =  [float(data[6]) for data in set if (data[1] == state)]

    average = sum(state_pibs)/len(state_pibs)

    # print('Média do PIB per capita de ' + state + ': %.2f' %average)

    #Associando os valores em uma tupla para melhor manipulacao
    return (state, round(average, 2))



def q2(dataset):
    filter_2010 = filtro_ano('2010', dataset)
    list_uf = ['AC','AL', 'AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']

    lista_de_medias_em_2010 = []
    for uf in list_uf:
        lista_de_medias_em_2010.append(estado_media(uf, filter_2010))

    dictonary_uf = dict(lista_de_medias_em_2010)
    
    # Algoritmo para ordenar dicionarios em python
    sort_dictionary = sorted(dictonary_uf.items(), key=lambda x: x[1], reverse=True)

    #Formatando a resposta a ser impressa no arquivo
    q2_str = "Ranking de estados por media de PIB per capita no ano de 2010:\n"
    for uf in sort_dictionary:
        q2_str += uf[0]
        q2_str += ' '
        q2_str += str(uf[1])
        q2_str += '\n'


    return q2_str
