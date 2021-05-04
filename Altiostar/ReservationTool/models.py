from django.db import models
#from ReservationTool import fixtures

# Create your models here.

# class SetupType(models.Model):
#      name = models.CharField(max_length=125, default="Setup Name")
#      is_booked = models.BooleanField(default=False)
   
#      def __str__(self):
#        return self.name

# class DeviceType(models.Model):
#     name = models.CharField(max_length=125)
#     is_acquired = models.BooleanField(default=False)
 
#     def __str__(self):
#       return self.name
    
#     class Meta:
#       db_table = "devices"


class Device(models.Model):
    device_name = models.CharField(max_length=125)
    device_srno = models.CharField(max_length=125)
    device_po_number = models.CharField(max_length=125)
    device_po_date = models.CharField(max_length=125)
    device_vendor = models.CharField(max_length=125)
    device_invoice_number = models.CharField(max_length=125)
    device_bonded = models.CharField(max_length=125)
    device_bond_number = models.CharField(max_length=125)
    device_shipped_date = models.CharField(max_length=125)
    device_arrival_date = models.CharField(max_length=125)
    device_warranty_inmonths = models.CharField(max_length=125)
    device_added_byuser = models.CharField(max_length=125)
    device_added_date = models.CharField(max_length=125)
    device_ownership = models.CharField(max_length=125)
    device_remark= models.CharField(max_length=125)
  
    def __str__(self):
      return self.device_name
    
    class Meta:
      db_table = "devices"

class DeviceType(models.Model):
    type_name = models.CharField(max_length=125)
    type_make  = models.CharField(max_length=125)
    type_model = models.CharField(max_length=125)
    type_part_no = models.CharField(max_length=125)
    type_remark = models.CharField(max_length=125)

    def __str__(self):
      return self.type_name
    
    class Meta:
      db_table = "device_types"


class CreateSetup(models.Model):
    create_setup_name = models.CharField(max_length=125 )
    create_setup_remark = models.CharField(max_length=125)
    # attenuator_db = models.CharField(max_length=125, default="10db")
    # rf_cable = models.IntegerField(default=0)
    # rf_shield_box = models.IntegerField(default=0)
    # device_type = models.ForeignKey(Device, on_delete=models.PROTECT )
    #setup_type = models.ForeignKey(SetupType, on_delete=models.PROTECT , null = True)

    def __str__(self):
      return self.create_setup_name

    class Meta:
      db_table = "create_setups"

class Consumable(models.Model):
    consumable_name = models.CharField(max_length=125)
    consumable_db  = models.CharField(max_length=125)
    consumable_connector1 = models.CharField(max_length=125)
    consumable_connector2 = models.CharField(max_length=125)
    consumable_watt = models.CharField(max_length=125)
    consumable_length = models.CharField(max_length=125)
    consumable_quantity = models.CharField(max_length=125)
    consumable_remark = models.CharField(max_length=125)


    def __str__(self):
      return self.consumable_name
    
    class Meta:
      db_table = "consumables"

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=125)
    vendor_email  = models.CharField(max_length=125)
    vendor_address = models.CharField(max_length=125)
    vendor_number = models.CharField(max_length=125)
    vendor_remark = models.CharField(max_length=125)

    def __str__(self):
      return self.vendor_name
    
    class Meta:
      db_table = "vendor"