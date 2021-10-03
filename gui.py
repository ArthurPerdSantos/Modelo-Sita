from tkinter import *
from data_provider import *

# Alunos
# Arthur Pereira dos Santos
# Luis Gustavo Barcelos
# Vinicius Santiago Dutra da Silva

# Disciplina
# Segurança em Tecnologia da Informação




root = Tk()
root.title("Trabalho 3 Segurança em TI")
root.geometry('1024x768')


def ColetaSelecoes():
    valor_temporal = value_inside_temporal.get()
    valor_espacial = value_inside_espacial.get()
    valor_identidade = value_inside_identidade.get()
    valor_atividade = value_inside_atividade.get()
    # passagem de dados entre data provider e a GUI
    espaco = SpatialData(valor_espacial)
    id = IdentityData(valor_identidade)
    tempo = TemporalData(valor_temporal)
    atividade = ActivityData(valor_atividade)

    # informações coletados de acordo com o nivel são mostradas na text box
    if espaco and id and tempo and atividade:
        texto.insert(END, f"DADOS USUARIO:\n"
                          f"{espaco}\n"
                          f"{atividade}\n"
                          f"{tempo}\n"
                          f"{id}\n"
                          f'\n')
    else:
        texto.insert(END, "É Necessário informar todos os campos acima\n\n")



options_list = ["Nível 0", "Nível 1", "Nível 2", "Nível 3", "Nível 4"]

# criações option menu
value_inside_espacial = StringVar()
value_inside_espacial.set("Espacial")
question_menu = OptionMenu(root, value_inside_espacial, *options_list)
question_menu.pack()


value_inside_atividade = StringVar()
value_inside_atividade.set("Atividade")
question_menu = OptionMenu(root, value_inside_atividade, *options_list)
question_menu.pack()


value_inside_temporal = StringVar(root)
value_inside_temporal.set("Temporal")
question_menu = OptionMenu(root, value_inside_temporal, *options_list)
question_menu.pack()


value_inside_identidade = StringVar()
value_inside_identidade.set("Identidade")
question_menu = OptionMenu(root, value_inside_identidade, *options_list)
question_menu.pack()

# criacao caixa de texto
texto = Text(root, height=25, width=300)
texto.pack()

# botao confirmar
confirmar = Button(root, text="confirmar", command=lambda: ColetaSelecoes())
confirmar.pack()

# botao para sair
sair = Button(root, text="Sair", command=root.quit)
sair.pack()


root.mainloop()
