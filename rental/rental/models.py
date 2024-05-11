from django.db import models
from django.contrib.auth.models import User


class Equipment(models.Model):
    equipment = models.CharField(max_length=50)


class Car(models.Model):
    ENGINE_TYPES = [("benzynowy", "Benzynowy"),
                    ("diesel", "Diesel"),
                    ("hybrydowy", "Hybrydowy"),
                    ("elektryczny", "Elektryczny"),
                    ("wodorowy", "Wodorowy")]
    
    GEARBOX_TYPES = [("automatyczna", "Automatyczna"),
                     ("manualna", "Manualna"),
                     ("polautomatyczna", "Polautomatyczna")]
    
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    engine_type = models.CharField(max_length=20, choices=ENGINE_TYPES)
    seats = models.PositiveSmallIntegerField()
    doors = models.PositiveSmallIntegerField()
    fuel_usage = models.FloatField()
    engine_power = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=20)
    equipment = models.ManyToManyField(Equipment)
    gearbox_type = model.CharField(max_length=20, choices=GEARBOX_TYPES)
    available = models.BooleanField()
    price = model.DecimalField(max_digits=10, decimal_places=2)
    value = model.DecimalField(max_digits=10, decimal_places=2)

    pass

class Address(models.Model):
    country =  models.CharField(max_length=20)
    city =  models.CharField(max_length=30)
    post_code = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    buiding_no = models.CharField(max_length=10)
    appartment_no = models.CharField(max_length=10)
    
    pass

class User(User):
    IDENTITY_DOCUMENT_TYPES = [
        ("dowod", "Dowód osobisty"),
        ("prawo jazdy", "Prawo Jazdy"),
        ("paszport", "Paszport")]
    
    username
    password
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    identity_document_type = models.CharField(max_length=20, choices=IDENTITY_DOCUMENT_TYPES)
    identity_document_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    address = models.OneToOneField(Address, on_delete=models.RESTRICT)
    email = models.EmailField()

    pass

class Order(models.Model):
    PAYMENT_METHODS = [
        ("karta", "Karta"),
        ("gotowka", "Gotowka"),
        ("przelew", "Przelew"),
        ("blik", "Blik")]
    customer = models.ForeignKey(User, on_delete=models.RESTRICT)
    car = models.ForeignKey(Car, on_delete=models.RESTRICT)
    order_value = models.DecimalField(max_length=10, decimal_places=2)
    declared_order_duration = models.DurationField()
    pickup_date = models.DateField()
    return_date = models.DateField()
    deposit = models.DecimalField(max_length=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    payment_status = models.BooleanField()

    pass


class User(models.Model):
    pass
