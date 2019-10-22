from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    name = models.TextField()
    # doctors = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')
    doctors = models.ManyToManyField(Doctor, related_name='patients')

# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.pk}예약 : {self.doctor.name}의 환자 {self.patient.name}'

