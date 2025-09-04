# Django E-commerce

A minimal e-commerce app built with Django and (optionally) React.

## Features

- User registration/login (JWT, custom user)
- Product listing, cart, order management
- Order history
- Admin panel (custom, not Django-admin)
- Docker-ready, .env support

## Setup

### Manual

1. Create `.env` (see `.env.example`)
2. Install requirements: `pip install -r requirements.txt`
3. Migrate: `python manage.py migrate`
4. Run: `python manage.py runserver`

### Docker

1. Build: `docker-compose build`
2. Run: `docker-compose up`

## API

- See `/api/docs/` or provided Postman collection.

## Tests

