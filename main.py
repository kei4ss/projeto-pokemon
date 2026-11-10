import pyttsx3
import random
import requests
import ascii

def getRandomPokemon():
    data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{random.randint(1, 1000)}").json()
    return data['name']

def falar(texto, rate=200, volume=0.9, voice=0):
    motor = pyttsx3.init()

    motor.setProperty('rate', rate)
    motor.setProperty('volume', volume)
    voices = motor.getProperty('voices')
    motor.setProperty('voice', voices[voice].id)

    motor.say(texto)
    motor.runAndWait()
    motor.stop()

def fale_exiba(texto, rate=200, volume=0.9, voice=0, br="\n"):
    print(texto, end=br)
    falar(texto, rate, volume, voice)


textos = {
    "boas-vindas": "Bem-vindo ao mundo Pokémon! Prepare-se para uma aventura incrível!",
    "descricao": "Neste mundo, você encontrará criaturas fascinantes chamadas Pokémon. Cada Pokémon possui habilidades únicas e características especiais.",
    "saida": "Obrigado por visitar o mundo Pokémon! Até a próxima aventura!",
    "lancar_pokebola": "Você lançou uma Pokébola no mato alto e encontrou um Pokémon!",
    "opcao_invalida": "Opção inválida. Por favor, escolha uma opção válida."
}

print("""
_______  _______  _        _______  _______  _______  _       
(  ____ )(  ___  )| \    /\(  ____ \(       )(  ___  )( (    /|
| (    )|| (   ) ||  \  / /| (    \/| () () || (   ) ||  \  ( |
| (____)|| |   | ||  (_/ / | (__    | || || || |   | ||   \ | |
|  _____)| |   | ||   _ (  |  __)   | |(_)| || |   | || (\ \) |
| (      | |   | ||  ( \ \ | (      | |   | || |   | || | \   |
| )      | (___) ||  /  \ \| (____/\| )   ( || (___) || )  \  |
|/       (_______)|_/    \/(_______/|/     \|(_______)|/    )_)
""")
print("-" * 50)
fale_exiba(textos["boas-vindas"])
fale_exiba(textos["descricao"])

while True:
    print("\nEscolha uma opção:")
    print("1. Lançar pokebola no mato alto")
    print("2. Sair")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        nome_pokemon = getRandomPokemon()
        print(ascii.pokebola)
        fale_exiba(f"Você vê um {nome_pokemon} selvagem!")
        fale_exiba("Você deseja capturá-lo?", br=" ")
        print("(s/n)")
        r = input().lower()
        if r == "s":
            resultado = random.choice(["capturado", "fugiu"])
            if resultado == "capturado":
                fale_exiba(f"Parabéns! Você capturou o {nome_pokemon}!")
            else:
                fale_exiba(f"Oh não! O {nome_pokemon} fugiu!")
        else:
            fale_exiba(f"Você decidiu não capturar o {nome_pokemon}.")

    elif opcao == "2":
        fale_exiba(textos["saida"])
        break
    else:
        fale_exiba(textos["opcao_invalida"])
