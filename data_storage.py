import datetime

import geocoder as geocoder


def Localizacao():
    gps = geocoder.ip('me')
    dados = f"""nome,Lat,Lon
    Local atual,{gps.latlng[0]},{gps.latlng[1]}
    """

    return dados


def Identidade():
    identidade_usuario = {
        "email": "robertosilva@gmail.com",
        "nome": "Roberto",
        "sexo": "Masculino",
        "telefone": "51 997652475",
        "sobre_nome": "da Silva",
        "profissao": "Empresário",
        "data_nascimento": "22/06/1978",
        "idade": "43",
        "cidade": "Santa Cruz do Sul",
        "rua": "Rua Julho de Castilho",
        "bairro": "Centro",
        "numero": "425",
        "complemento": "Casa",
        "cidade_nascimento": "Encruzilhada do Sul",
    }

    return identidade_usuario


def Temporal():
    return datetime.datetime.now()


def Atividade():
    atividade = {

        "nivel1": "Utilizando um aplicativo de celular",
        "nivel2": "Esperando o motorista da UBER chegar, com destino a AFUBRA",
        "nivel3": "Esperando o motorista da UBER chegar, com destino a UNISC",
        "nivel4": "Esperando o motorista da UBER chegar, com destino a UNISC",
    }

    return atividade
