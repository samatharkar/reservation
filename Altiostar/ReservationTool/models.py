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


# class Device(models.Model):
#     hostname = models.CharField(max_length=125)
#     serial_number  = models.CharField(max_length=125)
#     ip = models.CharField(max_length=125)
#     mac = models.CharField(max_length=125)
#     device_type = models.CharField(max_length=125)
#     make = models.CharField(max_length=125)


#     def __str__(self):
#       return self.hostname
    
#     class Meta:
#       db_table = "devices"


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
    
    # class Meta:
    #   db_table = "server_type"

class Server(models.Model):
   # server_id = models.AutoField(primary_key=True , default=0)
    server_type_name = models.ForeignKey(ServerType, on_delete=models.PROTECT)
    server_name  = models.CharField(max_length=125, default="NA")
    #server_model = models.CharField(max_length=125, default="NA")
    server_serial_number = models.CharField(max_length=125, default="NA")
    server_po_number = models.CharField(max_length=125, default="NA")
    server_po_date = models.DateField()
    server_vendor = models.CharField(max_length=125, default="NA")
    server_invoice  = models.CharField(max_length=125, default="NA")
    server_hdd_number = models.CharField(max_length=125, default="NA")
    server_bond = models.CharField(max_length=125, default="NA")
    server_bond_number = models.CharField(max_length=125, default="NA")
    server_type = models.CharField(max_length=125, default="NA")
    server_ship_date = models.DateField()
    server_arrival_date = models.DateField()
    server_warranty = models.CharField(max_length=125, default="NA")
    server_added_byuser = models.CharField(max_length=125, default="NA")
    server_added_ondate = models.DateField()
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
    
    # class Meta:
    #   db_table = "add_server"



# class RrhType(models.Model):
#   #  server_type_id = models.AutoField(primary_key=True, default=0)
#    # rrh_id = models.CharField(max_length=10, default=uuid.uuid4)
#     rrh_type_name = models.CharField(max_length=125, default="NA")
#     rrh_part_number  = models.CharField(max_length=125, default="NA")
#     rrh_model_number = models.CharField(max_length=125, default="NA")
#     rrh_band = models.CharField(max_length=125, default="NA")
#     rrh_remark = models.CharField(max_length=125, default="NA")

#     def __str__(self):
#       return self.rrh_type_name
    
#     # class Meta:
#     #   db_table = "rrh_type"

# class RRH(models.Model):
#    # server_id = models.AutoField(primary_key=True , default=0)
#     rrh_type_name = models.ForeignKey(RrhType, on_delete=models.PROTECT)
#     rrh_name  = models.CharField(max_length=125, default="NA")
#     #rrh_model = models.CharField(max_length=125, default="NA")
#     rrh_serial_number = models.CharField(max_length=125, default="NA")
#     rrh_po_number = models.CharField(max_length=125, default="NA")
#     rrh_po_date = models.DateField()
#     rrh_vendor = models.CharField(max_length=125, default="NA")
#     rrh_invoice  = models.CharField(max_length=125, default="NA")
#     rrh_hdd_number = models.CharField(max_length=125, default="NA")
#     rrh_bond = models.CharField(max_length=125, default="NA")
#     rrh_bond_number = models.CharField(max_length=125, default="NA")
#     rrh_oftype = models.CharField(max_length=125, default="NA")
#     rrh_ship_date = models.DateField()
#     rrh_arrival_date = models.DateField()
#     rrh_warranty = models.CharField(max_length=125, default="NA")
#     rrh_added_byuser = models.CharField(max_length=125, default="NA")
#     rrh_added_ondate = models.DateField()
#     rrh_ownership = models.CharField(max_length=125, default="NA")
#     rrh_ip_address = models.CharField(max_length=125, default="NA")
#     rrh_hostname = models.CharField(max_length=125, default="NA")
#     rrh_mgmt_mac = models.CharField(max_length=125, default="NA")
#     rrh_lan_mac = models.CharField(max_length=125, default="NA")
#     rrh_os = models.CharField(max_length=125, default="NA")
#     rrh_fversion = models.CharField(max_length=125, default="NA")
#     rrh_hardware_revision = models.CharField(max_length=125, default="NA")
#     rrh_setup_id = models.CharField(max_length=125, default="NA")
#     rrh_remark = models.CharField(max_length=125, default="NA")

#     def __str__(self):
#       return self.rrh_name
    
#     # class Meta:
#     #   db_table = "add_rrh"