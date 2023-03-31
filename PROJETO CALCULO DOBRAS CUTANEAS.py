import math

sexo = input("Informe o seu gênero (F para feminino e M para masculino): ")
while sexo.lower() not in ["f", "m"]:
    sexo = input("Opção inválida. Por favor, informe F para feminino ou M para masculino: ")

idade = int(input("Informe sua idade: "))
if idade <=0:
    idade = int(input("Idade inválida! Informe uma idade positiva: "))

altura = float(input("Informe sua altura: "))
if altura <=0 : 
    altura = float(input("Altura inválida! Informe um valor positivo: "))

massaCorporal = float(input("Informe seu peso corporal: "))
if massaCorporal <=0:
    massaCorporal = float(input("Peso corporal inválido! Informe um valor positivo: "))

dobraCutaneaPeitoral = float(input("Informe a dobra cutanea do peitoral: "))
if dobraCutaneaPeitoral <1 :
    dobraCutaneaPeitoral = float(input("Informe um valor positivo! "))

dobraCutaneaAbdomen = float(input("Informe a dobra cutanea do abdômen: "))
if dobraCutaneaAbdomen <1 :
    dobraCutaneaAbdomen = float(input("Informe um valor positivo! "))

dobraCutaneaTricipital = float(input("Informe a dobra cutanea do tríceps: "))
if dobraCutaneaTricipital <1 :
    dobraCutaneaPeitoral = float(input("Informe um valor positivo! "))

dobraCutaneaCoxa = float(input("Informe a dobra cutanea da coxa: "))
if dobraCutaneaCoxa <1 :
    dobraCutaneaCoxa = float(input("Informe um valor positivo! "))

dobraCutaneaSupraIliaca = float(input("Informe a dobra cutanea do suprailiaca]: "))
if dobraCutaneaSupraIliaca <1 :
    dobraCutaneaSupraIliaca = float(input("Informe um valor positivo! "))

dobraCutaneaAxilarMedia = float(input("Informe a dobra cutanea da axilar média: "))
if dobraCutaneaAxilarMedia <1 :
    dobraCutaneaAxilarMedia = float(input("Informe um valor positivo! "))

dobraCutaneaSubescapular = float(input("Informe a dobra cutanea subescapular: "))
if dobraCutaneaSubescapular <1 :
    dobraCutaneaSubescapular = float(input("Informe um valor o positivo! "))

circunferenciaCintura = float(input("Informe sua circunferencia da cintura: "))
if circunferenciaCintura <=0:
    circunferenciaCintura = float(input("Informe uma circunferencia positiva: "))


def  densidadeCorporal():
    dc = 1.0970 - (0.00046971 *(dobraCutaneaTricipital + dobraCutaneaSupraIliaca + dobraCutaneaCoxa +
                                dobraCutaneaAbdomen + dobraCutaneaPeitoral + dobraCutaneaSubescapular +
                                dobraCutaneaAxilarMedia)) + (0.00000056 *(dobraCutaneaTricipital + 
                                dobraCutaneaSupraIliaca + dobraCutaneaCoxa + dobraCutaneaAbdomen + 
                                dobraCutaneaPeitoral + dobraCutaneaSubescapular +dobraCutaneaAxilarMedia)**2 - (0.00012828 * idade))
    return (dc)


def densidadeCorporalMasculino():
    dc = 1.1120 - (0.00042499 (dobraCutaneaTricipital + dobraCutaneaSupraIliaca + dobraCutaneaCoxa +
                                dobraCutaneaAbdomen + dobraCutaneaPeitoral + dobraCutaneaSubescapular +
                                dobraCutaneaAxilarMedia)) + (0.00000055 *(dobraCutaneaTricipital + 
                                dobraCutaneaSupraIliaca + dobraCutaneaCoxa + dobraCutaneaAbdomen + 
                                dobraCutaneaPeitoral + dobraCutaneaSubescapular +dobraCutaneaAxilarMedia)**2 - (0.00028826 * idade))
    return (dc)


# Densidade corporal recebe formula feminina ou masculino
if sexo == "F" or sexo == "f":
    densidadeCorporal = True
else:
    densidadeCorporal = densidadeCorporalMasculino


def percentualGordura():
    pc =((4.95/densidadeCorporal)- 4.50) * 100
    return(pc)


def massaGorda():
    mg = (massaCorporal * percentualGordura) / 100
    return(mg)


def massaIsentaGordura():
    mig = massaCorporal - massaGorda
    return(mig)

densidadeCorporal(dobraCutaneaTricipital, dobraCutaneaSupraIliaca, dobraCutaneaCoxa, dobraCutaneaAbdomen,
                  dobraCutaneaPeitoral, dobraCutaneaSubescapular, dobraCutaneaAxilarMedia)

densidadeCorporalMasculino(dobraCutaneaTricipital, dobraCutaneaSupraIliaca, dobraCutaneaCoxa, dobraCutaneaAbdomen,
                          dobraCutaneaPeitoral, dobraCutaneaSubescapular, dobraCutaneaAxilarMedia)

percentualGordura(densidadeCorporal)

massaGorda(massaCorporal, percentualGordura)

massaIsentaGordura(massaCorporal, massaGorda)

if sexo == "F" or sexo == "f":
    print(f"Densidade corporal: {densidadeCorporal:.2f}")
else:
    print(f"Densidade corporal masculina: {densidadeCorporalMasculino:.2f}")
print(f"Percentual de gordura: {percentualGordura:.2f},%")
print(f"Massa Gorda: {massaGorda:.2f}")
print(f"Massa Isenta de Gordura: {massaIsentaGordura:.2f}")


if sexo =="M" or sexo =="m":
    if idade >5 and idade<17:
        if percentualGordura <= 5:
            print("Percentual de gordura não recomendado.")
        elif percentualGordura >5 and percentualGordura <=11:
            print("Percentual de gordura baixo.")
        elif percentualGordura >11 and percentualGordura <=25:
            print("Percentual de gordura médio.")
        elif percentualGordura >26 and percentualGordura <=31:
            print("Percentual de gordura alto.")
        else:
            print("Você está obeso.")

    elif idade >=18 and idade<=34:
        if percentualGordura <8:
            print("Percentual de gordura não recomendado.")
        elif percentualGordura >=8 and percentualGordura <13:
            print("Percentual de gordura baixo.")
        elif percentualGordura >=13 and percentualGordura <21:
            print("Percentual de gordura médio.")
        elif percentualGordura >=21 and percentualGordura <=22:
            print("Percentual de gordura alto.")
        else:
            print("Você está obeso.")

    elif idade >=35 and idade<=55:
        if percentualGordura <10:
            print("Percentual de gordura não recomendado.")
        elif percentualGordura ==10:
            print("Percentual de gordura baixo.")
        elif percentualGordura >10 and percentualGordura <18:
            print("Percentual de gordura médio.")
        elif percentualGordura >=18 and percentualGordura <=25:
            print("Percentual de gordura alto.")
        else:
            print("Você está obeso.")

    if idade >55:
        if percentualGordura <10:
            print("Percentual de gordura não recomendado.")
        elif percentualGordura ==10:
            print("Percentual de gordura baixo.")
        elif percentualGordura >10 and percentualGordura <16:
            print("Percentual de gordura médio.")
        elif percentualGordura >=16 and percentualGordura <=23:
            print("Percentual de gordura alto.")
        else:
            print("Você está obeso.")

    else:
        if idade >5 and idade <17:
            if percentualGordura <=12:
                print("Percentual de gordura não recomendado.")
            elif percentualGordura >12 and percentualGordura <=15:
                print("Percentual de gordura baixo.")
            elif percentualGordura >15 and percentualGordura <=30:
                print("Percentual de gordura médio.")
            elif percentualGordura >30 and percentualGordura <=36:
                print("Percentual de gordura alto.")
            else:
                print("Você está obeso.")
        
        elif idade >=18 and idade <34:
            if percentualGordura <=20:
                print("Percentual de gordura não recomendado.")
            elif percentualGordura ==20:
                print("Percentual de gordura baixo.")
            elif percentualGordura >20 and percentualGordura <=28:
                print("Percentual de gordura médio.")
            elif percentualGordura >28 and percentualGordura <=35:
                print("Percentual de gordura alto.")
            else:
                print("Você está obeso.")

        elif idade >=35 and idade <55:
            if percentualGordura <=25:
                print("Percentual de gordura não recomendado.")
            elif percentualGordura ==25:
                print("Percentual de gordura baixo.")
            elif percentualGordura >25 and percentualGordura <=32:
                print("Percentual de gordura médio.")
            elif percentualGordura >32 and percentualGordura <=38:
                print("Percentual de gordura alto.")
            else:
                print("Você está obeso.")

        else: 
            if idade >55:
                if percentualGordura <=25:
                   print("Percentual de gordura não recomendado.")
                elif percentualGordura ==25:
                    print("Percentual de gordura baixo.")
                elif percentualGordura >25 and percentualGordura <=30:
                    print("Percentual de gordura médio.")
                elif percentualGordura >30 and percentualGordura <=35:
                    print("Percentual de gordura alto.")
                else:
                    print("Você está obeso.")

def taxaMetabolismoBasal():
    tmb = 60.9 * massaCorporal - 54
    return tmb

def gastoCalorico():
    gc = 