def add_devices(network_devices, *devices):
    for device in devices:
        network_devices.add(device)
    return network_devices
    
network_devices = {'Switch', 'Router', 'Firewall'}
network_devices = add_devices(network_devices, 'Load Balancer', 'Proxy Server')
print(network_devices)