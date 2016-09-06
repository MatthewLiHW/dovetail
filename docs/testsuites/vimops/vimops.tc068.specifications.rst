.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) OPNFV and others

===================================================================
Dovetail VIM operations tc068 specification - Glance Images v2 list
===================================================================


.. table::
   :class: longtable

+---------------------------+---------------------------------------------------------------------------------------------------------------+
|test case                  |Glance Images v2 list                                                                                          |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|id                         |dovetail.vimops.tc068                                                                                          |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|objective                  |images list, glance                                                                                            |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|modules under test         |glance                                                                                                         |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|dependent test project     |functest/tempest                                                                                               |  
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|test items                 |tempest.api.image.v2.test_images.ListImagesTest.test_list_images_param_container_format                        |
|                           |"idempotent_id": "id-9959ca1d-1aa7-4b7a-a1ea-0fff0499b37e"                                                     |
|                           |tempest.api.image.v2.test_images.ListImagesTest.test_list_images_param_disk_format                             |
|                           |"idempotent_id": "id-4a4735a7-f22f-49b6-b0d9-66e1ef7453eb"                                                     |
|                           |tempest.api.image.v2.test_images.ListImagesTest.test_list_images_param_limit                                   |
|                           |"idempotent_id": "id-e914a891-3cc8-4b40-ad32-e0a39ffbddbb"                                                     |
|                           |tempest.api.image.v2.test_images.ListImagesTest.test_list_images_param_min_max_size                            |
|                           |"idempotent_id": "id-4ad8c157-971a-4ba8-aa84-ed61154b1e7f"                                                     |
|                           |tempest.api.image.v2.test_images.ListImagesTest.test_list_images_param_size                                    |
|                           |"idempotent_id": "id-cf1b9a48-8340-480e-af7b-fe7e17690876"                                                     |
|                           |tempest.api.image.v2.test_images.ListImagesTest.test_list_images_param_status                                  |
|                           | "idempotent_id": "id-7fc9e369-0f58-4d05-9aa5-0969e2d59d15"                                                    |
|                           |tempest.api.image.v2.test_images.ListImagesTest.test_list_images_param_visibility                              |
|                           |"idempotent_id": "id-7a95bb92-d99e-4b12-9718-7bc6ab73e6d2"                                                     |
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
