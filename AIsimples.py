import numpy as np

# Conjunto de perguntas e respostas
perguntas = [
    {
        "pergunta": "O animal é mamífero? ",
        "respostas": {
            "sim": np.array([0.8, 0.1, 0.1]),  # Probabilidades: mamífero, ave, réptil
            "não": np.array([0.1, 0.4, 0.5])
        }
    },
    {
        "pergunta": "O animal tem asas? ",
        "respostas": {
            "sim": np.array([0.1, 0.7, 0.2]),
            "não": np.array([0.6, 0.2, 0.2])
        }
    },
    {
        "pergunta": "O animal rasteja? ",
        "respostas": {
            "sim": np.array([0.1, 0.1, 0.8]),
            "não": np.array([0.4, 0.6, 0.1])
        }
    }
]

# Função para obter a resposta do usuário
def obter_resposta(pergunta):
    resposta = input(pergunta + "(sim/não): ").lower()
    while resposta not in ["sim", "não"]:
        resposta = input("Por favor, responda com 'sim' ou 'não': ").lower()
    return resposta

# Função para realizar a adivinhação do animal
def adivinhar_animal():
    probabilidades = np.array([0.33, 0.33, 0.33])  # Probabilidades iniciais igualmente distribuídas

    for pergunta in perguntas:
        resposta = obter_resposta(pergunta["pergunta"])
        probabilidades *= pergunta["respostas"][resposta]

    indice_animal = np.argmax(probabilidades)  # Encontrar o índice da maior probabilidade
    animais = ["mamífero", "ave", "réptil"]
    animal_adivinhado = animais[indice_animal]

    print("Eu acho que o animal é um(a):", animal_adivinhado)

# Executar adivinhação do animal
adivinhar_animal()
