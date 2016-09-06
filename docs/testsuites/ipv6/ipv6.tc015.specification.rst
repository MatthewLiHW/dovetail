.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) OPNFV and others

================================================================================================
Dovetail IPv6 tc015 specification - Create, Update, Delete, List and Show an IPv6 Security Group
================================================================================================

.. table::
   :class: longtable

+-----------------------+--------------------------------------------------------------------------------------------------------------+
|test case name         |Create, Update, Delete, List and Show an IPv6 Security Group                                                  |
|                       |                                                                                                              |
+-----------------------+--------------------------------------------------------------------------------------------------------------+
|id                     |dovetail.ipv6.tc015                                                                                           |
+-----------------------+--------------------------------------------------------------------------------------------------------------+
|objective              |VIM ipv6 operations, to create, update, delete, list and show an IPv6 security group                          |
+-----------------------+--------------------------------------------------------------------------------------------------------------+
|modules under test     |neutron, nova, etc                                                                                            |
+-----------------------+--------------------------------------------------------------------------------------------------------------+
|dependent test project |tempest(openstack)/functest(OPNFV)                                                                            |
+-----------------------+--------------------------------------------------------------------------------------------------------------+
|test items             |tempest.api.network.test_security_groups.SecGroupIPv6Test.test_create_list_update_show_delete_security_group  |
|                       |idempotent_id('bfd128e5-3c92-44b6-9d66-7fe29d22c802')                                                         |
+-----------------------+--------------------------------------------------------------------------------------------------------------+
|environmental          |                                                                                                              |
|requirements &         | environment can be deplyed on bare metal of virtualized infrastructure                                       |
|preconditions          | deployment can be HA or non-HA                                                                               |
|                       |                                                                                                              |
+-----------------------+--------------------------------------------------------------------------------------------------------------+
|scenario dependencies  | NA                                                                                                           |
+-----------------------+--------------------------------------------------------------------------------------------------------------+
|procedural             | 1, List security groups and verify if created group is there in response                                     |
|requirements           | 2, Update the security group                                                                                 |
|                       | 3, Verify if security group is updated                                                                       |
|                       | 4, Show details of the updated security group                                                                |
+-----------------------+--------------------------------------------------------------------------------------------------------------+
|input specifications   |NA                                                                                                            |
+-----------------------+--------------------------------------------------------------------------------------------------------------+
|output specifications  |success/fail                                                                                                  |
+-----------------------+--------------------------------------------------------------------------------------------------------------+
|pass/fail criteria     |success                                                                                                       |
+-----------------------+--------------------------------------------------------------------------------------------------------------+
|test report            | dovetail dashboard DB here                                                                                   |
+-----------------------+--------------------------------------------------------------------------------------------------------------+
