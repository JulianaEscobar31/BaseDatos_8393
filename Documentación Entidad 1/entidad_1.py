#Entidad 1

##Librerías

#Se utilizarán las siguientes librerías para crear los datos sintéticos

import pandas as pd
import uuid
import random
from faker import Faker
import datetime

#El número de datos sintéticos que se crearán son de 5000 datos

num_users = 5000

#La entidad de las que vamos a crear los datos sería "jugadores".
#Se utilizará los siguientes atributos para esta entidad:

#   ID (id)
#   Nombre del jugador (name)
#   Email del jugador (email)
#   Fecha de nacimiento del jugador (dob)
#   Género del jugador (gender): este atributo se lo añadió para poder crear los nombres sintéticos y los emails."""

features = [
    "id",
    "name",
    "email",
    "dob",
    "gender"
]# Creating a DF for these features
df = pd.DataFrame(columns=features)

#Creación de datos
# IDs

df['id'] = [uuid.uuid4().hex for i in range(num_users)]

#UUID es una gran biblioteca para generar identificaciones únicas para cada usuario debido a su posibilidad
#astronómicamente baja de duplicar una identificación.** Es una gran opción cuando se trata de generar conjuntos 
# de caracteres de identificación únicos. Pero, si desea asegurarse de que no se repitieron las ID, puede realizar 
# una verificación simple en el marco de datos con lo siguiente:

print(df['id'].nunique()==num_users)

#Esto devolverá True si todas las ID en el conjunto de datos son únicas.

#Gender
#Este atributo es uno de los casos en los que probablemente no se debería utilizar una elección igualmente aleatoria. 
# Porque se puede suponer con seguridad que cada elección no tiene la misma probabilidad de ocurrir.
#Para el género solamente se proporcionó el género masculino, ya que todos los jugadores de la copa de mundo son 
# hombres. Se lo añadió más que todo para poder crear los nombres y los emails de los jugadores.

genders = ["male"]

df['gender'] = random.choices(
    genders,  
    k=num_users
)

#Nombre
#Se utiliza la biblioteca Faker para crear miles de nombres para todos estos usuarios.

faker = Faker()

def name_gen(gender):
    """Quickly generates a name based on gender"""

    if gender=='male':
        return faker.name_male()
    
    return faker.name()# Generating names for each user
df['name'] = [name_gen(i) for i in df['gender']]

#Email
# Primero, se crea una nueva función que daría formato a los nombres en direcciones de correo electrónico con un 
# nombre de dominio predeterminado. También se maneja las direcciones duplicadas simplemente agregando un número 
# aleatorio al final del nombre formateado:

def emailGen(name, duplicateFound=False):
    """
    Generates a random email address based on the given name. 
    Adds a number at the end if a duplicate address was found.
    """
    # Fake domain name to use
    dom = "@fakemail.com"
    
    # Lowercasing and splitting
    name = name.lower().split(" ")
    
    # Random character to insert in the name
    chars = [".", "_"]
    
    new_name = name[0] + random.choice(chars) + name[1] 
    
    # Further distinguishing the email if a duplicate was found
    if duplicateFound:
        
        # Random number to insert at the end
        num = random.randint(0,100)
        
        # Inserting at the end
        new_name = new_name + str(num)
        
    # Returning the email address with the domain name attached
    return new_name + dom

#Ahora, para aprovechar adecuadamente el propósito de esta función, se crea un ciclo que se vuelve a ejecutar la función cuando fuera necesario mientras iteraba a través del atributo "Nombre". El ciclo seguiría volviendo a ejecutar la función hasta que se creara un nombre de correo electrónico único."""

emails = []

for name in df['name']:
    
    # Generating the email
    email = emailGen(name)
    
    # Looping until a unique email is generated
    while email in emails:
        
        # Creating an email with a random number
        email = emailGen(name, duplicateFound=True)
    
    # Attaching the new email to the list
    emails.append(email)
    
df['email'] = emails

#Date of Birth

def random_dob(start, end, n):
    """
    Generating a list of a set number of timestamps
    """
    
    # The timestamp format
    frmt = "%Y-%m-%d"
    
    # Formatting the two time periods
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    
    # Creating the pool for random times
    td = etime - stime
    
    # Generating a list with the random times
    times = [(random.random() * td + stime).strftime(frmt) for _ in range(n)]
    
    return times

df['dob'] = random_dob("1980-01-01", "2006-01-01", num_users)

#Guardando la información
# Ahora que los datos están completos y si estaba codificando, siéntase libre de ver el marco de datos antes de 
# decidir guardarlo. Si todo se ve bien, guarde el marco de datos como un archivo .csv con este simple comando:

df.to_csv('dataset_entidad1.csv')