import uuid
from django.db import models
from datetime import datetime


class Event(models.Model):
    eventName = models.CharField(max_length=200)
    eventDescription = models.TextField()
    eventPublished = models.DateTimeField("date published", default=datetime.now())
    eventId = models.CharField(max_length=36, null=True, unique=True, default=uuid.uuid4())

    def __str__(self):
        return self.eventName


class Activity(models.Model):
    activityId = models.CharField(max_length=36, null=True, unique=True, default=uuid.uuid4())
    activityStart = models.DateTimeField("activity start", default=datetime.now())
    activityEnd = models.DateTimeField("activity end", default=datetime.now())
    activityVolunteerId = models.CharField(max_length=36, null=True, unique=True, default=uuid.uuid4())
    eventId = models.CharField(max_length=36)
    activityDescription = models.TextField(default="text")
    activityName = models.CharField(max_length=200, default="activity name")

    def __str__(self):
        return self.activityId


class Trail(models.Model):
    activityId = models.CharField(max_length=36, null=True, unique=True, default=uuid.uuid4())
    activityStart = models.DateTimeField("activity start", default=datetime.now())
    activityEnd = models.DateTimeField("activity end", default=datetime.now())
    activityVolunteerId = models.CharField(max_length=36, null=True, unique=True, default=uuid.uuid4())
    eventId = models.CharField(max_length=36)
    trailName = models.CharField(max_length=200, default="trail name")

    def __str__(self):
        return self.activityId
class TrailSignUp(models.Model):
    activityId = models.CharField()
    

class LimActivity(models.Model):
    activityId = models.CharField(max_length=36, null=True, unique=True, default=uuid.uuid4())
    numberOfParticipants = models.BigIntegerField(default=0)
    activityStart = models.DateTimeField("activity start", default=datetime.now())
    activityEnd = models.DateTimeField("activity end", default=datetime.now())
    activityVolunteerId = models.CharField(max_length=36, null=True, unique=True, default=uuid.uuid4())
    eventId = models.CharField(max_length=36)

    def __str__(self):
        return self.activityId


class Vehicle(models.Model):
    vehicleId = models.CharField(max_length=36, null=True, unique=True, default=uuid.uuid4())
    vehicleMake = models.CharField(max_length=30)
    vehicleModel = models.CharField(max_length=30)
    vehicleYear = models.CharField(max_length=4)
    vehicleLicensePlateState = models.CharField(max_length=14)
    vehicleLicensePlateNum = models.CharField(max_length=20)

    def __str__(self):
        return self.vehicleId


class VehicleReg(models.Model):
    vehicleId = models.CharField(max_length=36)
    eventId = models.CharField(max_length=36)
    vehicleType = models.CharField(max_length=36)  # This will change to choices field, need to define choices
    trailPass = models.BooleanField(default=False)

    def __str__(self):
        return self.vehicleId
