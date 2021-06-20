# https://www.youtube.com/watch?v=qbLc5a9jdXo&ab_channel=CalebCurryCalebCurry
# DESDE LOS 28 MINUTUTOS EMPIEZA EL DESARROLLO DE LA REST API
# REST API CLIENT DE BEBIDAS

import requests

print('''
Listar - Listado de bebidas
Consultar - consulta una bebida
Borrar - Borra una bebida (id)
Cargar - Cargo una bebida
Salir - Sale de la app
        ''')

while True:
    option = input('> ').lower()
    if option == 'listar':
        print(requests.get('http://127.0.0.1:5000/api/drinks').text)
    elif option == 'cargar':
        beverage_name = input('Bebida: ')
        beverage_descr = input('Descripcion: ')

        response = requests.post('http://127.0.0.1:5000/api/drinks', json={"name" : beverage_name, "description" : beverage_descr})
        print(response.text)
    elif option == 'borrar':
        response = requests.get('http://127.0.0.1:5000/api/drinks')
        print(response.text)
        id = int(input("id: "))
        print(requests.delete(f'http://127.0.0.1:5000/api/drinks/{id}').text)
        print(requests.get('http://127.0.0.1:5000/api/drinks').text)
    elif option == 'consultar':
        print(requests.get('http://127.0.0.1:5000/api/drinks').text)
        id = int(input("id: "))
        print(requests.get(f'http://127.0.0.1:5000/api/drinks/{id}').text)
    elif option == 'ayuda':
        print('''
        Listar - Listado de bebidas
        Consultar - consulta una bebida
        Borrar - Borra una bebida (id)
        Cargar - Cargo una bebida
        Salir - Sale de la app
                ''')
    elif option == 'salir':
        break
    else:
        print('Option no disponible')
        print('''
Listar - Listado de bebidas
Consultar - consulta una bebida
Borrar - Borra una bebida (id)
Cargar - Cargo una bebida
Salir - Sale de la app''')
    
    

# POST CARGAR UNA BEBIDA, NO REPETIR NOMBRES PORQUE EL "name" es "unique" y si ya existe no funciona
'''beverage_name = input('Bebida: ')
beverage_descr = input('Descripcion: ')

response = requests.post('http://127.0.0.1:5000/api/drinks', json={"name" : beverage_name, "description" : beverage_descr})
print(response.text)'''

# PARA BORRAR UNA BEBIDA

'''response = requests.get('http://127.0.0.1:5000/api/drinks')
print(response.text)

id = int(input("id: "))
print(requests.delete(f'http://127.0.0.1:5000/api/drinks/{id}').text)
print(requests.get('http://127.0.0.1:5000/api/drinks').text)'''
