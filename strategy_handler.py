import random
from random import uniform

import folium


def SelecionaNivelLocalizacao(nivel, r, marker):
    if nivel == 'Nível 0':
        mapa = folium.Map(location=None, zoom_start=15)
        return f"Espaço: Dados Indisponíveis"
    elif nivel == 'Nível 1':
        location = (r['Lat'], r['Lon'])
        folium.vector_layers.Circle(
            location=location,
            popup=r['nome'],
            tooltip=r['nome'],
            radius=1000
        ).add_to(marker)
        valor = 0.0060
        return f"Espaço: Latitute:{r['Lat'] - random.uniform(-valor, valor)} Longitude:{r['Lon'] + random.uniform(-valor, valor)}"

    elif nivel == 'Nível 2':
        x, y = uniform(-90, 90), uniform(-45, 45)
        location = (x, y)
        folium.vector_layers.Circle(
            location=location,
            popup=r['nome'],
            tooltip=r['nome'],
            radius=2
        ).add_to(marker)
        return f"Espaço: Latitute:{x} Longitude:{y}"

    elif nivel == 'Nível 3':
        location = (r["Lat"], r["Lon"])
        lat_max = -29.7190
        lat_min = -29.7160
        lon_max = -52.4273
        lon_min = -52.4243
        valida_dentro_zona = True if lat_min >= r['Lat'] >= lat_max and lon_min >= r['Lon'] >= lon_max else False
        folium.vector_layers.Circle(
            location=location,
            popup=r['nome'],
            tooltip=r['nome'],
            radius=250 if valida_dentro_zona else 1
        ).add_to(marker)
        valor = 0.0015
        lat = r['Lat'] - random.uniform(-valor, valor)
        lon = r['Lon'] + random.uniform(-valor, valor)
        print(f"{lat} , {lon}")
        return f"Espaço: Latitute:{lat if valida_dentro_zona else r['Lat']} Longitude:{lon if valida_dentro_zona else r['Lon']}"


    elif nivel == 'Nível 4':
        location = (r["Lat"], r["Lon"])
        folium.vector_layers.Circle(
            location=location,
            popup=r['nome'],
            tooltip=r['nome'],
            radius=2
        ).add_to(marker)
        return f"Espaço: Latitute:{r['Lat']} Longitude:{r['Lon']}"


def SelecionaNivelTemporal(nivel, tempo):
    hora = f"{tempo.hour}:{tempo.minute}:{tempo.second}"
    if nivel == 'Nível 0':
        return "Temporal: Informação indisponível"
    elif nivel == 'Nível 1':
        return f"Temporal: {tempo.year} {tempo.month}"
    elif nivel == 'Nível 2':
        return f"Temporal: {tempo.year} {tempo.day}/{tempo.month}"
    elif nivel == 'Nível 3':
        return f"Temporal: {tempo.year} {tempo.day}/{tempo.month} {hora if tempo.day != 2 and tempo.day != 30 else ''}"
    elif nivel == 'Nível 4':
        return f"Temporal: {tempo.year} {tempo.day}/{tempo.month} {hora}"


def SelecionaNivelIdentidade(nivel, identidade):
    if nivel == 'Nível 0':
        return f"Identidade: Os dados do usuário estão indisponíveis"
    elif nivel == 'Nível 1':
        return f"Identidade:{identidade.get('sexo')} {identidade.get('idade')} {identidade.get('profissao')}"
    elif nivel == 'Nível 2':
        return f"Identidade: Antonio {identidade.get('idade')} {identidade.get('sexo')} {identidade.get('profissao')} {identidade.get('data_nascimento')}" \
               f" 51 987452165 {identidade.get('cidade')}"
    elif nivel == 'Nível 3':
        return f"Identidade: ALVARO IDERSTOB {identidade.get('idade')} {identidade.get('sexo')} {identidade.get('email')} " \
               f"{identidade.get('data_nascimento')} {identidade.get('cidade_nascimento')} {identidade.get('telefone')} {identidade.get('profissao')} " \
               f"{identidade.get('cidade')} {identidade.get('rua')} {identidade.get('numero')} {identidade.get('complemento')} "
    elif nivel == 'Nível 4':
        return f"Identidade:\nNome Completo:{identidade.get('nome')} {identidade.get('sobre_nome')}\nIdade:{identidade.get('idade')}\nSexo:{identidade.get('sexo')} \n" \
               f"Data de Nascimento:{identidade.get('data_nascimento')}\nCidade de Origem:{identidade.get('cidade_nascimento')}\nTelefone:{identidade.get('telefone')}\nEmail:{identidade.get('email')} " \
               f"\nProfissão:{identidade.get('profissao')}\nCidade:{identidade.get('cidade')}\nBairro:{identidade.get('bairro')}\nRua:{identidade.get('rua')}\nNúmero da Rua:{identidade.get('numero')}\n" \
               f"Complemento:{identidade.get('complemento')}"


def SelecionaNivelAtividade(nivel, atividade):
    if nivel == 'Nível 0':
        return "Atividade: Informação não disponível"
    elif nivel == 'Nível 1':
        return f"Atividade: {atividade.get('nivel1')}"
    elif nivel == 'Nível 2':
        return f"Atividade: {atividade.get('nivel2')}"
    elif nivel == 'Nível 3':
        return f"Atividade: {'Informação não disponível' if atividade.get('nivel3').find('UBER') else atividade.get('nivel3')}"
    elif nivel == 'Nível 4':
        return f"Atividade: {atividade.get('nivel4')}"
