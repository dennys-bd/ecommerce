# Client Endpoint
Interact with the logged Client
Any doubt about general behavior check [readme file](https://github.com/dennys-bd/ecommerce/#acessing-the-application)

## `GET /api/clients/`
Retrieve the logged client

**Response Format:**
```jsonc
{
    "email": "",
    "name": "",
    "products": [
        {
            "id": "",
            "title": "",
            "image": "",
            "price": 0.00,
            "score": 0.0,
        },
        // ...
    ]
}
```


## `PUT/PATCH /api/clients/`
Updates the logged client

**Request Format:**
```jsonc
{
    "email": "",
    "name": ""
}
```

**Response Format:**
It Returns the same as the Retrieve action


## `DELETE /api/clients/`

Delete the logged client

**Response Format:**
This action returns a `204` status
