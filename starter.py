from abc import ABC, abstractmethod
from typing import List

# Base Pizza Class
class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass
    
    @abstractmethod
    def get_cost(self) -> float:
        pass

# Concrete Pizza Classes
class MargheritaPizza(Pizza):
    def get_description(self) -> str:
        return "Margherita Pizza"
    
    def get_cost(self) -> float:
        return 5.0

class PepperoniPizza(Pizza):
    def get_description(self) -> str:
        return "Pepperoni Pizza"
    
    def get_cost(self) -> float:
        return 6.0

# Topping Decorator
class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

class CheeseTopping(ToppingDecorator):
    def get_description(self) -> str:
        return f"{self._pizza.get_description()}, extra cheese"
    
    def get_cost(self) -> float:
        return self._pizza.get_cost() + 1.0

class OlivesTopping(ToppingDecorator):
    def get_description(self) -> str:
        return f"{self._pizza.get_description()}, olives"
    
    def get_cost(self) -> float:
        return self._pizza.get_cost() + 0.5

class MushroomsTopping(ToppingDecorator):
    def get_description(self) -> str:
        return f"{self._pizza.get_description()}, mushrooms"
    
    def get_cost(self) -> float:
        return self._pizza.get_cost() + 0.7


class PizzaFactory:
    @staticmethod
    def create_pizza(choice: str) -> Pizza:
        if choice == "1":
            return MargheritaPizza()
        elif choice == "2":
            return PepperoniPizza()
        raise ValueError("Invalid pizza choice")


class InventoryManager:
    _instance = None
    _inventory = {
        "Margherita": 10,
        "Pepperoni": 10,
        "Cheese": 15,
        "Olives": 10,
        "Mushrooms": 12,
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def check_and_decrement(self, item: str) -> bool:
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return self._inventory

# Observer Pattern
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class Subject:
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)

class KitchenDisplay(Observer):
    def update(self, message: str):
        print(f"Kitchen Display: {message}")

class OrderTracker(Observer):
    def update(self, message: str):
        print(f"Order Tracking: {message}")

# Payment System
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f"Processing credit card payment for ${amount:.2f}")
        return True

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f"Processing PayPal payment for ${amount:.2f}")
        return True

# Main Function
def main():
    inventory_manager = InventoryManager()
    order_subject = Subject()
    kitchen_display = KitchenDisplay()
    order_tracker = OrderTracker()
    order_subject.attach(kitchen_display)
    order_subject.attach(order_tracker)

    print("Welcome to the Pizza Restaurant!")

    while True:
        print("\nChoose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0 => to exit")
        
        pizza_choice = input("Enter the number of your choice: ")
        if pizza_choice == '0':
            break

        try:
            pizza = PizzaFactory.create_pizza(pizza_choice)
            
            # Toppings menu
            while True:
                print("\nAdd toppings:")
                print("1. Cheese (+$1.0)")
                print("2. Olives (+$0.5)")
                print("3. Mushrooms (+$0.7)")
                print("0. Done with toppings")
                
                topping_choice = input("Choose a topping (0-3): ")
                
                if topping_choice == "0":
                    break
                elif topping_choice == "1" and inventory_manager.check_and_decrement("Cheese"):
                    pizza = CheeseTopping(pizza)
                elif topping_choice == "2" and inventory_manager.check_and_decrement("Olives"):
                    pizza = OlivesTopping(pizza)
                elif topping_choice == "3" and inventory_manager.check_and_decrement("Mushrooms"):
                    pizza = MushroomsTopping(pizza)
                else:
                    print("Invalid choice or topping not available!")

            # Payment
            print(f"\nTotal cost: ${pizza.get_cost():.2f}")
            print("Choose payment method:")
            print("1. Credit Card")
            print("2. PayPal")
            
            payment_choice = input("Enter payment method (1-2): ")
            payment_strategy = CreditCardPayment() if payment_choice == "1" else PayPalPayment()
            
            if payment_strategy.pay(pizza.get_cost()):
                order_subject.notify(f"New order: {pizza.get_description()} - ${pizza.get_cost():.2f}")
                print("\nOrder completed successfully!")
            else:
                print("\nPayment failed!")

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()