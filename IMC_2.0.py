import os

def main():

    altura = input ("Altura:")
    peso = input ("Peso:")
    altcm = (float(altura)) / 100
    imc = (float(peso)) / (((float(altcm)) * ((float(altcm)))))
    clear = lambda: os.system('cls')

    if imc < 18.5:
        input ("Seu IMC é " + str(imc)[:4] + " e você está abaixo do peso")
        clear()
        main()

    if imc <= 24.9:
        input ("Seu IMC é " + str(imc)[:4] + " e você está no peso normal")
        clear()
        main() 

    if imc <=29.9:
        input ("Seu IMC é " + str(imc)[:4] + " e você está sobrepeso")
        clear()
        main() 

    if imc <= 34.9:
        input ("Seu IMC é " + str(imc)[:4] + " e você está com obesidade grau 1")
        clear()
        main() 

    if imc <= 39.9:
        input ("Seu IMC é " + str(imc)[:4] + " e você está com obesidade grau 2")
        clear()
        main()

    if imc > 40.0 :
        input ("Seu IMC é " + str(imc)[:4] + " e você está com obesidade grau 3")
        clear()
        main()

main()
