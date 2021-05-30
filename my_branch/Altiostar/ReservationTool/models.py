from django.db import models


class DeviceType(models.Model):
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
    name = models.CharField(max_length=125)
    email  = models.CharField(max_length=125)
    address = models.CharField(max_length=125)
    number = models.CharField(max_length=125)
    remark = models.CharField(max_length=125)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "vendors"


class Consumable(models.Model):
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


class Team(models.Model):
    name = models.CharField(max_length=125, default="NA")
    manager = models.CharField(max_length=125, default="NA") 
    remark = models.CharField(max_length=125, default="NA")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "teams"


class SetupType(models.Model):
    setup_type = models.CharField(max_length=125, default="NA")
    remark = models.CharField(max_length=125, default="NA")

    def __str__(self):
        return self.setup_type

    class Meta:
        db_table = "setup_types"


class Setup(models.Model):
    name = models.CharField(max_length=125, default="NA")
    setup_type = models.ForeignKey(SetupType, on_delete=models.PROTECT , related_name="make_setup")
    device_type = models.ForeignKey(DeviceType, on_delete=models.PROTECT , related_name="make_setup")
    consumable = models.ForeignKey(Consumable, on_delete=models.PROTECT , related_name="make_setup")
    bookable = models.BooleanField(default=False) #If booked is ticked as yes, It should ask for the team name for which it will be booked
    booked_by = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="make_setup")
    remark = models.CharField(max_length=125, default="NA")


    def __str__(self):
        return self.name

    class Meta:
        db_table = "setups"


class Device(models.Model):
    TYPE1 = 't1'
    TYPE2 = 't2'
    TYPE3 = 't3'
    CHOICES = [
        (TYPE1, 'Type 1'),
        (TYPE2, 'Type 2'),
        (TYPE3, 'Type 3')
    ]

    name = models.CharField(max_length=125 , default="NA")
    type = models.ForeignKey( DeviceType ,  on_delete=models.PROTECT, related_name='devices' )
    srno = models.CharField(max_length=125 , default="NA")
    po_number = models.CharField(max_length=125 , default="NA")
    po_date = models.DateField()
    vendor = models.ForeignKey( Vendor, on_delete=models.PROTECT, related_name='devices')
    invoice_number = models.CharField(max_length=125, default="NA")
    bonded = models.BooleanField(default=False) #If bonded is ticked as yes, It should ask for the bond number 
    bond_number = models.CharField(max_length=125 , default="NA")
    setup = models.ForeignKey(Setup, on_delete=models.PROTECT , null=True, blank=True, related_name="devices")
    shipped_date = models.DateField()
    arrival_date = models.DateField()
    warranty_inmonths = models.IntegerField(choices=list(zip(range(1, 37), range(1, 37))))
    added_byuser = models.CharField(max_length=125, default="NA")
    added_date = models.DateField()
    ownership = models.CharField(max_length=2, choices=CHOICES, default=TYPE1,)
    remark = models.CharField(max_length=125, default="NA")
  
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "devices"
