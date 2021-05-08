# Product Endpoint
Interact with logged client favorit products list
Any doubt about general behavior check [readme file](https://github.com/dennys-bd/ecommerce/#acessing-the-application)

## `GET /api/products/`
List client's favorite products

**Response Format:**
```jsonc
[
    {
        "id": "",
        "title": "",
        "image": "",
        "price": 0.00,
        "score": 0.0,
    },
    // ...
]
```

## `POST /api/products/`
Add a product to client's list


**Request Format:**
```jsonc
{
    "id": "",
}
```

**Response Format:**
```jsonc
{
    "id": "",
    "title": "",
    "image": "",
    "price": 0.00,
    "score": 0.0,
}
```

## `DELETE /api/products/:id/`
This action returns a `204` status
