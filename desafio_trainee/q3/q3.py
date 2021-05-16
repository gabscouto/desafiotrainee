def filtro_ano(year, set):
    return [data for data in set if (data[0] == year)]

def estado_servico_proporcao(state, set):
    estado_total_pibs =  [float(data[5]) for data in set if (data[1] == state)]
    estado_servico_pibs =  [float(data[4]) for data in set if (data[1] == state)]
    
    media_total = sum(estado_total_pibs)/len(estado_total_pibs)
    media_services = sum(estado_servico_pibs)/len(estado_servico_pibs)

    # print('Média do PIB total  ' + state + ': %.2f' %average_total)
    # print('Média do PIB servicos  ' + state + ': %.2f' %average_services)

    # Calulando a proporcao media divindo o valor medio por municipios em servicos pelo PIB total
    proportion = media_services/ media_total
    percent = proportion * 100

    format_proportion = str(round(proportion, 4))
    format_percent = str(round(percent, 2)) + '%'


    #Retornando o valor em percentual
    return 'Proporcao do valor adicionado bruto medio do setor de servicos em relacao ao valor adicionado bruto total medio no estado do Amazonas no ano de 2018: ' + format_proportion + '\nEm percentual: ' +  format_percent

def q3(dataset):
    filtro_2018 = filtro_ano('2018', dataset)

    return(estado_servico_proporcao('AM', filtro_2018))
