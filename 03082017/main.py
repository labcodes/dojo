def n_erdos(lista_de_artigos):
    ret = {}

    autores_com_erdos = []
    for artigo in lista_de_artigos:
        if 'P. Erdos' in artigo:
            for autor in artigo[1:]:
                ret.update({autor: 1})
                autores_com_erdos.append(autor)
        else:
            foi_com_erdos = False
            for autor in artigo:
                if autor in autores_com_erdos:
                    foi_com_erdos = True

            if foi_com_erdos:
                for autor in artigo:
                    if autor not in autores_com_erdos:
                        ret.update({autor: 2})
            else:
                for autor in artigo:
                    ret.update({autor: 'infinito'})

    return ret
