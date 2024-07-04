class Tarifa:
    def __init__(self,id, tarifa,precio,precio_2):
        self.id=id
        self.tarifa=tarifa
        self.precio=precio
        self.precio_2=precio_2
        print('Tarifa --- Construccion', self)

    def serialize(self):
        return {
        'id':self.id,
        'tarifa':self.tarifa,
        'precio':self.precio,
        'precio_2':self.precio_2
        }
    def __del__(self):
        print('Destructor de ', self)
        self.id = ''
        self.tarifa = ''
        self.precio = ''
        self.precio_2 = ''





