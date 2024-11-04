# Product Management API 🛍️

A Django REST API for managing products with JWT (JSON Web Token) authentication. This API provides secure endpoints for CRUD operations on products and includes authentication features.

## Features ✨

- JWT Authentication
- Product CRUD operations
- Protected routes
- Django Admin interface
- RESTful API endpoints

## Prerequisites 📋

- Python 3.x
- Django
- Django REST Framework
- Django REST Framework Simple JWT

## Installation 🚀

1. **Clone the repository**
   ```bash
   git clone https://github.com/benzine12/Django_simple_login_register
   cd Django_simple_login_register
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**
   ```bash
   python manage.py migrate
   ```

4. **Create an admin user**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## Project Structure 📁

```
Django_simple_login_register/
├── myapp/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py         # Product model
│   ├── serializers.py    # Product serializer
│   ├── views.py         # API views for CRUD operations
│   ├── urls.py          # URL configuration
├── manage.py
├── requirements.txt
└── README.md
```

## Database Model 💾

```python
class Product(models.Model):
    desc = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    createdTime = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.desc
```

## API Endpoints 🛣️

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Index route - returns "hello" |
| GET | `/products/` | Get all products |
| POST | `/products/create/` | Create a new product |
| GET | `/products/<id>/` | Get specific product |
| PUT | `/products/<id>/update/` | Update specific product |
| DELETE | `/products/<id>/delete/` | Delete specific product |
| POST | `/login/` | Get JWT tokens |
| GET | `/private/` | Protected route (requires login) |

## Authentication Guide 🔐

### Getting JWT Tokens

```bash
curl -X POST http://127.0.0.1:8000/login/ \
     -H "Content-Type: application/json" \
     -d '{"username": "your_username", "password": "your_password"}'
```

**Response:**
```json
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```

### Accessing Protected Routes

```bash
curl -X GET http://127.0.0.1:8000/private/ \
     -H "Authorization: Bearer your_access_token"
```

## Testing the API 🧪

### Get All Products
```bash
curl -X GET http://127.0.0.1:8000/products/
```

### Create New Product
```bash
curl -X POST http://127.0.0.1:8000/products/create/ \
  -H "Content-Type: application/json" \
  -d '{"desc": "Sample Product", "price": "19.99"}'
```

## Django Admin Panel 👨‍💼

Access the admin interface at `http://127.0.0.1:8000/admin/`

**Default credentials:**
- Username: `admin`
- Password: `admin`

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Need Help? 🤔

If you have any questions or run into issues, please feel free to:
1. Open an issue in the repository
2. Check the documentation
3. Contact the development team

---

*Made with ❤️ by Your Team*