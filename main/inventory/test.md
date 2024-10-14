register test:
url: http://localhost:8000/register/
{
  "username": "Tewoflos",
  "password": "Tewoflos@1999",
  "email": "tedrcsos@gmail.com"
}


login test:
url: http://localhost:8000/login/
{
  "username": "Tewoflos",
  "password": "Tewoflos@1999"
}


Add category
url: http://localhost:8000/categories/

{
  "name": "Sample Item"
}

Add Inventory
URL: http://127.0.0.1:8000/inventory/

{
  "name": "Sample Item",
  "description": "A description of the sample item.",
  "quantity": 10,
  "price": 19.99,
  "category_id": 1
}

Inventory-Levels test:

url: http://localhost:8000/inventory-levels/

Filter test by category:
GET 
http://localhost:8000/inventory-levels/?category=1
Filter test by price range:
GET http://localhost:8000/inventory-levels/?min_price=10&max_price=50

Filter test by low stock item:
GET http://localhost:8000/inventory-levels/?low_stock=True


Update Inventory
http://localhost:8000/inventory/<inventory_item_id>/

{
	"name": "Add your name in the body",
    "quantity": "5",
    "price": "15",
    "category_id": "1"
}