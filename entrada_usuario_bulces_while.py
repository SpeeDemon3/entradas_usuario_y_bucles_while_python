### Funcion input() ### Pausa el programa y espera a que el usuario introduzca un texto
# La funcion input() interpreta toda la informacion introducida por el usuario como una cadena

message = input('Hola introduce algo:')  # Muestro un mensaje por consola y guardo el valor introducido por el usuario
print('Texto introducido: ' + message)  # Imprimo el valor introducido por el usuario

### Funcion int() ### Copnvierte la representacion en cadena de un numero en representacion numerica
age = input('How old are you?')  # Muestro un mensaje al usuario y guardo el valor que introduce

age_int = int(age)  # Convierto el valor introducido a valor numerico

if age_int >= 18:  # Si el valor numerico es mayor o igual a 18
    print('Hello!!!')
else:  # Si es menor a 18
    print('Bye...')

### Comprobar si un numero es par o impar utilizando el operador modulo %
user_number = input('\tEnter a number:')  # Guardo el valor introducido

user_number_int = int(user_number)  # Convierto el valor de cadena a numerico

if user_number_int % 2 == 0:  # Si el valor introducido dividido entre 2 tiene un resto de 0, el valor sera par
    print(f'The number {user_number_int} is even.')
else:  # Si no, sera impar
    print(f'The number {user_number_int} is pdd.')

### Coche de alquiler
car = input('What car do you want?')

print(f"Let's see if we have a {car.title()}...")

### Mesa en un restaurante
question = input('How many come to dinner?')

question_int = int(question)

if question_int > 8:  # Si son mas de 8 personas
    print('You have to wait....')
else:  # Si no
    print('Ok, you table is ready!!!')

### Multiplos de 10
number_user = input('Enter a number:\n')

number_user_int = int(number_user)

if number_user_int % 2 == 0:
    print(f'The number {number_user_int} is a multiple of ten.')
else:
    print(f'The number {number_user_int} is not a multiple of ten.')

### Bucle while se ejecuta mientras se cumpla una condicion ###

current_number = 0

while current_number <= 10:
    print(current_number)
    current_number += 1  # Suma uno a la variable en cada iteracion para no provocar un bucle infinito

# Pizza
active = True
while active:
    promp = input('Introduce a new ingredient:\n'
                  'Enter quit to exit.\n')

    if promp.lower() == 'quit':  # Si el usuario intruduce quit
        break;  # Utilizando la sentencia break salimos del bucle
    else:  # Si no, añadimos el ingrediente
        print('A new ingredient has been added.')

# Entradas de cine
exit_number = 0
while exit_number <= 5:
    age = input('Introduce your age:')  # Guardo el valor introducido

    age_int = int(age)  # Lo convierto a valor numerico

    if age_int < 3:  # Compruebo si es menor a 3
        print('Your ticket is free.')
    elif age_int <= 12:  # Compruebo si es menor o igual a 12
        print('Your ticket costs 8€.')
    else:
        print('Your ticket cost 12€.')

    exit_number += 1  # Sumo 1 a la variable en cada iteracion para no crear un bucle infinito

### Usar un bucle while con listas y diccionarios ###
unconfirmed_user = ['user_1', 'user_2', 'user_3']  # Lista de usuarios sin confirmar
confirmed_user = []  # Lista vacia donde se guardaran los usuarios confirmados

# Verificar cada usuario hasta que ya no hay usuarios sin confirmar
# Mueve a cada usuario verificado a la lista de usuarios confirmados
while unconfirmed_user:  # Mientras la lista no este vacia el bucle seguira iterando
    current_user = unconfirmed_user.pop()  # Con el metodo pop() voy eliminando cada usuario de la lista empezando por el final

    print(f"Verifying user: {current_user.title()}")
    confirmed_user.append(current_user)  # Añado cada usuario a la nueva lista

# Mostrar todos los usuario confirmados
for user in confirmed_user:
    print(f"New confirmed user {user}.")

# Eliminar todos los casos de valores especificados de una lista
numbers = [1, 2, 3, 3, 3, 9]  # Lista de numeros con el numero 3 repetido 3 veces
print(numbers)

while 3 in numbers:  # Bucle while para buscar todos los numeros 3 dentro de la lista, el bucle se seguira ejecutando mientras el numero 3 este en la lista
    numbers.remove(3)  # Con la funcion remove() voy eliminando todos los elementos con el valor 3

print(numbers)  # Imprimo la lista, en la que ya no estara ningun valor 3

### Rellenar un diccionario con entradas de usuario
responses = {}

# Configuro una vandera para activar el bucle while
survey_active = True

while survey_active:
    name = input('\tWhat is your name?')  # Pido y guardo el nombre del usuario mostrandole un mensaje
    response = input('\t Where do you from?')  # Pido de donde es y lo guardo

    responses[name] = response  # Guardo la respuesta en el diccionario

    # Compruebo si hay que realizar una nueva encuesta
    repeat = input("\tYou want to make a new survey?")

    if repeat.lower() == 'no':  # Compruebo si la respuesta del usuario es no, de ser asi
        survey_active = False  # Combio el valor de la bandera a False
        print("Bye, bye...")

print("###\tSurvey complete###")  # Muestto todas las encuestas
for name, response in responses.items():
    print(f"Hi {name} from {response}")

# Concesionario
# Creo una lista con el pedido de coches
ordered_cars = ["Audi tt quattro", "Seat Leon Cupra 300", "Audi a5", "Seat Leon Cupra 300", "BMW m3", "Ford focus st",
                "Seat Leon Cupra 300"]
print(ordered_cars)

# Creo una lista vacia donde estaran los coches entregados
cars_delivered = []

# Informo de que no quedan "Seat Leon Cupra 300"
print("There are no Seat Leon Cupra 300")
# Con un bucle while recorro la lista mientra exista el elemento "Seat Leon Cupra 300"
while "Seat Leon Cupra 300" in ordered_cars:
    ordered_cars.remove("Seat Leon Cupra 300") # Con el metodo remove() elimino el elemento

while ordered_cars:
    car_delivere = ordered_cars.pop()  # Guardo y elimino cada coche

    cars_delivered.append(car_delivere)  # Añado un nuevo coche a la lista de coches entregados

print(cars_delivered)  # Imprimo la nueva lista

# Videojuegos
# Creo un diccionario para guardar las respuestas
responses_games = {}

control = True

while control:
    player = input('Introduce your name:')
    response = input('What is your favorite game?:')

    responses_games[player] = response

    again = input('any more?'
                  '\n yes or no?')

    if again.lower() == 'no':
        control = False

print('Your favorite games are:')

for player, game in responses_games.items():
    print(f'{player} ==> {game}')