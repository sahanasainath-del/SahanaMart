```python
from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    role: str


class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int


class ProductResponse(BaseModel):
    id: int
    seller_id: int
    name: str
    description: str
    price: float
    stock: int

    class Config:
        from_attributes = True
```
