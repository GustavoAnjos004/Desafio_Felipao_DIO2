nome = input("Qual o seu nome: ")
xp = None 
nivel = ""

while xp is None:
    try:
        xp = int(input("Qual o seu nivel (digite um número): "))
    except ValueError:
        print("Por favor, digite um número válido.")

if xp <= 1000:
    nivel = "Ferro"
elif 1001 <= xp <= 2000:
    nivel = "Bronze"
elif 2001 <= xp <= 6000:
    nivel = "Prata"
elif 6001 <= xp <= 7000:
    nivel = "Ouro"
elif 7001 <= xp <= 8000:
    nivel = "Platina"
elif 8001 <= xp <= 9000:
    nivel = "Ascendente"
elif 9001 <= xp <= 10000:
    nivel = "Imortal"
elif xp >= 10001:
    nivel = "Radiante"

print("Olá {}, seus equipamentos são de nível {}.".format(nome, nivel))