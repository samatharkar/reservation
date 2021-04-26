from django.db import models
#from ReservationTool import fixtures

# Create your models here.

# class SetupType(models.Model):
#     name = models.CharField(max_length=125)
#     is_booked = models.BooleanField(default=False)
    
#     def __str__(self):
#       return self.name

# class DeviceType(models.Model):
#     name = models.CharField(max_length=125)
#     is_acquired = models.BooleanField(default=False)
 
#     def __str__(self):
#       return self.name
    
#     class Meta:
#       db_table = "devices"


class Device(models.Model):
    hostname = models.CharField(max_length=125)
    serial_number  = models.CharField(max_length=125)
    ip = models.CharField(max_length=125)
    mac = models.CharField(max_length=125)
    device_type = models.CharField(max_length=125)
    make = models.CharField(max_length=125)


    def __str__(self):
      return self.hostname
    
    class Meta:
      db_table = "devices"


class Setup(models.Model):
    setup_name = models.CharField(max_length=125 , null = True)
    # attenuator = models.IntegerField()
    # attenuator_db = models.CharField(max_length=125)
    # rf_cable = models.IntegerField()
    # rf_shield_box = models.IntegerField()
    device_type = models.ForeignKey(Device, on_delete=models.PROTECT )
    #setup_type = models.ForeignKey(SetupType, on_delete=models.PROTECT)

    

   # attenuator = models.CharField(max_length=125)


    def __str__(self):
      return self.setup_name

    class Meta:
      db_table = "setups"

# class Test(models.Model):
#   setup_type = models.ForeignKey(Setup, on_delete=models.CASCADE)