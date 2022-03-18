<?php
require '../config.php';

$sql = "SELECT count(*) FROM counter";
$result = mysqli_query($conn,$sql);
$array = mysqli_fetch_array($result);

echo $array[0];

?>