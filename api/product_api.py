from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')
django.setup()

from products.models import Product, Category


router = APIRouter()


class CategoryOut(BaseModel):
    id: int
    name: str

class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    image: str
    category: CategoryOut
    price: int
    stock: int

class ProductCreate(BaseModel):
    name: str
    description: str
    image: str
    category: int
    price: int
    stock: int




@router.get("/products", response_model=list[ProductOut])
def get_products():
    products = Product.objects.all()
    return [ProductOut(id=product.id,
                       name=product.name,
                       description=product.description,
                       image=product.image.url,
                       category=CategoryOut(id=product.category.id,
                                            name=product.category.name),
                       price=product.price,
                       stock=product.stock) for product in

            products]



@router.post("/products", response_model=ProductOut)
def create_product(product: ProductCreate):
    category = Category.objects.get(id=product.category)
    db_product = Product(name=product.name,
                         description=product.description,
                         image=product.image,
                         category=category,
                         price=product.price,
                         stock=product.stock)

    db_product.save()
    return ProductOut(id=db_product.id,
                      name=db_product.name,
                      description=db_product.description,
                      image=db_product.image.url,
                      category=CategoryOut(id=category.id,
                                           name=category.name),
                      price=db_product.price,
                      stock=db_product.stock)




@router.get("/products/{product_id}", response_model=ProductOut)
def get_product(product_id: int):
    product = Product.objects.filter(id=product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductOut(id=product.id,
                        name=product.name,
                        description=product.description,
                        image=product.image.url,
                        category=CategoryOut(id=product.category.id,
                                             name=product.category.name),
                        price=product.price,
                        stock=product.stock)



# @router.put("/products/{product_id}", response_model=ProductOut)
# def update_product(product_id: int, product: ProductCreate):
#     db_product = Product.objects.filter(id=product_id).first()
#     if db_product is None:
#         raise HTTPException(status_code=404, detail="Product not found")
#
#     category = Category.objects.get(id=product.category)
#     db_product.name = product.name
#     db_product.description = product.description
#     db_product.image = product.image
#     db_product.category = category
#     db_product.price = product.price
#     db_product.stock = product.stock
#     db_product.save()
#
#     return ProductOut(id=db_product.id,
#                       name=db_product.name,
#                       description=db_product.description,
#                       image=db_product.image.url,
#                       category=CategoryOut(id=category.id,
#                                            name=category.name),
#                       price=db_product.price,
#                       stock=db_product.stock)


@router.delete("/products/{product_id}", response_model=dict)
def delete_product(product_id: int):
    db_product = Product.objects.filter(id=product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    db_product.delete()
    return {"message": "Product deleted successfully"}


