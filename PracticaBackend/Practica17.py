from io import open


listaNombres = ["ivan","juan","carlos","santiago","maxi","santi","tiago","martin","marcos"]

fichero = open('nombres.txt', 'w')
for i in listaNombres:
    fichero.write(i+"\n")
    


fichero.close()