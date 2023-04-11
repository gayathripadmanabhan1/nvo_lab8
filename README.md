# nvo_lab8

For performing this lab, we neeed to use the following tools/technologies to implement automation for creationg of the network, VMs, Security groups.

1. BGP
2. Hypervisor (such as OpenStack)
3.Containers
4. SDN Controller
5. Hardware server


Open Stack Implementation for automation is done in the following ways:
1. Create the network topology as in the lab for the same - Two VMs, private network space associated with it.
Steps executed after:
1. neutron net-create <network_name> -f json
2. neutron subnet-create --name <subnet_name> <network_name> <subnet [192.168.10.0/24]> -f json"
3. nova boot --flavor m1.tiny --image <vm_image_name> --min-count <vm_count> --nic net-id=<Netowrk_Id> <VM_Initial_Names>
4. neutron router-create <router_name> -f json
5. neutron router-gateway-set <router_name> public
6. neutron router-interface-add <router_id> <subnet_name>
7. neutron floatingip-create public -f json
8. neutron floatingip-associate <floating_ip_id> <vm_port_id>
9. ICMP: openstack security group rule create --protocol icmp <default_security_group_id> -f json

SSH: openstack security group rule create --protocol tcp --dst-port 22:22 <default_security_group_id> -f json



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

