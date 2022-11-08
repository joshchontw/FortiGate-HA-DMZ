## FortiGate Firewalls

In this lab, two FortiGate firewalls will be operating in active-passive (high-availability) mode. They will be in front of a DMZ and internal network. An outside user will be able to access the webserver, but not the internal router. Python is used to automate the provisioning of the firewalls.

![image](https://user-images.githubusercontent.com/81763406/199127293-3d343ce7-f577-4bc0-b24f-686d591ceba6.png)
---
### High availability configuration
![image](https://user-images.githubusercontent.com/81763406/200664677-a1afd4c9-001b-46fb-bd1b-48d19689a1a4.png)

If the primary firewall goes down, the secondary becomes the master ***at the same IP address as the primary***.

>*This is after shutting down the primary firewall*:
![image](https://user-images.githubusercontent.com/81763406/200664894-926d7e34-f462-4efd-b0ac-2eac20f92460.png)

***Notice the secondary firewall becomes the master at the IP address of the primary firewall***.

---
### External User accessing the webserver
![image](https://user-images.githubusercontent.com/81763406/200662257-6858656d-387a-4fa5-9286-d2f6e171ecc2.png)

>*The external user initiates a connection to a virtual IP setup on the firewalls*:
![image](https://user-images.githubusercontent.com/81763406/200665562-4fea442c-4971-4006-9217-b481f82347a6.png)
>
>The IP address on the external network (172.20.1.200) maps to the webserver's DMZ network address of 192.168.2.2. 

>*The final step to allow the connection is via an IPv4 policy*:
>
>![image](https://user-images.githubusercontent.com/81763406/200666129-2c6d96e8-c707-4041-8b63-888ff3eb7b03.png)
>
>The traffic coming in from the external user arrives at the WAN (external) interface, gets sent into the DMZ via the DMZ interface, to the webserver on port 443. As there was no route to the extneral user configured on the webserver, the NAT option must be enabled, for the firewall to be the proxy.

---
### Internal router SSH into the webserver
![image](https://user-images.githubusercontent.com/81763406/200663089-80f143ff-72b2-4a98-b98d-da422a27a612.png)

***This setup follows the same principles as the external to DMZ connection, just with a different VIP and IPv4 policy.***

>*VIP of the webserver for the SSH profile*:
>
>![image](https://user-images.githubusercontent.com/81763406/200668063-134f7932-794a-49c4-b4dd-a1b44052b68e.png)

>*IPv4 policy for the internal network to DMZ connection*:
>
>![image](https://user-images.githubusercontent.com/81763406/200668509-954ccb21-1a52-40a3-878b-85fbf0138caf.png)


