```markdown
# SOLID Principles and Design Patterns Relationship

## 1. Decorator Pattern (Pizza Toppings)
### Single Responsibility Principle (SRP)
- Each topping class has one responsibility
- Base pizza classes handle only base pizza functionality
- Toppings handle only their specific modifications

### Open/Closed Principle (OCP)
- New toppings can be added without modifying existing code
- Pizza behavior can be extended through new decorators

### Interface Segregation Principle (ISP)
- Pizza interface is minimal and focused
- Decorators implement only necessary methods

## 2. Singleton Pattern (Inventory Manager)
### Single Responsibility Principle (SRP)
- Inventory Manager has sole responsibility for managing ingredients
- Centralized inventory state management

### Dependency Inversion Principle (DIP)
- High-level modules depend on abstraction
- Concrete implementation is hidden behind singleton interface

## 3. Factory Pattern (Pizza Creation)
### Single Responsibility Principle (SRP)
- Factory handles only object creation
- Separates creation logic from business logic

### Open/Closed Principle (OCP)
- New pizza types can be added without modifying existing code
- Factory method can be extended for new varieties

### Liskov Substitution Principle (LSP)
- All created pizzas can be used interchangeably
- Base pizza type can be replaced with any concrete implementation

## 4. Observer Pattern (Order Notifications)
### Single Responsibility Principle (SRP)
- Each observer has one specific notification responsibility
- Subject manages only subscription and notification

### Open/Closed Principle (OCP)
- New observers can be added without changing existing code
- Notification system is extensible

### Interface Segregation Principle (ISP)
- Observers implement only the methods they need
- Clean separation of notification concerns

## Overall SOLID Compliance
The combination of these patterns creates a system that:
1. Maintains clear separation of concerns (SRP)
2. Is extensible without modification (OCP)
3. Uses proper abstractions (LSP)
4. Keeps interfaces focused (ISP)
5. Depends on abstractions rather than concrete implementations (DIP)

The patterns work together to create a maintainable and extensible system that adheres to SOLID principles while solving specific design challenges in the pizza ordering system.