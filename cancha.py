class Cancha:
    def __init__(self, numero_cancha, deporte, habilitada, ):
        self.numero_cancha = numero_cancha
        self.deporte = deporte
        self.habilitada = habilitada
        self.lista_reserva = []
        self.lista_empleado = []


def crear_cancha(mi_cancha):
    numero_cancha = int(input("Introduce el numero de cancha: "))
    deporte = input("Introduce el deporte que se practicara en la cancha de esta lista: -Futbol\n-Baloncesto\n-Volleyball\n-Padel ")
    while True:
        if deporte not in ["Futbol", "Baloncesto", "Voleyball", "Padel"]:
            print("Deporte Invalido.")
            deporte = input("Introduce el deporte que se practicara en la cancha de esta lista: -Futbol\n-Baloncesto\n-Volleyball\n-Padel ")
        else:
            break

    habilitada = input("La cancha esta habilitada: Si/No ").lower()
    if habilitada == "si":
         habilitada = True
    else:
        habilitada = False

    mi_cancha = Cancha(numero_cancha, deporte, habilitada)

    return mi_cancha


def agregar_cancha(lista, mi_cancha):
    if mi_cancha not in lista:
        lista.append(mi_cancha)
    else:
        print("La cancha que desea agregar ya existe.")
    

def listar_canchas(lista):
    for i, deporte in enumerate(lista):
        print(f"{i + 1}. {deporte}.")


def quitar_cancha(lista):
    print("Selecciona la cancha que desee eliminar.")
    for i, deporte in enumerate(lista):
        print(f"{i + 1}. {deporte}.")

    indice_deporte = int(input(""))
    
    if 1 <= indice_deporte <= len(lista):
        lista.pop(indice_deporte - 1)
        print("La cancha ha sido eliminada exitosamente.")
    else:
        print("Índice inválido. Por favor, selecciona un número válido.")