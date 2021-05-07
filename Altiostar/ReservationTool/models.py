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

class DeviceType(models.Model):
    type_name = models.CharField(max_length=125, default="NA")
    type_make  = models.CharField(max_length=125, default="NA")
    type_model = models.CharField(max_length=125, default="NA")
    type_part_no = models.CharField(max_length=125, default="NA")
    type_remark = models.CharField(max_length=125, default="NA")

    def __str__(self):
      return self.type_name
    
    class Meta:
      db_table = "device_types"
class Device(models.Model):
    device_name = models.CharField(max_length=125 , default="NA")
    device_type = models.CharField(max_length=125 , default="NA")
    device_srno = models.CharField(max_length=125 , default="NA")
    device_po_number = models.CharField(max_length=125 , default="NA")
    device_po_date = models.CharField(max_length=125 )
    device_vendor = models.CharField(max_length=125, default="NA")
    device_invoice_number = models.CharField(max_length=125, default="NA")
    device_bonded = models.CharField(max_length=125, default="NA")
    device_bond_number = models.CharField(max_length=125 , default="NA")
    device_shipped_date = models.CharField(max_length=125)
    device_arrival_date = models.CharField(max_length=125)
    device_warranty_inmonths = models.CharField(max_length=125, default="NA")
    device_added_byuser = models.CharField(max_length=125, default="NA")
    device_added_date = models.CharField(max_length=125, default="NA")
    device_ownership = models.CharField(max_length=125, default="NA")
    device_remark= models.CharField(max_length=125, default="NA")
  
    def __str__(self):
      return self.device_name
    
    class Meta:
      db_table = "devices"




class CreateSetup(models.Model):
    create_setup_name = models.CharField(max_length=125, default="NA" )
    create_setup_remark = models.CharField(max_length=125, default="NA")
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
    consumable_name = models.CharField(max_length=125, default="NA")
    consumable_db  = models.CharField(max_length=125, default="NA")
    consumable_connector1 = models.CharField(max_length=125, default="NA")
    consumable_connector2 = models.CharField(max_length=125, default="NA")
    consumable_watt = models.CharField(max_length=125, default="NA")
    consumable_length = models.CharField(max_length=125, default="NA")
    consumable_quantity = models.CharField(max_length=125, default="NA")
    consumable_remark = models.CharField(max_length=125, default="NA")


    def __str__(self):
      return self.consumable_name
    
    class Meta:
      db_table = "consumables"

class MakeSetup(models.Model):
    # make_setup_name = models.ForeignKey ( CreateSetup , on_delete=models.PROTECT )
    # make_setup_device = models.ForeignKey ( Device , on_delete=models.PROTECT )
    # make_setup_consumable = models.ForeignKey ( Consumable , on_delete=models.PROTECT )
    make_setup_name = models.CharField(max_length=125, default="NA")
    make_setup_device = models.CharField(max_length=125, default="NA")
    make_setup_consumable = models.CharField(max_length=125, default="NA")


    def __str__(self):
      return self.make_setup_name

    class Meta:
      db_table = "make_setup"

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