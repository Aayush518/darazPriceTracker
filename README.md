# Daraz Price Tracker API

This API allows you to track the prices of products listed on daraz.com.np with ease. Utilizing Django Rest Framework, Celery, Redis, and Django-Rest-Knox, it provides a seamless experience for price monitoring and user authentication.

## Features

- Track prices of products on daraz.com.np
- Periodic updates and tracking of prices
- User authentication using Django-Rest-Knox
- Interactive API endpoints for easy integration

## API Reference

### Authentication

#### Login

```http
POST /api/login
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email`   | `string` | **Required**. User's email|
| `password`| `string` | **Required**. User's password |

#### Register

```http
POST /api/register
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email`   | `string` | **Required**. User's email|
| `password`| `string` | **Required**. User's password |

### User Operations

Endpoints below require authentication through an auth token.

#### Logout

```http
POST /api/logout
```

#### Retrieve User

```http
GET /api/user
```

### Product Operations

#### Add Product

```http
POST /api/products/create
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url`     | `string` | **Required**. URL of the product on daraz.com.np|

#### Delete Product

```http
POST /api/products/delete 
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `productId`| `integer`| **Required**. Product ID of the product being deleted|

### Response Format

#### User

```yaml
{
  id: userId,
  email: userEmail,
  products: [
    {
      id: productId,
      title: productTitle,
      url: productUrl,
      image_url: productImageUrl,
      prices: [
        {
          date: dateWhenThisPriceWasTracked,
          price: price
        },
        ...
      ]
    },
    ...
  ]
}
```

#### Login

```yaml
{
  expiry: expiryDateofToken,
  token: authToken,
  user: UserObject
}
```

#### Register

```yaml
{
  user: UserObject,
  token: authToken
}
```

#### Create Product

```yaml
{
  id: productId,
  title: productTitle,
  url: productUrl,
  image_url: productImageUrl,
  prices: [
    {
      date: dateWhenThisPriceWasTracked,
      price: price
    },
    ...
  ]
}
```

## Getting Started

1. Clone the project

```bash
git clone https://github.com/Aayush518/darazPriceTracker
```

2. Navigate to the project directory

```bash
cd darazscarape-api
```

3. Install requirements

```bash
pip install -r requirements.txt
```

4. Start the Django server

```bash
python manage.py runserver
```

5. Start Redis server

```bash
sudo service redis-server start
```

6. Start Celery worker

```bash
celery -A backend worker -l INFO
```

7. Start Celery Beat Scheduler

```bash
celery -A backend beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

Now you're ready to use the Daraz Price Tracker API! Enjoy tracking prices effortlessly.
