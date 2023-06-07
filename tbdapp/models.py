from django.db import models

# Create your models here.



class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    street_number = models.IntegerField()
    street_name = models.CharField(max_length=50)
    city_name = models.CharField(max_length=50)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.street_name} No. {self.street_number}, {self.city_name}"

    class Meta:
        managed = False
        db_table = 'address'


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length=20)
    author_name = models.CharField(max_length=50)
    main_genre = models.CharField(max_length=50)
    last_update = models.DateTimeField(blank=True, null=True)
    publisher = models.ForeignKey('Publisher', models.DO_NOTHING)
    price = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.author_name}"

    class Meta:
        managed = False
        db_table = 'book'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer_id} - {self.first_name} {self.last_name} ({self.email})"

    class Meta:
        managed = False
        db_table = 'customer'


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    last_update = models.DateTimeField(blank=True, null=True)
    book = models.ForeignKey(Book, models.DO_NOTHING)
    store = models.ForeignKey('Store', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'inventory'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    staff = models.ForeignKey('Staff', models.DO_NOTHING)
    inventory = models.ForeignKey(Inventory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orders'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    order = models.ForeignKey(Orders, models.DO_NOTHING)
    staff = models.ForeignKey('Staff', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment'


class Publisher(models.Model):
    publisher_id = models.AutoField(primary_key=True)
    last_update = models.DateTimeField(blank=True, null=True)
    publisher_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publisher'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    last_update = models.DateTimeField(blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING)

    def __str__(self):
        return f"{self.staff_id} - {self.first_name} {self.last_name}"

    class Meta:
        managed = False
        db_table = 'staff'


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    last_update = models.DateTimeField(blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'store'
