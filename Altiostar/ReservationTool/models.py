from django.db import models
class DeviceType(models.Model):
    id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=125, default="NA")
    make  = models.CharField(max_length=125, default="NA")
    model = models.CharField(max_length=125, default="NA")
    part_no = models.CharField(max_length=125, default="NA")
    remark = models.CharField(max_length=125, default="NA")

    def __str__(self):
      return self.name
    
    class Meta:
      db_table = "device_types"

class Vendor(models.Model):
    id = models.IntegerField( primary_key= True)
    name = models.CharField(max_length=125)
    email  = models.CharField(max_length=125)
    address = models.CharField(max_length=125)
    number = models.CharField(max_length=125)
    remark = models.CharField(max_length=125)

    def __str__(self):
      return self.name
    
    class Meta:
      db_table = "vendor"
class Device(models.Model):
    id = models.IntegerField( primary_key= True)
    name = models.CharField(max_length=125 , default="NA")
    type = models.ForeignKey( DeviceType ,  on_delete=models.PROTECT, related_name='devices' )
    srno = models.CharField(max_length=125 , default="NA")
    po_number = models.CharField(max_length=125 , default="NA")
    po_date = models.CharField(max_length=125 )
    vendor = models.ForeignKey( Vendor, on_delete=models.PROTECT, related_name='devices')
    invoice_number = models.CharField(max_length=125, default="NA")
    bonded = models.CharField(max_length=125, default="NA")
    bond_number = models.CharField(max_length=125 , default="NA")
    shipped_date = models.CharField(max_length=125)
    arrival_date = models.CharField(max_length=125)
    warranty_inmonths = models.CharField(max_length=125, default="NA")
    added_byuser = models.CharField(max_length=125, default="NA")
    added_date = models.CharField(max_length=125, default="NA")
    ownership = models.CharField(max_length=125, default="NA")
    remark= models.CharField(max_length=125, default="NA")
  
    def __str__(self):
      return self.name
    
    class Meta:
      db_table = "devices"




class CreateSetup(models.Model):
    id = models.IntegerField( primary_key= True)
    name = models.CharField(max_length=125, default="NA" )
    remark = models.CharField(max_length=125, default="NA")
    # attenuator_db = models.CharField(max_length=125, default="10db")
    # rf_cable = models.IntegerField(default=0)
    # rf_shield_box = models.IntegerField(default=0)
    # device_type = models.ForeignKey(Device, on_delete=models.PROTECT )
    #setup_type = models.ForeignKey(SetupType, on_delete=models.PROTECT , null = True)

    def __str__(self):
      return self.name

    class Meta:
      db_table = "create_setups"

class Consumable(models.Model):
    id = models.IntegerField( primary_key= True)
    name = models.CharField(max_length=125, default="NA")
    db  = models.CharField(max_length=125, default="NA")
    connector1 = models.CharField(max_length=125, default="NA")
    connector2 = models.CharField(max_length=125, default="NA")
    watt = models.CharField(max_length=125, default="NA")
    length = models.CharField(max_length=125, default="NA")
    quantity = models.CharField(max_length=125, default="NA")
    remark = models.CharField(max_length=125, default="NA")


    def __str__(self):
      return self.name
    
    class Meta:
      db_table = "consumables"

class MakeSetup(models.Model):
    # make_setup_name = models.ForeignKey ( CreateSetup , on_delete=models.PROTECT )
    # make_setup_device = models.ForeignKey ( Device , on_delete=models.PROTECT )
    # make_setup_consumable = models.ForeignKey ( Consumable , on_delete=models.PROTECT )
    id = models.IntegerField( primary_key= True)
    name = models.CharField(max_length=125, default="NA")
    device = models.ForeignKey(Device, on_delete=models.PROTECT , related_name="make_setup")
    type = models.ForeignKey(DeviceType, on_delete=models.PROTECT , related_name="make_setup")
    consumable = models.ForeignKey(Consumable, on_delete=models.PROTECT , related_name="make_setup")


    def __str__(self):
      return self.name

    class Meta:
      db_table = "make_setup"

