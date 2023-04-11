# nvo_lab8

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

Objective 5: Automate spinning up and configuring an SDN controller as another Docker container
a. Automate its BGP speaker configuration to peer with Quagga/FRR. Enter the required IP Address and AS numbers and routes to be advertised to FRR

