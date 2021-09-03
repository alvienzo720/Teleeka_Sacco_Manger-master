from django.db import models

# Create your models here.

# SavingGroup model
class SavingGroup(models.Model):
	STATUS = (
		('Verified','Verified'),
		('Pending-verification', 'Pending-verification'),
		)
	name = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)



	def __str__(self):
		return self.name

# Client Model

class Client(models.Model):
	STATUS = (
		('Active','Active'),
		('Pending', 'Pending'),
		)
	fullname = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	group = models.ForeignKey(SavingGroup, on_delete=models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	



	def __str__(self):
		return self.fullname



# deposit model

class Deposit(models.Model):
	STATUS = (
		('Pending','Pending'),
		('Completed', 'Completed'),
		)
	clientName = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
	group = models.ForeignKey(SavingGroup, on_delete=models.SET_NULL, null=True)
	amount = models.IntegerField(null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)



	def __str__(self):
		return str(self.clientName)


# withrwal model
class Withdrawl(models.Model):
	STATUS = (
		('Pending','Pending'),
		('Completed', 'Completed'),
		)
	clientName = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
	group = models.ForeignKey(SavingGroup, on_delete=models.SET_NULL, null=True)
	amount = models.IntegerField(null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)



	def __str__(self):
		return str(self.clientName)


class Loan(models.Model):
	clientName = models.ForeignKey(Client, on_delete=models.SET_NULL,null=True)

