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