.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) OPNFV and others

==============================================================================
Dovetail IPv6 tc011 specification - Add Multiple Interfaces for an IPv6 Router
==============================================================================

.. table::
   :class: longtable

+-----------------------+----------------------------------------------------------------------------------------------------+
|test case name         |Add Multiple Interfaces for an IPv6 Router                                                          |
|                       |                                                                                                    |
+-----------------------+----------------------------------------------------------------------------------------------------+
|id                     |dovetail.ipv6.tc011                                                                                 |
+-----------------------+----------------------------------------------------------------------------------------------------+
|objective              |VIM ipv6 operations, to add multiple interfaces for an IPv6 router                                  |
+-----------------------+----------------------------------------------------------------------------------------------------+
|modules under test     |neutron, nova, etc                                                                                  |
+-----------------------+----------------------------------------------------------------------------------------------------+
|dependent test project |tempest(openstack)/functest(OPNFV)                                                                  |
+-----------------------+----------------------------------------------------------------------------------------------------+
|test items             |tempest.api.network.test_routers.RoutersIpV6Test.test_add_multiple_router_interfaces                |
|                       |idempotent_id('802c73c9-c937-4cef-824b-2191e24a6aab')                                               |
+-----------------------+----------------------------------------------------------------------------------------------------+
|environmental          |                                                                                                    |
|requirements &         | environment can be deplyed on bare metal of virtualized infrastructure                             |
|preconditions          | deployment can be HA or non-HA                                                                     |
|                       |                                                                                                    |
+-----------------------+----------------------------------------------------------------------------------------------------+
|scenario dependencies  | NA                                                                                                 |
+-----------------------+----------------------------------------------------------------------------------------------------+
|procedural             | 1,create 2 networks, 01 and 02                                                                     |
|requirements           | 2,create subnet 01 in network 01 and subnet 02 in network 02                                       |
|                       | 3,create one router                                                                                |
|                       | 4,add the router interface to subnet 01 and subnet 02 respectively                                 |
|                       | 5,verify the 2 router interface respectively                                                       |
+-----------------------+----------------------------------------------------------------------------------------------------+
|input specifications   |NA                                                                                                  |
+-----------------------+----------------------------------------------------------------------------------------------------+
|output specifications  |success/fail                                                                                        |
+-----------------------+----------------------------------------------------------------------------------------------------+
|pass/fail criteria     |success                                                                                             |
+-----------------------+----------------------------------------------------------------------------------------------------+
|test report            | dovetail dashboard DB here                                                                         |
+-----------------------+----------------------------------------------------------------------------------------------------+
