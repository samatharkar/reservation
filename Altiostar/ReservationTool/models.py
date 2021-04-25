from django.db import models

# Create your models here.

class SetupType(models.Model):
    name = models.CharField(max_length=125)

class DeviceType(models.Model):
    name = models.CharField(max_length=125)
    is_acquired = models.BooleanField(default=False)


class Device(models.Model):
    hostname = models.CharField(max_length=125)
    serial_number  = models.CharField(max_length=125)
    ip = models.CharField(max_length=125)
    mac = models.CharField(max_length=125)
    device_type = models.ForeignKey(DeviceType , on_delete=models.PROTECT)
    make = models.CharField(max_length=125)


    def __str__(self):
      return self.device_type

class Setup(models.Model):
    setup_name = models.CharField(max_length=125)
    attenuator = models.IntegerField()
    attenuator_db = models.CharField(max_length=125)
    rf_cable = models.IntegerField()
    rf_shield_box = models.IntegerField()
    device_type = models.ForeignKey(Device, on_delete=models.PROTECT)
    setup_type = models.ForeignKey(SetupType, on_delete=models.PROTECT)

    

   # attenuator = models.CharField(max_length=125)


    def __str__(self):
      return self.setup_name

# class Test(models.Model):
#   setup_type = models.ForeignKey(Setup, on_delete=models.CASCADE)