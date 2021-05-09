## Cloud Drive v1

### How to connect this cloud drive in Pyabr?

#### In web host:
- Buy a PHP webhost
- Copy all this current directory files and directory  `clouddrive/PHP`
- Edit `config.php` and save it
```php
<?
define ('password','1400');     // Set your password
define ('rootpath','stor/');    // Set your rootpath
?>
```

#### In Pyabr:
- Create a file for example named "/dev/foo"
- Edit it
```text
host: https://example.com/
password: 1400
index: index.php
list: list.php
download: download.php
upload: upload.php
remove: remove.php
```
- Save it
- Mount this drive
```shell
mount foo
```