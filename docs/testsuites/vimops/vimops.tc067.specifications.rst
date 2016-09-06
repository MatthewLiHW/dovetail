.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. (c) OPNFV and others

===================================================================
Dovetail VIM operations tc067 specification - Glance Images v2 Get 
===================================================================


.. table::
   :class: longtable

+---------------------------+---------------------------------------------------------------------------------------------------------------+
|test case                  |Glance Images v2 Get                                                                                           |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|id                         |dovetail.vimops.tc067                                                                                          |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|objective                  |images get, glance                                                                                             |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|modules under test         |glance                                                                                                         |
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|dependent test project     |functest/tempest                                                                                               |  
+---------------------------+---------------------------------------------------------------------------------------------------------------+
|test items                 |tempest.api.image.v2.test_images.ListImagesTest.test_get_image_schema                                          |
|                           |"idempotent_id": "id-622b925c-479f-4736-860d-adeaf13bc371"                                                     |
|                           |tempest.api.image.v2.test_images.ListImagesTest.test_get_images_schema                                         |
|                           |"idempotent_id": "id-25c8d7b2-df21-460f-87ac-93130bcdc684"                                                     |
|                           |tempest.api.image.v2.test_images_member.ImagesMemberTest.test_get_image_member                                 |
|                           |"idempotent_id": "id-a6ee18b9-4378-465e-9ad9-9a6de58a3287"                                                     |
|                           |tempest.api.image.v2.test_images_member.ImagesMemberTest.test_get_image_member_schema                          |
|                           |"idempotent_id": "id-634dcc3f-f6e2-4409-b8fd-354a0bb25d83"                                                     |
|                           |tempest.api.image.v2.test_images_member.ImagesMemberTest.test_get_image_members_schema                         |
|                           |"idempotent_id": "id-6ae916ef-1052-4e11-8d36-b3ae14853cbb"                                                     |
|                           |tempest.api.image.v2.test_images_negative.ImagesNegativeTest.test_get_delete_deleted_image                     |
|                           |"idempotent_id": "id-e57fc127-7ba0-4693-92d7-1d8a05ebcba9"                                                     |
|                           |tempest.api.image.v2.test_images_negative.ImagesNegativeTest.test_get_image_null_id                            |
|                           |"idempotent_id": "id-ef45000d-0a72-4781-866d-4cb7bf2562ad"                                                     |
|                           |tempest.api.image.v2.test_images_negative.ImagesNegativeTest.test_get_non_existent_image                       |
|                           |"idempotent_id": "id-668743d5-08ad-4480-b2b8-15da34f81d9f"                                                     |
|                           |tempest.api.image.v2.test_images_member.ImagesMemberTest.test_get_private_image                                |
|                           |"idempotent_id": "id-cb961424-3f68-4d21-8e36-30ad66fb6bfb"                                                     |
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
