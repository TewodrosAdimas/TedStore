# Inventory Management API

This project is an Inventory Management API built with Django and Django REST Framework. It provides features such as managing inventory items, categories, stock levels, user authentication, and logging inventory changes.

## Features

- User authentication and registration.
- CRUD operations for inventory items and categories.
- Track inventory changes (restock, sale).
- Low stock threshold alerts.
- Inventory filtering by category, price, and stock level.
- API pagination and ordering.
- JSON Web Token (JWT) authentication.

## Project Structure

- `models.py`: Defines database models such as `CustomUser`, `Category`, `InventoryItem`, and `InventoryChangeLog`.
- `serializers.py`: Defines serializers for transforming model instances to/from JSON.
- `views.py`: Contains API views for managing users, inventory items, categories, and inventory changes.
- `utils.py`: Contains utility functions such as sending low stock alerts.
- `urls.py`: Defines the URL routing for the API endpoints.

## API Endpoints

### Authentication

- `POST /register/`: Register a new user.
- `POST /login/`: Login and obtain JWT tokens.

### Inventory

- `GET /inventory/`: List all inventory items for the authenticated user (with pagination and sorting).
- `POST /inventory/`: Create a new inventory item.
- `GET /inventory/{id}/`: Retrieve a specific inventory item.
- `PUT /inventory/{id}/`: Update a specific inventory item.
- `DELETE /inventory/{id}/`: Delete a specific inventory item.

### Categories

- `GET /categories/`: List all categories.
- `POST /categories/`: Create a new category.
- `GET /categories/{id}/`: Retrieve a specific category.
- `PUT /categories/{id}/`: Update a specific category.
- `DELETE /categories/{id}/`: Delete a specific category.

### Inventory Levels

- `GET /inventory-levels/`: Get a filtered list of inventory items with stock levels.

### Inventory Change Logs

- `GET /inventory/{item_id}/change-logs/`: Get the change logs for a specific inventory item.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/TewodrosAdimas/TedStore.git
