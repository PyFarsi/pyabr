<?php

require 'config.php';

$username = $_POST['username'];

$sql = "SELECT public_key FROM users WHERE username='$username'";
$result = mysqli_query ($conn,$sql);
$array = mysqli_fetch_array ($result);

echo $array[0];

?>