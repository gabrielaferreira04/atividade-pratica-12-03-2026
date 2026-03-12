renda = int(input("Informe sua renda:  "))
score = int(input("Qual seu score? "))
fiador = input("Você tem um fiador com score 700? (sim/não)")

if renda >=2000 and (score >600 or fiador == "sim"):
    print ("Emprestimo liberado")
else:
    print("tente outro banco")