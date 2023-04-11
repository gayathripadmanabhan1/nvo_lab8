# nvo_lab8

For performing this lab, we neeed to use the following tools/technologies to implement automation for creationg of the network, VMs, Security groups.

1. BGP
2. Hypervisor (such as OpenStack)
3.Containers
4. SDN Controller
5. Hardware server

<img width="486" alt="Screenshot 2023-04-11 at 7 36 38 AM" src="https://user-images.githubusercontent.com/89698476/231180399-1a7104f7-a574-47b1-9049-f82374d5b0dc.png">

Objective 1: Automate the creation of multiple virtual networks (VNs) within the hypervisor and their connection to the public network
Options:
1. Create a Virtual Machine, Virtual Network
2. Create a Security Group
3. Run and Configure FRR/RYU BGP Router

Objective 2: Automate the creation of multiple VMs within the hypervisor-
a. Both single tenant (same VN) and multi-tenant (different VNs)

b. All VMs should be accessible from the host server and be able to access the Internet

Upon creation of VM, Floating IPs are automatically created and assigned to VM

Objective 3: Automate the security groups and port security configuration to make intra-VN and inter-VN communication possible
This security group configuration allows all intra-VN and inter-VN communication possible

Objective 4: Automate spinning up and configuring a Quagga/FRR BGP router as a Docker container
a. Automate its BGP configuration to peer with the SDN controller in the next objective. Enter the required IP Address and AS numbers

- docker pull cumulusnetworks/frrouting

$ docker pull cumulusnetworks/frrouting
$ docker run -t -d --net=host --privileged --name frr cumulusnetworks/frrouting:latest
$ docker exec -i -t frr /usr/bin/vtysh
$ show run


Objective 5: Automate spinning up and configuring an SDN controller as another Docker container
a. Automate its BGP speaker configuration to peer with Quagga/FRR. Enter the required IP Address and AS numbers and routes to be advertised to FRR

