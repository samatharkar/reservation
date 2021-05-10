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
    type_id = models.IntegerField( primary_key= True)
    type_name = models.CharField(max_length=125, default="NA")
    type_make  = models.CharField(max_length=125, default="NA")
    type_model = models.CharField(max_length=125, default="NA")
    type_part_no = models.CharField(max_length=125, default="NA")
    type_remark = models.CharField(max_length=125, default="NA")

<<<<<<< HEAD
    def __str__(self):
      return self.type_name
    
    class Meta:
      db_table = "device_types"
class Device(models.Model):
    device_id = models.IntegerField( primary_key= True)
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
=======
# class Device(models.Model):
#     hostname = models.CharField(max_length=125)
#     serial_number  = models.CharField(max_length=125)
#     ip = models.CharField(max_length=125)
#     mac = models.CharField(max_length=125)
#     device_type = models.CharField(max_length=125)
#     make = models.CharField(max_length=125)


#     def __str__(self):
#       return self.hostname
>>>>>>> main
    
#     class Meta:
#       db_table = "devices"


<<<<<<< HEAD


class CreateSetup(models.Model):
    create_setup_id = models.IntegerField( primary_key= True)
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
    consumable_id = models.IntegerField( primary_key= True)
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
    make_setup_id = models.IntegerField( primary_key= True)
    make_setup_name = models.CharField(max_length=125, default="NA")
    make_setup_device = models.CharField(max_length=125, default="NA")
    make_setup_consumable = models.CharField(max_length=125, default="NA")


    def __str__(self):
      return self.make_setup_name

    class Meta:
      db_table = "make_setup"

class Vendor(models.Model):
    vendor_id = models.IntegerField( primary_key= True)
    vendor_name = models.CharField(max_length=125)
    vendor_email  = models.CharField(max_length=125)
    vendor_address = models.CharField(max_length=125)
    vendor_number = models.CharField(max_length=125)
    vendor_remark = models.CharField(max_length=125)

    def __str__(self):
      return self.vendor_name
    
    class Meta:
      db_table = "vendor"
=======
# class Setup(models.Model):
#     setup_name = models.CharField(max_length=125 , null = True)
#     attenuator_quantity = models.IntegerField(default=0)
#     attenuator_db = models.CharField(max_length=125, default="10db")
#     rf_cable = models.IntegerField(default=0)
#     rf_shield_box = models.IntegerField(default=0)
#     device_type = models.ForeignKey(Device, on_delete=models.PROTECT )
#     setup_type = models.ForeignKey(SetupType, on_delete=models.PROTECT , null = True)
    
#    # attenuator = models.CharField(max_length=125)


#     def __str__(self):
#       return self.setup_name

#     class Meta:
#       db_table = "setups"

# class Test(models.Model):
#   setup_type = models.ForeignKey(Setup, on_delete=models.CASCADE)


class ServerType(models.Model):
  #  server_type_id = models.AutoField(primary_key=True, default=0)
    server_type_name = models.CharField(max_length=125, default="NA")
    server_make  = models.CharField(max_length=125, default="NA")
    server_model = models.CharField(max_length=125, default="NA")
    server_processor = models.CharField(max_length=125, default="NA")
    server_socket = models.CharField(max_length=125, default="NA")
    server_core = models.CharField(max_length=125, default="NA")
    server_hdd_model = models.CharField(max_length=125, default="NA")
    server_hdd_size  = models.CharField(max_length=125, default="NA")
    server_hdd_number = models.CharField(max_length=125, default="NA")
    server_ram = models.CharField(max_length=125, default="NA")

    def __str__(self):
      return self.server_type_name
    
    class Meta:
      db_table = "server_type"

class Server(models.Model):
   # server_id = models.AutoField(primary_key=True , default=0)
    server_type_name = models.ForeignKey(ServerType, on_delete=models.PROTECT)
    server_name  = models.CharField(max_length=125, default="NA")
    #server_model = models.CharField(max_length=125, default="NA")
    server_serial_number = models.CharField(max_length=125, default="NA")
    server_po_number = models.CharField(max_length=125, default="NA")
    server_po_date = models.CharField(max_length=125, default="NA")
    server_vendor = models.CharField(max_length=125, default="NA")
    server_invoice  = models.CharField(max_length=125, default="NA")
    server_hdd_number = models.CharField(max_length=125, default="NA")
    server_bond = models.CharField(max_length=125, default="NA")
    server_bond_number = models.CharField(max_length=125, default="NA")
    server_type = models.CharField(max_length=125, default="NA")
    server_ship_date = models.CharField(max_length=125, default="NA")
    server_arrival_date = models.CharField(max_length=125, default="NA")
    server_warranty = models.CharField(max_length=125, default="NA")
    server_added_byuser = models.CharField(max_length=125, default="NA")
    server_added_ondate = models.CharField(max_length=125, default="NA")
    server_ownership = models.CharField(max_length=125, default="NA")
    server_ip_address = models.CharField(max_length=125, default="NA")
    server_hostname = models.CharField(max_length=125, default="NA")
    server_mgmt_mac = models.CharField(max_length=125, default="NA")
    server_lan_mac = models.CharField(max_length=125, default="NA")
    server_os = models.CharField(max_length=125, default="NA")
    server_fversion = models.CharField(max_length=125, default="NA")
    server_hardware_revision = models.CharField(max_length=125, default="NA")
    server_setup_id = models.CharField(max_length=125, default="NA")
    server_remark = models.CharField(max_length=125, default="NA")

    def __str__(self):
      return self.server_name
    
    class Meta:
      db_table = "add_server"
>>>>>>> main
