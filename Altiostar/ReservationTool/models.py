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
    bonded = models.BooleanField(default=False) #If bonded is ticked as yes, It should ask for the bond number 
    bond_number = models.CharField(max_length=125 , default="NA")
    shipped_date = models.CharField(max_length=125)
    arrival_date = models.CharField(max_length=125)
    warranty_inmonths = models.IntegerField(choices=list(zip(range(1, 37), range(1, 37))))
    added_byuser = models.CharField(max_length=125, default="NA")
    added_date = models.CharField(max_length=125, default="NA")
    type1 = 't1'
    type2 = 't2'
    type3 = 't3'
    CHOICES = [(type1, 'Type 1'),(type2, 'Type 2'),(type3, 'Type 3')]
    ownership = models.CharField(max_length=2, choices=CHOICES, default=type1,)
    remark= models.CharField(max_length=125, default="NA")
  
    def __str__(self):
      return self.name
    
    class Meta:
      db_table = "devices"




class CreateSetup(models.Model):
    id = models.IntegerField( primary_key= True)
    name = models.CharField(max_length=125, default="NA" )
    remark = models.CharField(max_length=125, default="NA")

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

class SetupType(models.Model):
    id = models.IntegerField( primary_key= True)
    setup_type = models.CharField(max_length=125, default="NA")
    remark = models.CharField(max_length=125, default="NA")

    def __str__(self):
      return self.setup_type

    class Meta:
      db_table = "setup_type"

class Team(models.Model):
    id = models.IntegerField( primary_key= True)
    name = models.CharField(max_length=125, default="NA")
    manager = models.CharField(max_length=125, default="NA") 
    remark = models.CharField(max_length=125, default="NA")

    def __str__(self):
      return self.team

    class Meta:
      db_table = "team"

class MakeSetup(models.Model):

    id = models.IntegerField( primary_key= True)
    name = models.CharField(max_length=125, default="NA")
    setup_type = models.ForeignKey(SetupType, on_delete=models.PROTECT , related_name="make_setup")
    device = models.ForeignKey(Device, on_delete=models.PROTECT , related_name="make_setup")
    type = models.ForeignKey(DeviceType, on_delete=models.PROTECT , related_name="make_setup")
    consumable = models.ForeignKey(Consumable, on_delete=models.PROTECT , related_name="make_setup")
    bookable = models.BooleanField(default=False) #If booked is ticked as yes, It should ask for the team name for which it will be booked
    booked_by = models.ForeignKey( Team , on_delete=models.PROTECT, related_name="make_setup")
    remark = models.CharField(max_length=125, default="NA")



    def __str__(self):
      return self.name

    class Meta:
      db_table = "make_setup"


