<?php
require 'config.php';

$version = $_POST['version'];
$date = date("Y-m-d");

$sql = "INSERT INTO counter (id,version,date) VALUES (NULL,'$version','$date')";
mysqli_query ($conn,$sql);

?>