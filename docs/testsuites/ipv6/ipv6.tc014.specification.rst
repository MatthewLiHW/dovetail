.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) OPNFV and others

========================================================================================
Dovetail IPv6 tc014 specification - Create, Update, Delete, List and Show an IPv6 Router
========================================================================================

.. table::
   :class: longtable

+-----------------------+----------------------------------------------------------------------------------------------------+
|test case name         |Create, Update, Delete, List and Show an IPv6 Router                                                |
|                       |                                                                                                    |
+-----------------------+----------------------------------------------------------------------------------------------------+
|id                     |dovetail.ipv6.tc014                                                                                 |
+-----------------------+----------------------------------------------------------------------------------------------------+
|objective              |VIM ipv6 operations, to create, update, delete, list and show an IPv6 router                        |
+-----------------------+----------------------------------------------------------------------------------------------------+
|modules under test     |neutron, nova, etc                                                                                  |
+-----------------------+----------------------------------------------------------------------------------------------------+
|dependent test project |tempest(openstack)/functest(OPNFV)                                                                  |
+-----------------------+----------------------------------------------------------------------------------------------------+
|test items             |tempest.api.network.test_routers.RoutersIpV6Test.test_create_show_list_update_delete_router         |
|                       |idempotent_id('f64403e2-8483-4b34-8ccd-b09a87bcc68c')                                               |
+-----------------------+----------------------------------------------------------------------------------------------------+
|environmental          |                                                                                                    |
|requirements &         | environment can be deplyed on bare metal of virtualized infrastructure                             |
|preconditions          | deployment can be HA or non-HA                                                                     |
|                       |                                                                                                    |
+-----------------------+----------------------------------------------------------------------------------------------------+
|scenario dependencies  | NA                                                                                                 |
+-----------------------+----------------------------------------------------------------------------------------------------+
|procedural             | 1, create a router                                                                                 |
|requirements           | 2, show the details of the created router                                                          |
|                       | 3, list routers and verify if created router is there in response                                  |
|                       | 4, update the name of router and verify if it is updated                                           |
+-----------------------+----------------------------------------------------------------------------------------------------+
|input specifications   |NA                                                                                                  |
+-----------------------+----------------------------------------------------------------------------------------------------+
|output specifications  |success/fail                                                                                        |
+-----------------------+----------------------------------------------------------------------------------------------------+
|pass/fail criteria     |success                                                                                             |
+-----------------------+----------------------------------------------------------------------------------------------------+
|test report            | dovetail dashboard DB here                                                                         |
+-----------------------+----------------------------------------------------------------------------------------------------+
