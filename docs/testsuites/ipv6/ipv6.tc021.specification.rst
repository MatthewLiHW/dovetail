.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) OPNFV and others

=============================================================================================================
Dovetail IPv6 tc021 specification - IPv6 Address Assignment - Dual Stack, Multiple Prefixes, DHCPv6 Stateless
=============================================================================================================

.. table::
   :class: longtable

+-----------------------+----------------------------------------------------------------------------------------------------+
|test case name         |IPv6 Address Assignment - Dual Stack, Multiple Prefixes, DHCPv6 Stateless                           |
|                       |                                                                                                    |
+-----------------------+----------------------------------------------------------------------------------------------------+
|id                     |dovetail.ipv6.tc021                                                                                 |
+-----------------------+----------------------------------------------------------------------------------------------------+
|objective              |VIM ipv6 operations, to do IPv6 Address Assignment - Dual Stack, Multiple Prefixes, DHCPv6 Stateless|
+-----------------------+----------------------------------------------------------------------------------------------------+
|modules under test     |neutron, nova, etc                                                                                  |
+-----------------------+----------------------------------------------------------------------------------------------------+
|dependent test project |tempest(openstack)/functest(OPNFV)                                                                  |
+-----------------------+----------------------------------------------------------------------------------------------------+
|test items             |tempest.scenario.test_network_v6.TestGettingAddress.test_dualnet_multi_prefix_dhcpv6_stateless      |
|                       |idempotent_id('cf1c4425-766b-45b8-be35-e2959728eb00')                                               |
+-----------------------+----------------------------------------------------------------------------------------------------+
|environmental          |                                                                                                    |
|requirements &         | environment can be deplyed on bare metal of virtualized infrastructure                             |
|preconditions          | deployment can be HA or non-HA                                                                     |
|                       |                                                                                                    |
+-----------------------+----------------------------------------------------------------------------------------------------+
|scenario dependencies  | NA                                                                                                 |
+-----------------------+----------------------------------------------------------------------------------------------------+
|procedural             | 1. Create network with subnets:                                                                    |
|requirements           |    1.1. one IPv4 and                                                                               |
|                       |    1.2. one or more IPv6 in a given address mode                                                   |
|                       | 2. Boot 2 VMs on this network                                                                      |
|                       | 3. Allocate and assign 2 FIP4                                                                      |
|                       | 4. Check that vNICs of all VMs gets all addresses actually assigned                                |
|                       | 5. Each VM will ping the other's v4 private address                                                |
|                       | 6. If ping6 available in VM, each VM will ping all of the other's  v6                              |
|                       |    addresses as well as the router's                                                               |
|                       |                                                                                                    |
+-----------------------+----------------------------------------------------------------------------------------------------+
|input specifications   |address6_mode='dhcpv6-stateless', n_subnets6=2, dualnet=True                                        |
+-----------------------+----------------------------------------------------------------------------------------------------+
|output specifications  |success/fail                                                                                        |
+-----------------------+----------------------------------------------------------------------------------------------------+
|pass/fail criteria     |success                                                                                             |
+-----------------------+----------------------------------------------------------------------------------------------------+
|test report            | dovetail dashboard DB here                                                                         |
+-----------------------+----------------------------------------------------------------------------------------------------+
