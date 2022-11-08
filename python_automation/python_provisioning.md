## Python automation

Python, with the help of files with details of the different objects to be created, will automate the provisioning of the two firewalls in a high-availability mode.

The only pre-requisite to the whole operation is to manually define the management and high-availibility interfaces of the two firewalls. Doing this will ensure the Python controller connects to the devices via SSH and applies the configuration.

>Before applying the configuration, there are *only two interfaces defined*:
![image](https://user-images.githubusercontent.com/81763406/200683231-eee03bae-02e4-48ab-b691-504b1038befe.png)

>After applying, *all four interfaces are defined*:
![Animation](https://user-images.githubusercontent.com/81763406/200684702-9639365f-2396-4ec6-ab72-a22d0aa8e03f.gif)

*Although not shown, all other relevant objects were also created thanks to the script.*

---
### Code

![image](https://user-images.githubusercontent.com/81763406/200685248-037b9dd8-78ee-4526-ab90-6a7eb21dc030.png)

The library leveraged is netmiko. This allows the machine to SSH into the devices and apply the configurations defined. The two firewalls and their credentials are defined.

![image](https://user-images.githubusercontent.com/81763406/200686050-8cbcefe6-19d8-4a62-8e1c-005e22e17727.png)

All configuration files are defined with their proper locations. 

![image](https://user-images.githubusercontent.com/81763406/200686348-66ac0b0f-fc21-46cd-b691-782d2cfb6ab5.png)

To take one example template file, this defines the two policies needed. One is for the outside user to access the DMZ, and the other is for the internal network to access the DMZ.

![image](https://user-images.githubusercontent.com/81763406/200686694-0b19c018-14a3-4913-b615-1424c72ab6d2.png)

The final block of code allows the connections to the devices and applies the configurations in the template files.
