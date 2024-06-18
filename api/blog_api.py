from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime, timezone
from typing import Optional
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')
django.setup()

from products.models import Blog
from customers.models import Customer


router = APIRouter()


class CustomerOut(BaseModel):
    id: int
    first_name: str
    last_name: str


class BlogOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    image: str
    customer: CustomerOut
    created_at: Optional[datetime] = None

class BlogCreate(BaseModel):
    title: str
    description: str
    image: str
    customer: int



@router.get("/blogs", response_model=list[BlogOut])
def get_blogs():
    blogs = Blog.objects.all()
    return [BlogOut(id=blog.id,
                   title=blog.title,
                   description=blog.description,
                   image=blog.image.url,
                   customer=CustomerOut(id=blog.customer.id,
                                        first_name=blog.customer.first_name,
                                        last_name=blog.customer.last_name),
                   created_at=blog.created_at) for blog in

            blogs]




@router.post("/blogs", response_model=BlogOut)
def create_product(blog: BlogCreate):
    customer = Customer.objects.get(id=blog.customer)
    db_blog = Blog(title=blog.title,
                   description=blog.description,
                   image=blog.image,
                   customer=customer)

    db_blog.save()
    return BlogOut(id=db_blog.id,
                   title=db_blog.title,
                   description=db_blog.description,
                   image=db_blog.image.url,
                   customer=CustomerOut(id=db_blog.customer.id,
                                        first_name=db_blog.customer.first_name,
                                        last_name=db_blog.customer.last_name),
                   created_at=db_blog.created_at)



@router.get("/blogs/{blog_id}", response_model=BlogOut)
def get_blog(blog_id: int):
    blog = Blog.objects.filter(id=blog_id).first()
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return BlogOut(id=blog.id,
                   title=blog.title,
                   description=blog.description,
                   image=blog.image.url,
                   customer=CustomerOut(id=blog.customer.id,
                                        first_name=blog.customer.first_name,
                                        last_name=blog.customer.last_name),
                   created_at=blog.created_at)




@router.put("/blog/{blog_id}", response_model=BlogOut)
def update_product(blog_id: int, blog: BlogCreate):
    db_blog = Blog.objects.filter(id=blog_id).first()
    customer = Customer.objects.get(id=blog.customer)

    if db_blog is None:
        raise HTTPException(status_code=404, detail="Product not found")

    db_blog.title = blog.title
    db_blog.description = blog.description
    db_blog.image = blog.image
    db_blog.customer = customer
    db_blog.save()

    return {"message": "Blog updated successfully"}





@router.delete("/blogs/{blog_id}", response_model=dict)
def delete_blog(blog_id: int):
    db_blog = Blog.objects.filter(id=blog_id).first()
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")

    db_blog.delete()
    return {"message": "Blog deleted successfully"}

