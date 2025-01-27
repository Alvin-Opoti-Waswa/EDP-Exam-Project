# Restaurant Order Management System

## Overview

This repository contains a Python implementation of a Restaurant Order Management System based on the Event-Driven Programming (EDP) paradigm. The system simulates the flow of customer orders in a restaurant, from placement to preparation and serving, using an event-driven approach with an event queue and multiple classes emitting events.

## Features

Customers can place orders for food items.

-The restaurant receives and processes the orders.

-Chefs prepare the orders, simulating preparation times.

-Waiters serve the orders to customers.

-An event loop ensures sequential handling of all events.

## Key Components

### Events

OrderPlacedEvent: Triggered when a customer places an order.

OrderBeingPreparedEvent: Triggered when the restaurant starts preparing the order.

OrderPreparedEvent: Triggered when the chef finishes preparing the order.

OrderServedEvent: Triggered when the waiter serves the order.

### Classes

Customer:

Places an order and generates an OrderPlacedEvent.

Restaurant:

Handles incoming orders.

Generates an OrderBeingPreparedEvent after assigning an order ID.

Chef:

Prepares the order.

Simulates preparation time.

Generates an OrderPreparedEvent when the order is ready.

Waiter:

Serves the order to the customer.

Generates an OrderServedEvent when the order is served.

### Event Queue

A centralized event queue ensures all events are processed sequentially and in the correct order.

### Event Loop

The event loop dequeues events one by one and delegates them to the appropriate handler (e.g., Restaurant, Chef, Waiter), ensuring a seamless workflow.
