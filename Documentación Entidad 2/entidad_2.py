#Entidad 2

import pandas as pd
import uuid
import random
from faker import Faker
import datetime

#Size
#El tamaño del conjunto de datos será de 20 puntos de datos (puede hacer más, pero el procesamiento puede demorar más).
#  Asigné esta cantidad a una variable constante, que usé en todo momento:


num_users = 20

#Atributos***

#Elegí solamente 3 atributos:
# ID (id)
# Nombre del club(nameClub)
# Status (status)
# Fecha de creación (fechaCreacion)

#Ingresé lo anterior como una lista de características para inicializar un marco de datos de Pandas:

features = [
    "id",
    "nameClub",
    "status",
    "fechaCreacion"
]# Creating a DF for these features
df = pd.DataFrame(columns=features)

#Creación de datos
# Algunos atributos anteriores normalmente deberían contener datos desequilibrados. Se puede asumir con seguridad con 
# una investigación rápida, algunas opciones no estarán igualmente representadas. Para un conjunto de datos más 
# realista, estas tendencias deben reflejarse.

#IDs
# Para el atributo ID, utilicé la biblioteca uuid para generar una cadena aleatoria de caracteres 20 veces. Luego, 
# lo asigné al atributo ID en el marco de datos.

df['id'] = [uuid.uuid4().hex for i in range(num_users)]

print(df['id'].nunique()==num_users)

#Nombre del Club
# Primeramente se declarón los nombres de 20 clubes que son participes del programa de la FIFA

namesClubs = ['Real Madrid', 'Manchester United', 'FC Barcelona', 'Paris Saint-German', 'Atlético de Madrid', 'Union Berlin','Rosenborg BK', 'OGC Nice','Juventus', 'Chelsea', 'AS Roma', 'Sevilla','Villareal', 'Olympique Dortmund', 'Benfica', 'Napoli','FC Basel', 'Sporting CP Lisbon', 'Slavia Praha', 'Internazionale']

df['nameClub'] = random.choices(namesClubs, weights=(5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5), k=num_users)

#Estado del club

choice = [True, False]
df['status'] = random.choices(
    choice, 
    k=num_users
)

#Fecha

def randomtimes(start, end, n):
    """
    Generates random time stamps based on a given amount between two time periods.
    """
    # The timestamp format
    frmt = "%Y-%m-%d %H:%M:%S"
    
    # Formatting the two time periods
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    
    # Creating the pool for random times
    td = etime - stime
    
    # Generating a list with the random times
    times = [(random.random() * td + stime).strftime(frmt) for _ in range(n)]
    
    return times

# Setting the start and end times
start = "2021-08-01 00:00:00"

end = "2021-08-24 00:00:00"

df['fechaCreacion'] = randomtimes(start, end, num_users)

#Saving the Dataset**
# Ahora que los datos están completos y si estaba codificando, siéntase libre de ver el marco de datos antes de 
# decidir guardarlo. Si todo se ve bien, guarde el marco de datos como un archivo .csv con este simple comando:

df.to_csv('dataset_entidad2.csv')