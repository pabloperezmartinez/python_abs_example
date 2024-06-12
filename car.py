from ground_transport import GroundTransport

class Car(GroundTransport):
    def __init__(self) -> None:
        self.wheel_number = 4
        
    def roll(self):
        print("El carro está rodando")
        
    def fill(self):
        print("Llenando tanque del carro")