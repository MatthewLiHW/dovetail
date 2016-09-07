.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) OPNFV and others

================================================================================
Dovetail VIM operations tc072 specification - Ceilometer Samples and Meters List
================================================================================


.. table::
   :class: longtable

+---------------------------+---------------------------------------------------------------------------------------------------------------+
|test case                  |Ceilometer Samples and Meters List                                                                             |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|id                         |dovetail.vimops.tc072                                                                                          |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|objective                  |samples and meters list, ceilometer                                                                            |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|modules under test         |ceilometer                                                                                                     |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|dependent test project     |functest/tempest                                                                                               |  
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|test items                 |tempest.api.telemetry.test_telemetry_notification_api.                                                         |
|                           |TelemetryNotificationAPITestJSON.test_check_glance_v1_notifications                                            |
|                           |idempotent_id('04b10bfe-a5dc-47af-b22f-0460426bf498')                                                          |
|                           |tempest.api.telemetry.test_telemetry_notification_api.                                                         |
|                           |TelemetryNotificationAPITestJSON.test_check_nova_notification                                                  |
|                           |idempotent_id('d7f8c1c8-d470-4731-8604-315d3956caad')                                                          |
|                           |tempest.api.telemetry.test_telemetry_notification_api.                                                         |
|                           |TelemetryNotificationAPITestJSON.test_check_glance_v2_notifications                                            |
|                           |idempotent_id('c240457d-d943-439b-8aea-85e26d64fe8e')                                                          |
|                           |tempest.api.telemetry.test_telemetry_notification_api.                                                         |
|                           |TelemetryNotificationAdminAPITestJSON.test_check_nova_notification_event_and_meter                             |
|                           |idempotent_id('29604198-8b45-4fc0-8af8-1cae4f94ebe9')                                                          |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|environmental requirements |Openstack                                                                                                      |
|& preconditions            |                                                                                                               |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|scenario dependencies      |NA                                                                                                             |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|procedural requirements    |NA                                                                                                             |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|input specifications       |NA                                                                                                             |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|output specifications      |NA                                                                                                             |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|pass fail criteria         |All tests are passed                                                                                           |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|test report                |NA                                                                                                             |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
