def filtro_cidade_pib_ocorrencias(city, set):
    return [float(data[6]) for data in set if (data[3] == city)]

#Aqui vamos filtrar todas as ocorrencias da cidade de Manaus no decorrer dos anos e tirar a média do PIB
def q1(dataset):
    #Exibindo os PIBs de Manaus formatados por cada ano
    manaus_pib_para_cada_ano = filtro_cidade_pib_ocorrencias('Manaus', dataset)

    #Calculando a media somando o valor total e dividindo pelo numero de ocorrencias:
    average = sum(manaus_pib_para_cada_ano)/len(manaus_pib_para_cada_ano)
    
    #print('Media do PIB per capita de Manaus de 2010 a 2018: %.2f' %average)

    return average