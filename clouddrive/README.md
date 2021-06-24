### How to use Cloud drive in Webhost?

- Copy all files in `/clouddrive` into your **Host**.
- Edit **'/config.php'**
```php
<?php
/* Cloud Disk */

define ('password','your cloud drive password');
define ('rootpath','stor/');

?>
```
- Remove `/cloud.php`
- Connect to this cloud drive with **Pyabr**