.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) OPNFV and others

======================================================================
Dovetail VIM operations tc071 specification - Glance Images v2 Update 
======================================================================


.. table::
   :class: longtable

+---------------------------+---------------------------------------------------------------------------------------------------------------+
|test case                  |Glance Images v2 Update                                                                                        |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|id                         |dovetail.vimops.tc071                                                                                          |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|objective                  |Image update tests using the Glance v2 API                                                                     |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|modules under test         |glance                                                                                                         |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|dependent test project     |functest/tempest                                                                                               |  
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|test items                 |tempest.api.image.v2.test_images.BasicOperationsImagesTest.test_update_image                                   |
|                           |"idempotent_id": "id-f66891a7-a35c-41a8-b590-a065c2a1caa6"                                                     |
|                           |tempest.api.image.v2.test_images_tags.ImagesTagsTest.test_update_delete_tags_for_image                         |
|                           |"idempotent_id": "id-10407036-6059-4f95-a2cd-cbbbee7ed329"                                                     |
|                           |tempest.api.image.v2.test_images_tags_negative.ImagesTagsNegativeTest.test_update_tags_for_non_existing_image  |
|                           |"idempotent_id": "id-8cd30f82-6f9a-4c6e-8034-c1b51fba43d9"                                                     |
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
