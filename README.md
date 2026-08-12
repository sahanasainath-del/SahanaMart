# SahanaMart

SahanaMart is an e-commerce management system built using FastAPI, SQLAlchemy, SQLite, and HTML/CSS/JavaScript.

## Modules

- Authentication
- Admin
- Buyer
- Seller
- Product Management

## Database Design

The system uses three main tables:

### Users
Stores user authentication and role information.

### Sellers
Stores seller/business information and references the Users table using `user_id`.

### Products
Stores product information and references the Sellers table using `seller_id`.

## Relationships

Users → Sellers

One user can be associated with zero or one seller.

Sellers → Products

One seller can have multiple products.

## Foreign Keys

- `sellers.user_id` → `users.id`
- `products.seller_id` → `sellers.id`

## Technologies

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT
- HTML
- CSS
- JavaScript