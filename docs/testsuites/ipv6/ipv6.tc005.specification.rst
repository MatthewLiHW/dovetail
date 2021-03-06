.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) OPNFV and others

=====================================================================================
Dovetail IPv6 tc005 specification - Show Information of an IPv6 Network and Subnet
=====================================================================================

.. table::
   :class: longtable

+-----------------------+----------------------------------------------------------------------------------------------------+
|test case name         |show information of an IPv6 network and subnet                                                      |
|                       |                                                                                                    |
+-----------------------+----------------------------------------------------------------------------------------------------+
|id                     |dovetail.ipv6.tc005                                                                                 |
+-----------------------+----------------------------------------------------------------------------------------------------+
|objective              |VIM ipv6 operations, to show information of an IPv6 network and subnet                              |
+-----------------------+----------------------------------------------------------------------------------------------------+
|modules under test     |neutron, nova, etc                                                                                  |
+-----------------------+----------------------------------------------------------------------------------------------------+
|dependent test project |tempest(openstack)/functest(OPNFV)                                                                  |
+-----------------------+----------------------------------------------------------------------------------------------------+
|test items             |tempest.api.network.test_networks.NetworksIpV6Test.test_show_network                                |
|                       |{idempotent_id('2bf13842-c93f-4a69-83ed-717d2ec3b44e')}                                             |
|                       |tempest.api.network.test_networks.NetworksIpV6Test.test_show_subnet                                 |
|                       |{idempotent_id('bd635d81-6030-4dd1-b3b9-31ba0cfdf6cc')}                                             |
|                       |tempest.api.network.test_networks.NetworksIpV6TestAttrs.test_show_network                           |
|                       |{idempotent_id('2bf13842-c93f-4a69-83ed-717d2ec3b44e')}                                             |
|                       |tempest.api.network.test_networks.NetworksIpV6TestAttrs.test_show_subnet                            |
|                       |{idempotent_id('bd635d81-6030-4dd1-b3b9-31ba0cfdf6cc')}                                             |
+-----------------------+----------------------------------------------------------------------------------------------------+
|environmental          |                                                                                                    |
|requirements &         | environment can be deplyed on bare metal of virtualized infrastructure                             |
|preconditions          | deployment can be HA or non-HA                                                                     |
|                       |                                                                                                    |
+-----------------------+----------------------------------------------------------------------------------------------------+
|scenario dependencies  | NA                                                                                                 |
+-----------------------+----------------------------------------------------------------------------------------------------+
|procedural             |show network:                                                                                       |
|requirements           |     verify the details of a network                                                                |
|                       |show subnet:                                                                                        |
|                       |     verify the details of a subnet                                                                 |
|                       |                                                                                                    |
+-----------------------+----------------------------------------------------------------------------------------------------+
|input specifications   |NA                                                                                                  |
+-----------------------+----------------------------------------------------------------------------------------------------+
|output specifications  |success/fail                                                                                        |
+-----------------------+----------------------------------------------------------------------------------------------------+
|pass/fail criteria     |success                                                                                             |
+-----------------------+----------------------------------------------------------------------------------------------------+
|test report            | dovetail dashboard DB here                                                                         |
+-----------------------+----------------------------------------------------------------------------------------------------+
