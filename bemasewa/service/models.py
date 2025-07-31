from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)  # ✅ Add this field
    document = models.FileField(upload_to='documents/')  # ✅ Add this field
    status = models.CharField(max_length=20, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.name}"
    

# service/models.py
from django.db import models


class PanCardApplication(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # link to the user who submitted
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    profession = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=200)
    citizenship_front = models.FileField(upload_to='uploads/citizenship/')
    citizenship_back = models.FileField(upload_to='uploads/citizenship/')
    passport_size_photo = models.FileField(upload_to='uploads/photos/')

    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    rejection_note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name
    


class LifeInsuranceApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    STATUS_CHOICES = [('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')]

    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    nominee_name = models.CharField(max_length=100)
    annual_income = models.DecimalField(max_digits=10, decimal_places=2)
    id_proof = models.FileField(upload_to='uploads/id_proofs/')
    photo = models.FileField(upload_to='uploads/photos/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
