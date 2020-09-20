from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.IntegerField(max_length=3)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.id} : {self.code} city {self.city}"
    
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name="departures") #models.CharField(max_length=64)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name="arrivals")#models.CharField(max_length=64)
    duration = models.IntegerField()
    
    def __str__(self):
        return f"{self.id} :   {self.origin} to {self.destination}"
    
class Passenger(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    flights= models.ManyToManyField(Flight,blank=True, related_name="passengers")