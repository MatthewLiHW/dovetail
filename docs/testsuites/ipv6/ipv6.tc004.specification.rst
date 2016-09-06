.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) OPNFV and others

==================================================================================
Dovetail IPv6 tc004 specification - List IPv6 Networks and Subnets of a Tenant
==================================================================================

.. table::
   :class: longtable

+-----------------------+----------------------------------------------------------------------------------------------------+
|test case name         |list IPv6 networks and subnets of a tenant                                                          |
|                       |                                                                                                    |
+-----------------------+----------------------------------------------------------------------------------------------------+
|id                     |dovetail.ipv6.tc004                                                                                 |
+-----------------------+----------------------------------------------------------------------------------------------------+
|objective              |VIM ipv6 operations, to list IPv6 networks and subnets of a tenant                                  |
+-----------------------+----------------------------------------------------------------------------------------------------+
|modules under test     |neutron, nova, etc                                                                                  |
+-----------------------+----------------------------------------------------------------------------------------------------+
|dependent test project |tempest(openstack)/functest(OPNFV)                                                                  |
+-----------------------+----------------------------------------------------------------------------------------------------+
|test items             |tempest.api.network.test_networks.NetworksIpV6Test.test_list_networks                               |
|                       |idempotent_id('f7ffdeda-e200-4a7a-bcbe-05716e86bf43')                                               |
|                       |tempest.api.network.test_networks.NetworksIpV6Test.test_list_subnets                                |
|                       |idempotent_id('db68ba48-f4ea-49e9-81d1-e367f6d0b20a')                                               |
|                       |tempest.api.network.test_networks.NetworksIpV6TestAttrs.test_list_networks                          |
|                       |idempotent_id('f7ffdeda-e200-4a7a-bcbe-05716e86bf43')                                               |
|                       |tempest.api.network.test_networks.NetworksIpV6TestAttrs.test_list_subnets                           |
|                       |idempotent_id('db68ba48-f4ea-49e9-81d1-e367f6d0b20a')                                               |
+-----------------------+----------------------------------------------------------------------------------------------------+
|environmental          |                                                                                                    |
|requirements &         | environment can be deplyed on bare metal of virtualized infrastructure                             |
|preconditions          | deployment can be HA or non-HA                                                                     |
|                       |                                                                                                    |
+-----------------------+----------------------------------------------------------------------------------------------------+
|scenario dependencies  | NA                                                                                                 |
+-----------------------+----------------------------------------------------------------------------------------------------+
|procedural             |list networks:                                                                                      |
|requirements           |     verify the networks exists in the list of all networks                                         |
|                       |list subnets:                                                                                       |
|                       |     verify the subnet exists in the list of all subnets                                            |
+-----------------------+----------------------------------------------------------------------------------------------------+
|input specifications   |NA                                                                                                  |
+-----------------------+----------------------------------------------------------------------------------------------------+
|output specifications  |success/fail                                                                                        |
+-----------------------+----------------------------------------------------------------------------------------------------+
|pass/fail criteria     |success                                                                                             |
+-----------------------+----------------------------------------------------------------------------------------------------+
|test report            | dovetail dashboard DB here                                                                         |
+-----------------------+----------------------------------------------------------------------------------------------------+
