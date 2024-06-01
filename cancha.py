class Cancha:
    def __init__(self, numero, deporte, precio, habilitada=True):
        self.numero = numero
        self.deporte = deporte
        self.precio = precio
        self.habilitada = habilitada
        self.reservas = []
        self.empleados = []

    @staticmethod
    def crear_cancha():
        try:
            numero = int(input("Ingrese el número de cancha: "))
            deporte = input("Ingrese el deporte de la cancha: ")
            precio = float(input("Ingrese el precio de la cancha: "))
        except ValueError as error:
            print("Error:", error)
            return None
        return Cancha(numero, deporte, precio)

    def agregar_cancha(self, lista_canchas):
        for cancha in lista_canchas:
            if cancha.numero == self.numero:
                print(f"La cancha {self.numero} ya está registrada.")
                return
        lista_canchas.append(self)

    @staticmethod
    def listar_canchas_por_deporte(lista_canchas, deporte):
        return [cancha for cancha in lista_canchas if cancha.deporte == deporte]

    def quitar_cancha(self, lista_canchas):
        if self.reservas:
            print(f"No se puede quitar la cancha {self.numero} porque tiene reservas pendientes.")
            return
        lista_canchas.remove(self)
