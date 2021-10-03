import io

import folium
import pandas as pd
from folium.plugins import MarkerCluster

import data_storage
import strategy_handler


def SpatialData(nivel):
    dados = data_storage.Localizacao()
    df = pd.read_csv(io.StringIO(dados))
    mapa = folium.Map(location=df[["Lat", "Lon"]].mean().to_list(), zoom_start=5, control_scale=True, max_bounds=True)
    marker_cluster = MarkerCluster().add_to(mapa)
    r = df.loc[0]
    coordenadas = strategy_handler.SelecionaNivelLocalizacao(nivel, r, marker_cluster)

    mapa.save("mapa.html")
    return coordenadas

def TemporalData(nivel):
    tempo = data_storage.Temporal()
    return strategy_handler.SelecionaNivelTemporal(nivel, tempo)


def IdentityData(nivel):
    identidade = data_storage.Identidade()
    return strategy_handler.SelecionaNivelIdentidade(nivel, identidade)


def ActivityData(nivel):
    atividade = data_storage.Atividade()
    return strategy_handler.SelecionaNivelAtividade(nivel, atividade)
