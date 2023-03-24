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
if circunferenciaCintura <0:
    circunferenciaCintura = float(input("Informe uma circunferencia positiva: "))


def  densidadeCorporal():
    dc = 1.0970 - (0.00046971 *(dobraCutaneaTricipital + dobraCutaneaSupraIliaca + dobraCutaneaCoxa +
                                dobraCutaneaAbdomen + dobraCutaneaPeitoral + dobraCutaneaSubescapular +
                                dobraCutaneaAxilarMedia)) + (0.00000056 *(dobraCutaneaTricipital + 
                                dobraCutaneaSupraIliaca + dobraCutaneaCoxa + dobraCutaneaAbdomen + 
                                dobraCutaneaPeitoral + dobraCutaneaSubescapular +dobraCutaneaAxilarMedia)**2 - (0.00012828 * idade))
    return (dc)


def percentualGordura():
    pc =((4.95/densidadeCorporal)- 4.50) * 100
    return(pc)

def massaGorda():
    mg = (massaCorporal * percentualGordura) / 100
    return(mg)

def massaIsentaGordura():
    mig = massaCorporal - massaGorda
    return(mig)


print("Densidade corporal: ", densidadeCorporal())
print("Percentual de gordura: ", percentualGordura())
