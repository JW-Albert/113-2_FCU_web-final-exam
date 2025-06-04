# FCU Shop

A Django-based e-commerce website for FCU (Feng Chia University) merchandise.

## Features

- User authentication (login/logout)
- Product listing with images and descriptions
- Shopping cart functionality
- Checkout system
- Purchase history
- Responsive design using Bootstrap

## Technical Stack

- Python 3.x
- Django
- SQLite (Database)
- Bootstrap 5 (Frontend)
- Pillow (Image processing)

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd fcu-shop
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Project Structure

```
fcu-shop/
├── fcu_shop/          # Main project configuration
├── shop/             # Main application
├── templates/        # HTML templates
├── static/          # Static files (CSS, JS, images)
├── media/           # User-uploaded files
└── manage.py        # Django management script
```

## Usage

1. Access the admin interface at `http://127.0.0.1:8000/admin` to manage products
2. Browse products at `http://127.0.0.1:8000/product_list/`
3. Add products to cart and proceed to checkout
4. View purchase history after completing orders

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.