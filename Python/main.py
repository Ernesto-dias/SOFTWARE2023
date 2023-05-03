from car import Car 
from account import Account 
from uberX import UberX 
from user import User 

if _name_ == "_main_":
    print("Inicializando las info de los carros")
    print("Car")
    car = Car("AMS256", Account("Andres Herrera", "ADS12365","andrea@platzi.com", "2563"))
    print(vars(car))
    print(vars(car.driver))

    print("UberX")
    uberX = UberX("KLO365", Account("Marco Lois", "SGHJ1236","marco@platzi.com", "7856",) "Toyota","Corolla")
    print(vars(uberX))
    print( vars(uberX.driver))

    print("User")
    user = User("mariana Valle", "SDFG125F", "mariana@platzi.com","7856")
    print(vars(user))