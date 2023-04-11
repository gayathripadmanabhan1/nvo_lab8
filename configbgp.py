from __future__ import absolute_import
import os
from ryu.services.protocols.bgp.bgpspeaker import RF_VPN_V4
from ryu.services.protocols.bgp.bgpspeaker import RF_VPN_V6
from ryu.services.protocols.bgp.bgpspeaker import RF_L2_EVPN
from ryu.services.protocols.bgp.bgpspeaker import RF_VPNV4_FLOWSPEC
from ryu.services.protocols.bgp.bgpspeaker import RF_VPNV6_FLOWSPEC
from ryu.services.protocols.bgp.bgpspeaker import RF_L2VPN_FLOWSPEC
from ryu.services.protocols.bgp.bgpspeaker import EVPN_MAX_ET
from ryu.services.protocols.bgp.bgpspeaker import ESI_TYPE_LACP
from ryu.services.protocols.bgp.bgpspeaker import ESI_TYPE_MAC_BASED
from ryu.services.protocols.bgp.bgpspeaker import EVPN_ETH_AUTO_DISCOVERY
from ryu.services.protocols.bgp.bgpspeaker import EVPN_MAC_IP_ADV_ROUTE
from ryu.services.protocols.bgp.bgpspeaker import TUNNEL_TYPE_VXLAN
from ryu.services.protocols.bgp.bgpspeaker import EVPN_MULTICAST_ETAG_ROUTE
from ryu.services.protocols.bgp.bgpspeaker import EVPN_ETH_SEGMENT
from ryu.services.protocols.bgp.bgpspeaker import EVPN_IP_PREFIX_ROUTE
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_FAMILY_IPV4
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_FAMILY_IPV6
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_FAMILY_VPNV4
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_FAMILY_VPNV6
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_FAMILY_L2VPN
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_TA_SAMPLE
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_TA_TERMINAL
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_VLAN_POP
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_VLAN_PUSH
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_VLAN_SWAP
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_VLAN_RW_INNER
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_VLAN_RW_OUTER
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_TPID_TI
from ryu.services.protocols.bgp.bgpspeaker import FLOWSPEC_TPID_TO
from ryu.services.protocols.bgp.bgpspeaker import REDUNDANCY_MODE_SINGLE_ACTIVE
# =============================================================================
# BGP configuration.
# =============================================================================
BGP = {
    # AS number for this BGP instance.
    'local_as': 20,
    # BGP Router ID.
    'router_id': '172.17.0.3',
    # Default local preference
    #'local_pref': 100,
    # List of TCP listen host addresses.
    'bgp_server_hosts': ['0.0.0.0', '::'],
    # List of BGP neighbors.
    # The parameters for each neighbor are the same as the arguments of
    # BGPSpeaker.neighbor_add() method.
    'neighbors': [
        {
            'address': 172.17.0.2,
            'remote_as': 10,
            'enable_ipv4': True,
            'enable_ipv6': True,
        },
    ],
    
}
# =============================================================================
# SSH server configuration.
# =============================================================================
SSH = {
    'ssh_port': 4990,
    'ssh_host': 'localhost',
   
}
