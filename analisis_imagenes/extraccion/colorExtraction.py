import extcolors
from webcolors import *
def dameColor(c):
    if c > 16725558 and c <= 16752950:
        return("NaranjaI")
    elif (c > 16752950 and c<=16766780):
        return("NaranjaII")
    elif (c>16766780 and c<=16775484):
        return("NaranjaIII")
    elif (c>16775484 and c<=16187190):
        return("Amarillo")
    elif (c>3406945 and c<=11534131):
        return("Verde")
    elif(c>3407000 and c<=8453939):
        return("Optimo")
    else:
        return("Irrelevante")
#3406945 -> Verde intenso
#16739891 ->A anaranjado intenso
#16758067 ->A anaranjado medio
#16766771 ->A anaranjado pálido
#16187187 -> amarillo clarito
#13958963 -> verde
#8453939 -> verde intenso
#3407695 -> óptimo
listaDatos = []
colors, pixel_count = extcolors.extract_from_path("imagenes_lotes\\lote-6.png")
#print(pixel_count)
#print("Colores:")
#print(colors)
f = open("analisisColores.csv", "w+")
f.write("id,lote,tamanio,pixelescolor,color,rangocolor\n")
for i in range(1,7):
    colors, pixel_count = extcolors.extract_from_path("imagenes_lotes\\lote-"+str(i)+".png")
    aux = []
    aux.append(colors)
    aux.append(pixel_count)
    listaDatos.append(aux)
    
for i, datos in enumerate(listaDatos):
    cadenaO = ""
    cadenaO = cadenaO+(str(i+1))+",lote"+str(i+1)+"," #1,lote1
    #f.write("Imagen Lote "+ str(i+1)+"\n")
    totalPix = listaDatos[i][1]
    pixelsTrabajo = 0
    datosX = listaDatos[i][0]
    pixelesUsados = [datosX[i][1] for i in range(len(datosX))]
    pixelesUsados = sum(pixelesUsados)
    cadenaO = cadenaO+str(pixelesUsados)
    #f.write("Total de píxeles: "+ str(totalPix)+"\n")
    #f.write("Total de píxeles trabajo: "+ str(pixelesUsados)+"\n")
    #print("Datos de colores:")
    cadaux = cadenaO
    for datosColor in datosX:
        cadenaO = cadaux
        porc = str((100)*round((datosColor[1]/pixelesUsados),3))
        colorHexa = rgb_to_hex(datosColor[0])
        colorDec = int(colorHexa[1:], 16)
        #colorHexa = colorDec
        cadenaO = cadenaO+","+str(datosColor[1])+","+str(colorHexa)
        cadenaO = cadenaO+","+dameColor(colorDec)+"\n"
        #f.write("Color: "+ colorHexa +" |  Píxeles: "+ str(datosColor[1])+ " | Porcentaje: "+porc )
        #f.write("\n")
        f.write(cadenaO)
        #print(cadenaO)

f.close()
    
    