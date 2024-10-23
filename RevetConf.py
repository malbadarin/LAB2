import pyeapi

# Connect to Arista device
connection = pyeapi.connect(host='192.168.8.101', username='cvpadmin', password='cvpadmin123', transport='https')
connection.enable() 
# Save the running configuration to flash:init-config
output = connection.execute(['show running-config'], encoding='text')
# Output the result
print(output)
