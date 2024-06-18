from django.db import models



class Customer(models.Model):
    class Position(models.TextChoices):
        user = 'User'
        admin = 'Admin'
        worker = 'Worker'

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='customers/', null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=250)
    is_active = models.BooleanField(default=False)
    position = models.CharField(max_length=50, choices=Position.choices, default=Position.user)

    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name



class Comments(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment


class Workers(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


