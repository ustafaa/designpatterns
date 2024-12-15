# Design Patterns Implementation

## 1. Decorator Pattern (Pizza Toppings)
### Before Pattern
Initially, we would need separate classes for each pizza-topping combination:
```python
class MargheritaWithCheese(Pizza):
    def get_cost(self): return 6.0
class MargheritaWithOlives(Pizza):
    def get_cost(self): return 5.5
```
### After Pattern
The Decorator pattern allows dynamic addition of toppings:
```python
pizza = MargheritaPizza()
pizza = CheeseTopping(pizza)
pizza = OlivesTopping(pizza)
```
### Benefits
- Flexible composition of toppings
- Easy to add new toppings
- Maintains Single Responsibility Principle

## 2. Singleton Pattern (Inventory Manager)
### Before Pattern
Multiple inventory instances could lead to inconsistent state:
```python
inventory1 = InventoryManager()
inventory2 = InventoryManager()
```
### After Pattern
```python
class InventoryManager:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```
### Benefits
- Ensures single source of truth for inventory
- Prevents resource conflicts
- Centralizes inventory management

## 3. Factory Pattern (Pizza Creation)
### Before Pattern
Direct instantiation with complex logic:
```python
if type == "margherita":
    pizza = MargheritaPizza()
elif type == "pepperoni":
    pizza = PepperoniPizza()
```
### After Pattern
```python
pizza = PizzaFactory.create_pizza(choice)
```
### Benefits
- Encapsulates creation logic
- Easy to add new pizza types
- Centralized creation point

## 4. Observer Pattern (Order Notifications)
### Before Pattern
Direct coupling between components:
```python
class Order:
    def process(self):
        notify_kitchen()
        notify_customer()
```
### After Pattern
```python
order_subject = Subject()
order_subject.attach(kitchen_display)
order_subject.attach(order_tracker)
order_subject.notify(message)
```
### Benefits
- Loose coupling
- Easy to add new observers
- Flexible notification system

## Overengineering Example


```python
class OverengineeredPizzaSystem:
    def __init__(self):
        self.observers = {}
        self.notification_queue = []
        self.event_handlers = {}
        self.pizza_cache = {}
        self.topping_validators = {}
        self.price_calculators = {}
        self.ingredient_proxies = {}
        self.order_state_machine = {}
        self.payment_middleware = []
        
    def process_order(self, order):
        # Unnecessary complexity
        self.validate_order_state()
        self.check_ingredient_availability()
        self.calculate_optimal_preparation_sequence()
        self.notify_all_subsystems()
        self.update_various_caches()
        # More unnecessary steps...
```

This is overengineered because:
1. Too many abstraction layers
2. Unnecessary caching
3. Complex state management
4. Over-modularization
5. Excessive use of design patterns