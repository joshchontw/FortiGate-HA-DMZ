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

config_files = ["interface_template/interface_config-primary.txt", "vip_policy_template/virtualIP_config.txt", 
                "vip_policy_template/policy_config.txt", "ha_template/HA_config-primary.txt", 
                "ha_template/HA_config-secondary.txt", "interface_template/interface_config-secondary.txt"]

print('Connecting')

net_connect = ConnectHandler(**primaryFW)
for file in config_files[0:4]:
    configurePrimary = net_connect.send_config_from_file(file)

net_connect = ConnectHandler(**secondaryFW)
for file in config_files[4:]:
    configureSecondary = net_connect.send_config_from_file(file)


print('Completed the configuration')