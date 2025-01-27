import time
import random

# Base Event class
class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload

# Event Subclasses
class OrderPlacedEvent(Event):
    def __init__(self, customer_name, order_items):
        super().__init__("order_placed", {"customer_name": customer_name, "order_items": order_items})

class OrderBeingPreparedEvent(Event):
    def __init__(self, order_id):
        super().__init__("order_being_prepared", {"order_id": order_id})

class OrderPreparedEvent(Event):
    def __init__(self, order_id):
        super().__init__("order_prepared", {"order_id": order_id})

class OrderServedEvent(Event):
    def __init__(self, customer_name):
        super().__init__("order_served", {"customer_name": customer_name})

# Event Queue
event_queue = []

# Classes Emitting Events
class Customer:
    def __init__(self, name):
        self.name = name

    def place_order(self, order_items):
        event = OrderPlacedEvent(self.name, order_items)
        event_queue.append(event)
        print(f"Customer {self.name} placed an order: {order_items}")

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.current_order_id = 0

    def handle_order(self, event):
        self.current_order_id += 1
        order_id = self.current_order_id
        print(f"Restaurant received order from {event.payload['customer_name']} for {event.payload['order_items']}. Order ID: {order_id}")
        event = OrderBeingPreparedEvent(order_id)
        event_queue.append(event)

class Chef:
    def prepare_order(self, event):
        order_id = event.payload["order_id"]
        print(f"Chef is preparing order ID: {order_id}...")
        time.sleep(random.randint(1, 3))  # Simulate time taken to prepare the order
        print(f"Order ID: {order_id} is ready!")
        event = OrderPreparedEvent(order_id)
        event_queue.append(event)

class Waiter:
    def serve_order(self, event):
        print(f"Waiter is serving order ID: {event.payload['order_id']} to the customer...")
        customer_name = "Unknown"  # You could map order IDs to customers for better tracking
        print(f"Order served to {customer_name}!")
        event = OrderServedEvent(customer_name)
        event_queue.append(event)

# Event Loop
def event_loop():
    while event_queue:
        event = event_queue.pop(0)
        if isinstance(event, OrderPlacedEvent):
            restaurant.handle_order(event)
        elif isinstance(event, OrderBeingPreparedEvent):
            chef.prepare_order(event)
        elif isinstance(event, OrderPreparedEvent):
            waiter.serve_order(event)
        elif isinstance(event, OrderServedEvent):
            print(f"Customer {event.payload['customer_name']} has received their order!")

# Usage
restaurant = Restaurant("The Gourmet Place")
chef = Chef()
waiter = Waiter()

# Customers placing orders
customer1 = Customer("Alice")
customer2 = Customer("Bob")
customer3 = Customer("Charlie")

customer1.place_order(["Pasta", "Salad"])
customer2.place_order(["Burger", "Fries"])
customer3.place_order(["Pizza", "Soda"])

event_loop()
