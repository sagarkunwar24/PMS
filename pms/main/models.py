from django.db import models

# Create your models here.

class Quote(models.Model):
    QID = models.AutoField(primary_key=True)
    QLink = models.TextField(max_length=2000)
    Qprice = models.IntegerField()
    Supplier = models.CharField(max_length=30)

class Contract(models.Model):
    CID = models.AutoField(primary_key=True)
    CName = models.TextField(max_length=50)
    CBudget = models.IntegerField()
    CStart = models.DateField()
    CEnd = models.DateField(null=True)

class OrderDetail(models.Model):
    OID = models.AutoField(primary_key=True)
    EID = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    CID = models.ForeignKey(Contract, on_delete=models.CASCADE)
    QID = models.ForeignKey(Quote, on_delete=models.CASCADE)
    productName = models.CharField(max_length=20)
    productDescription = models.TextField(max_length=200)
    deliveryAddress = models.TextField(max_length=200)
    quantity = models.IntegerField()
    total = models.IntegerField()
    orderDate = models.DateField()
    approvedDate = models.IntegerField()
    dateReceived = models.IntegerField()






