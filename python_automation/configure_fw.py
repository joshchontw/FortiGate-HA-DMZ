from netmiko import ConnectHandler

primaryFW = {
    'host': '172.20.1.1',
    'username': 'admin',
    'password': 'password',
    'device_type': 'fortinet'
}

secondaryFW = {
    'host': '172.20.1.2',
    'username': 'admin',
    'password': 'password',
    'device_type': 'fortinet'
}


config_files = ["interface_config-primary.txt", "virtualIP_config.txt", "policy_config.txt", 
                "HA_config-primary.txt", "HA_config-secondary.txt", "interface_config-secondary.txt"]

print('Connecting')

net_connect = ConnectHandler(**primaryFW)
for file in config_files[0:4]:
    configurePrimary = net_connect.send_config_from_file(file)

net_connect = ConnectHandler(**secondaryFW)
for file in config_files[4:]:
    configureSecondary = net_connect.send_config_from_file(file)


print('Completed the configuration')