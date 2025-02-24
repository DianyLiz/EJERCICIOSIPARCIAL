import bcrypt  # libreria para encriptar contraseñas
from datetime import datetime # libreria para manejar fechas

import os
os.system('cls' if os.name == 'nt' else 'clear')


# Datos de los departamentos y municipios
departamentos_municipios = {
    '01': {
        'nombre': 'Atlántida',
        'municipios': {
            '01': 'La Ceiba',
            '02': 'El Porvenir',
            '03': 'Esparta',
            '04': 'Jutiapa',
            '05': 'La Masica',
            '06': 'San Francisco',
            '07': 'Tela',
            '08': 'Arizona'
        }
    },
    '02': {
        'nombre': 'Colón',
        'municipios': {
            '01': 'Trujillo',
            '02': 'Balfate',
            '03': 'Iriona',
            '04': 'Limón',
            '05': 'Sabá',
            '06': 'Santa Fe',
            '07': 'Santa Rosa de Aguán',
            '08': 'Sonaguera',
            '09': 'Tocoa',
            '10': 'Bonito Oriental'
        }
    },
    '03': {
        'nombre': 'Comayagua',
        'municipios': {
            '01': 'Comayagua',
            '02': 'Ajuterique',
            '03': 'El Rosario',
            '04': 'Esquías',
            '05': 'Humuya',
            '06': 'La Libertad',
            '07': 'Lamaní',
            '08': 'La Trinidad',
            '09': 'Lejamaní',
            '10': 'Meámbar',
            '11': 'Minas de Oro',
            '12': 'Ojos de Agua',
            '13': 'San Jerónimo',
            '14': 'San José de Comayagua',
            '15': 'San José del Potrero',
            '16': 'San Luis',
            '17': 'San Sebastián',
            '18': 'Siguatepeque',
            '19': 'Villa de San Antonio',
            '20': 'Las Lajas',
            '21': 'Taulabé'
        }
    },
    '04': {
        'nombre': 'Copán',
        'municipios': {
            '01': 'Santa Rosa de Copán',
            '02': 'Cabañas',
            '03': 'Concepción',
            '04': 'Copán Ruinas',
            '05': 'Corquín',
            '06': 'Cucuyagua',
            '07': 'Dolores',
            '08': 'Dulce Nombre',
            '09': 'El Paraíso',
            '10': 'Florida',
            '11': 'La Jigua',
            '12': 'La Unión',
            '13': 'Nueva Arcadia',
            '14': 'San Agustín',
            '15': 'San Antonio',
            '16': 'San Jerónimo',
            '17': 'San José',
            '18': 'San Juan de Opoa',
            '19': 'San Nicolás',
            '20': 'San Pedro',
            '21': 'Santa Rita',
            '22': 'Trinidad de Copán',
            '23': 'Veracruz'
        }
    },
    '05': {
        'nombre': 'Cortés',
        'municipios': {
            '01': 'San Pedro Sula',
            '02': 'Choloma',
            '03': 'Omoa',
            '04': 'Pimienta',
            '05': 'Potrerillos',
            '06': 'Puerto Cortés',
            '07': 'San Antonio de Cortés',
            '08': 'San Francisco de Yojoa',
            '09': 'San Manuel',
            '10': 'Santa Cruz de Yojoa',
            '11': 'Villanueva',
            '12': 'La Lima'
        }
    },
    '06': {
        'nombre': 'Choluteca',
        'municipios': {
            '01': 'Choluteca',
            '02': 'Apacilagua',
            '03': 'Concepción de María',
            '04': 'Duyure',
            '05': 'El Corpus',
            '06': 'El Triunfo',
            '07': 'Marcovia',
            '08': 'Morolica',
            '09': 'Namasigüe',
            '10': 'Orocuina',
            '11': 'Pespire',
            '12': 'San Antonio de Flores',
            '13': 'San Isidro',
            '14': 'San José',
            '15': 'San Marcos de Colón',
            '16': 'Santa Ana de Yusguare'
        }
    },
    '07': {
        'nombre': 'El Paraíso',
        'municipios': {
            '01': 'Yuscarán',
            '02': 'Alauca',
            '03': 'Danlí',
            '04': 'El Paraíso',
            '05': 'Güinope',
            '06': 'Jacaleapa',
            '07': 'Liure',
            '08': 'Morocelí',
            '09': 'Oropolí',
            '10': 'Potrerillos',
            '11': 'San Antonio de Flores',
            '12': 'San Lucas',
            '13': 'San Matías',
            '14': 'Soledad',
            '15': 'Teupasenti',
            '16': 'Texiguat',
            '17': 'Vado Ancho',
            '18': 'Yauyupe',
            '19': 'Trojes'
        }
    },
    '08': {
        'nombre': 'Francisco Morazán',
        'municipios': {
            '01': 'Distrito Central',
            '02': 'Alubarén',
            '03': 'Cedros',
            '04': 'Curarén',
            '05': 'El Porvenir',
            '06': 'Guaimaca',
            '07': 'La Libertad',
            '08': 'La Venta',
            '09': 'Lepaterique',
            '10': 'Maraita',
            '11': 'Marale',
            '12': 'Nueva Armenia',
            '13': 'Ojojona',
            '14': 'Orica',
            '15': 'Reitoca',
            '16': 'Sabanagrande',
            '17': 'San Antonio de Oriente',
            '18': 'San Buenaventura',
            '19': 'San Ignacio',
            '20': 'San Juan de Flores',
            '21': 'San Miguelito',
            '22': 'Santa Ana',
            '23': 'Santa Lucía',
            '24': 'Talanga',
            '25': 'Tatumbla',
            '26': 'Valle de Ángeles',
            '27': 'Villa de San Francisco',
            '28': 'Vallecillo'
        }
    },
    '09': {
        'nombre': 'Gracias a Dios',
        'municipios': {
            '01': 'Puerto Lempira',
            '02': 'Brus Laguna',
            '03': 'Ahuas',
            '04': 'Juan Francisco Bulnes',
            '05': 'Ramón Villeda Morales',
            '06': 'Wampusirpi'
        }
    },
    '10': {
        'nombre': 'Intibucá',
        'municipios': {
            '01': 'La Esperanza',
            '02': 'Camasca',
            '03': 'Colomoncagua',
            '04': 'Concepción',
            '05': 'Dolores',
            '06': 'Intibucá',
            '07': 'Jesús de Otoro',
            '08': 'Magdalena',
            '09': 'Masaguara',
            '10': 'San Antonio',
            '11': 'San Isidro',
            '12': 'San Juan',
            '13': 'San Marcos de la Sierra',
            '14': 'San Miguelito',
            '15': 'Santa Lucía',
            '16': 'Yamaranguila',
            '17': 'San Francisco de Opalaca'
        }
    },
    '11': {
        'nombre': 'Islas de la Bahía',
        'municipios': {
            '01': 'Roatán',
            '02': 'Guanaja',
            '03': 'José Santos Guardiola',
            '04': 'Utila'
        }
    },
    '12': {
        'nombre': 'La Paz',
        'municipios': {
            '01': 'La Paz',
            '02': 'Aguanqueterique',
            '03': 'Cabañas',
            '04': 'Cane',
            '05': 'Chinacla',
            '06': 'Guajiquiro',
            '07': 'Lauterique',
            '08': 'Marcala',
            '09': 'Mercedes de Oriente',
            '10': 'Opatoro',
            '11': 'San Antonio del Norte',
            '12': 'San José',
            '13': 'San Juan',
            '14': 'San Pedro de Tutule',
            '15': 'Santa Ana',
            '16': 'Santa Elena',
            '17': 'Santa María',
            '18': 'Santiago de Puringla',
            '19': 'Yarula'
        }
    },
    '13': {
        'nombre': 'Lempira',
        'municipios': {
            '01': 'Gracias',
            '02': 'Belén',
            '03': 'Candelaria',
            '04': 'Cololaca',
            '05': 'Erandique',
            '06': 'Gualcince',
            '07': 'Guarita',
            '08': 'La Campa',
            '09': 'La Iguala',
            '10': 'Las Flores',
            '11': 'La Unión',
            '12': 'La Virtud',
            '13': 'Lepaera',
            '14': 'Mapulaca',
            '15': 'Piraera',
            '16': 'San Andrés',
            '17': 'San Francisco',
            '18': 'San Juan Guarita',
            '19': 'San Manuel Colohete',
            '20': 'San Rafael',
            '21': 'San Sebastián',
            '22': 'Santa Cruz',
            '23': 'Talgua',
            '24': 'Tambla',
            '25': 'Tomalá',
            '26': 'Valladolid',
            '27': 'Virginia',
            '28': 'San Marcos de Caiquín'
        }
    },
    '14': {
        'nombre': 'Ocotepeque',
        'municipios': {
            '01': 'Ocotepeque',
            '02': 'Belén Gualcho',
            '03': 'Concepción',
            '04': 'Dolores Merendón',
            '05': 'Fraternidad',
            '06': 'La Encarnación',
            '07': 'La Labor',
            '08': 'Lucerna',
            '09': 'Mercedes',
            '10': 'San Fernando',
            '11': 'San Francisco del Valle',
            '12': 'San Jorge',
            '13': 'San Marcos',
            '14': 'Santa Fé',
            '15': 'Sensenti',
            '16': 'Sinuapa'
        }
    },
    '15': {
        'nombre': 'Olancho',
        'municipios': {
            '01': 'Juticalpa',
            '02': 'Campamento',
            '03': 'Catacamas',
            '04': 'Concordia',
            '05': 'Dulce Nombre de Culmí',
            '06': 'El Rosario',
            '07': 'Esquipulas del Norte',
            '08': 'Gualaco',
            '09': 'Guarizama',
            '10': 'Guata',
            '11': 'Guayape',
            '12': 'Jano',
            '13': 'La Unión',
            '14': 'Mangulile',
            '15': 'Manto',
            '16': 'Salamá',
            '17': 'San Esteban',
            '18': 'San Francisco de Becerra',
            '19': 'San Francisco de la Paz',
            '20': 'Santa María del Real',
            '21': 'Silca',
            '22': 'Yocón',
            '23': 'Patuca'
        }
    },
    '16': {
        'nombre': 'Santa Bárbara',
        'municipios': {
            '01': 'Santa Bárbara',
            '02': 'Arada',
            '03': 'Atima',
            '04': 'Azacualpa',
            '05': 'Ceguaca',
            '06': 'Colinas',
            '07': 'Concepción del Norte',
            '08': 'Concepción del Sur',
            '09': 'Chinda',
            '10': 'El Níspero',
            '11': 'Gualala',
            '12': 'Ilama',
            '13': 'Macuelizo',
            '14': 'Naranjito',
            '15': 'Nueva Celilac',
            '16': 'Petoa',
            '17': 'Protección',
            '18': 'Quimistán',
            '19': 'San Francisco de Ojuera',
            '20': 'San Luis',
            '21': 'San Marcos',
            '22': 'San Nicolás',
            '23': 'San Pedro Zacapa',
            '24': 'Santa Rita',
            '25': 'San Vicente Centenario',
            '26': 'Trinidad',
            '27': 'Las Vegas',
            '28': 'Nueva Frontera'
        }
    },
    '17': {
        'nombre': 'Valle',
        'municipios': {
            '01': 'Nacaome',
            '02': 'Alianza',
            '03': 'Amapala',
            '04': 'Aramecina',
            '05': 'Caridad',
            '06': 'Goascorán',
            '07': 'Langue',
            '08': 'San Francisco de Coray',
            '09': 'San Lorenzo'
        }
    },
    '18': {
        'nombre': 'Yoro',
        'municipios': {
            '01': 'Yoro',
            '02': 'Arenal',
            '03': 'El Negrito',
            '04': 'El Progreso',
            '05': 'Jocón',
            '06': 'Morazán',
            '07': 'Olanchito',
            '08': 'Santa Rita',
            '09': 'Sulaco',
            '10': 'Victoria',
            '11': 'Yorito'
        }
    }
}
# Base de datos ficticia de usuarios
usuarios = {
    "admin": {
        "password": bcrypt.hashpw("admin123".encode('utf-8'), bcrypt.gensalt()),
        "intentos_fallidos": 0
    }
}

def limpiar():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_edad(fecha_nacimiento): # Calcula la edad a partir de la fecha de nacimiento
    hoy = datetime.today()
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def registrar_usuario(usuarios): # Función para registrar un usuario
    username = input("Ingrese un nombre de usuario: ")
    if username in usuarios:
        print("El nombre de usuario ya existe. Intente con otro.")
        return

    password = input("Ingrese una contraseña: ")
    fecha_nacimiento = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) # Encriptar la contraseña
    usuarios[username]  = {
        "password": hashed_password,
        "intentos_fallidos": 0,
        "fecha_nacimiento": fecha_nacimiento
    } # Agregar el usuario a la base de datos ficticia de usuarios y encriptar la contraseña y la fecha de nacimiento encriptada en el diccionario
    print("Usuario registrado exitosamente.")

def iniciar_sesion(usuarios):
    username = input("Ingrese su nombre de usuario: ")
    if username not in usuarios:
        print("Usuario no encontrado.")
        return False

    if usuarios[username]["intentos_fallidos"] >= 3:
        print("Su cuenta está bloqueada debido a múltiples intentos fallidos.")
        return False

    password = input("Ingrese su contraseña: ")
    if bcrypt.checkpw(password.encode('utf-8'), usuarios[username]["password"]):
        print("Inicio de sesión exitoso.")
        usuarios[username]["intentos_fallidos"] = 0
        return True
    else:
        print("Contraseña incorrecta.")
        usuarios[username]["intentos_fallidos"] += 1
        return False

def consultar_departamento_municipio(cedula):
    departamento_codigo = cedula[:2]
    municipio_codigo = cedula[2:4]
    fecha_nacimiento = cedula[4:12]

    departamento = departamentos_municipios.get(departamento_codigo, {}).get('nombre', 'Desconocido')
    municipio = departamentos_municipios.get(departamento_codigo, {}).get('municipios', {}).get(municipio_codigo, 'Desconocido')

    try:
        fecha_nacimiento = f"{fecha_nacimiento[:4]}-{fecha_nacimiento[4:6]}-{fecha_nacimiento[6:]}"
        edad = calcular_edad(fecha_nacimiento)
        es_mayor = edad >= 18
    except ValueError:
        es_mayor = False

    return departamento, municipio, es_mayor

def consultar_departamento():
    print("Departamentos y municipios disponibles:")
    for depto_codigo, depto_info in departamentos_municipios.items():
        print(f"{depto_codigo} - {depto_info['nombre']}")
        for municipio_codigo, municipio_nombre in depto_info['municipios'].items():
            print(f"    {municipio_codigo} - {municipio_nombre}")

def sistema_consulta():
    while True:
        print("\nSistema de Consulta de Departamentos y Municipios")
        print("1. Registrar Usuario")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario(usuarios)
        elif opcion == '2':
            if iniciar_sesion(usuarios):
                while True:
                    print("\nMenú Principal")
                    print("1. Consultar Departamento y Municipio por Cédula")
                    print("2. Consultar Departamento y Municipios")
                    print("3. Cerrar Sesión")
                    opcion = input("Seleccione una opción: ")

                    if opcion == '1':
                        limpiar()
                        dni = input("Ingrese su numero de identidad: ")

                        if not dni.isdigit() or len(dni) != 13:
                            print("Numero de identidad invalido, intente de nuevo (13 digitos y solo enteros)")
                            input("Presione Enter para continuar...")
                        else:
                            id_departamento = dni[0:2]
                            id_municipio = dni[2:4]
                            id_anionacimiento = dni[4:8]
                            edad = datetime.now().year - int(id_anionacimiento)

                            if id_departamento not in departamentos_municipios or id_municipio not in departamentos_municipios[id_departamento]['municipios']:
                                print("Datos no encontrados.")
                                input("Presione Enter para continuar...")
                            else:
                                departamento = departamentos_municipios[id_departamento]
                                municipio = departamento['municipios'].get(id_municipio)
                                print("Departamento: ", departamento['nombre'])
                                print("Municipio: ", municipio)
                                print("Edad: ", edad, " años")

                                if edad >= 21:
                                    print("Eres mayor de edad")
                                elif edad >= 18:
                                    print("Eres ciudadano")
                                else:
                                    print("Eres menor de edad")

                                input("Presione Enter para continuar...")
                    elif opcion == '2':
                        limpiar()
                        id = input("Ingrese el numero de departamento para ver sus municipios y su codigo (ejemplo 16): ")
                        if not id.isdigit() or len(id) != 2:
                            print("Codigo no valido, por favor intente de nuevo. (2 digitos y solo enteros)")
                            input("Presione Enter para continuar...")
                        else:
                            if id not in departamentos_municipios:
                                print("Departamento no encontrado.")
                                input("Presione Enter para continuar...")
                            else:
                                print("Departamento encontrado: ", departamentos_municipios[id]['nombre'])
                                print("-----------------------------------------------------")
                                print("Codigo\t\t Municipio")
                                print("-----------------------------------------------------")
                                for municipio in departamentos_municipios[id]['municipios']:
                                    print(municipio, "\t\t", departamentos_municipios[id]['municipios'][municipio])
                                    
                                input("Presione Enter para continuar...")
                    elif opcion == '3':
                        break
        elif opcion == '3':
            break

sistema_consulta()
