from ground_transport import GroundTransport

class Motorcycle(GroundTransport):
    def __init__(self) -> None:
        self.wheel_number = 4
        
    def roll(self):
        print("La moto está rodando")
        
    def fill(self):
        print("Llenando tanque de la moto")