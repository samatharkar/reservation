from django.db import models


class Vendor(models.Model):
    name = models.CharField('Name', max_length=125)
    email  = models.CharField('Email', max_length=125)
    address = models.CharField('Address', max_length=125)
    number = models.CharField('Number', max_length=125)
    remark = models.CharField('Remark', max_length=125)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "vendors"


class Consumable(models.Model):
    name = models.CharField('Name', max_length=125, default="NA")
    db  = models.CharField('DB', max_length=125, default="NA")
    connector1 = models.CharField('Connector1', max_length=125, default="NA")
    connector2 = models.CharField('Connector2', max_length=125, default="NA")
    watt = models.CharField('Watt', max_length=125, default="NA")
    length = models.CharField('Length', max_length=125, default="NA")
    quantity = models.CharField('Quantity', max_length=125, default="NA")
    remark = models.CharField('Remark', max_length=125, default="NA")


    def __str__(self):
      return self.name
    
    class Meta:
      db_table = "consumables"


class Team(models.Model):
    name = models.CharField('Name', max_length=125, default="NA")
    manager = models.CharField('Manager', max_length=125, default="NA") 
    remark = models.CharField('Remark', max_length=125, default="NA")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "teams"


class SetupType(models.Model):
    name = models.CharField('Name', max_length=125, default="NA")
    remark = models.CharField('Remark', max_length=125, default="NA")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "setup_types"


class Setup(models.Model):
    name = models.CharField('Name', max_length=125, default="NA")
    setup_type = models.ForeignKey(SetupType, on_delete=models.PROTECT , related_name="setups")
    consumable = models.ForeignKey(Consumable, on_delete=models.PROTECT , related_name="setups")
    bookable = models.BooleanField(default=False) #If booked is ticked as yes, It should ask for the team name for which it will be booked
    booked_by = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="setups")
    remark = models.CharField('Remark', max_length=125, default="NA")


    def __str__(self):
        return self.name

    class Meta:
        db_table = "setups"


class DeviceType(models.Model):
    name = models.CharField('Name', max_length=125, default="NA")
    make  = models.CharField('Make', max_length=125, default="NA")
    model = models.CharField('Model', max_length=125, default="NA")
    part_no = models.CharField('Part No.', max_length=125, default="NA")
    remark = models.CharField('Remark', max_length=125, default="NA")
    setup = models.ManyToManyField(Setup, blank=True, related_name="device_types")

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "device_types"


class Device(models.Model):
    TYPE1 = 't1'
    TYPE2 = 't2'
    TYPE3 = 't3'
    CHOICES = [
        (TYPE1, 'Type 1'),
        (TYPE2, 'Type 2'),
        (TYPE3, 'Type 3')
    ]

    name = models.CharField('Name', max_length=125 , default="NA")
    type = models.ForeignKey(DeviceType ,  on_delete=models.PROTECT, related_name='devices' )
    srno = models.CharField('Serial No.', max_length=125 , default="NA")
    po_number = models.CharField('PO No.', max_length=125 , default="NA")
    po_date = models.DateField()
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT, related_name='devices')
    invoice_number = models.CharField('Invoice No.', max_length=125, default="NA")
    bonded = models.BooleanField(default=False) #If bonded is ticked as yes, It should ask for the bond number 
    bond_number = models.CharField('Bond No.', max_length=125 , default="NA")
    setup = models.ForeignKey(Setup, on_delete=models.PROTECT , null=True, blank=True, related_name="devices")
    shipped_date = models.DateField()
    arrival_date = models.DateField()
    warranty_inmonths = models.IntegerField('Warranty(In months)', choices=list(zip(range(1, 37), range(1, 37))))
    added_byuser = models.CharField('Added by user', max_length=125, default="NA")
    added_date = models.DateField()
    ownership = models.CharField('Ownership', max_length=2, choices=CHOICES, default=TYPE1,)
    remark = models.CharField('Remark', max_length=125, default="NA")
  
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "devices"
