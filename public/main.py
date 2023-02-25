#Represa Hidroituango
import random

#ENTRADAS

nivelDeAgua = random.uniform(0, 500)

#PROCESO:
if (nivelDeAgua >= 400):
    print(f"Melo pa' morir el nivel de agua es {nivelDeAgua}")
elif(nivelDeAgua >= 200 and nivelDeAgua < 400):
    print(f"Melo pa' seguir viviendo el nivel de agua es {nivelDeAgua}")
elif(nivelDeAgua < 200):
    print(f"Melo, melitiqui, remelo... El nivel de agua es {nivelDeAgua}")

'''
buscar en internet las fechas de inicio de las estaciones del año
digitar dia mes y año
'''