class Cliente:
    def __init__(self, nombre, apellido, telefono, identificador, activo=True):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.identificador = identificador
        self.activo = activo
        self.saldo = 0
        self.reservas = []

    @staticmethod
    def crear_cliente():
        try:
            nombre = input("Ingrese el nombre del cliente: ")
            apellido = input("Ingrese el apellido del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            identificador = input("Ingrese el identificador del cliente: ")
        except ValueError as error:
            print("Error:", error)
            return None
        return Cliente(nombre, apellido, telefono, identificador)

    def agregar_cliente(self, lista_clientes):
        for cliente in lista_clientes:
            if cliente.identificador == self.identificador:
                print(f"El cliente con ID {self.identificador} ya está registrado.")
                return
        lista_clientes.append(self)

    def quitar_cliente(self, lista_clientes):
        if self.reservas:
            print(f"No se puede quitar el cliente {self.identificador} porque tiene reservas pendientes.")
            return
        lista_clientes.remove(self)

    @staticmethod
    def listar_clientes_morosos(lista_clientes):
        return [cliente for cliente in lista_clientes if cliente.saldo < 0]



