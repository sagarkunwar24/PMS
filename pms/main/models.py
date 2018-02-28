from django.db import models

# Create your models here.

class Employee(models.Model):
    EID = models.AutoField(primary_key=True)
    EFName = models.TextField(max_length=50)
    ELName = models.TextField(max_length=50)
    EEmail = models.EmailField(max_length=200)
    isAdmin = models.BooleanField()

class Product(models.Model):
    PID = models.AutoField(primary_key=True)
    PName = models.TextField(max_length=50)
    PDescription = models.TextField(max_length=2000)

class Supplier(models.Model):
    SID = models.AutoField(primary_key=True)
    SName = models.TextField(max_length=50)
    SLink = models.TextField(max_length=2000)

class Quote(models.Model):
    QID = models.AutoField(primary_key=True)
    QLink = models.TextField(max_length=2000)
    Qprice = models.CharField(max_length=50)
    SID = models.ForeignKey(Supplier, on_delete=models.CASCADE)

class Contract(models.Model):
    CID = models.AutoField(primary_key=True)
    CName = models.TextField(max_length=50)
    CBudget = models.IntegerField()
    CStart = models.DateField()
    CEnd = models.DateField(null=True)

class OrderDetail(models.Model):
    OID = models.AutoField(primary_key=True)
    EID = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    PID = models.ForeignKey(Product, on_delete=models.CASCADE)
    SID = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    CID = models.ForeignKey(Contract, on_delete=models.CASCADE)
    QID = models.ForeignKey(Quote, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    orderDate = models.DateField()
    isApproved = models.BooleanField()
    hasArrived = models.BooleanField()






