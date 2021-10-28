<?php
require 'config.php';

$username = $_POST['username'];
$password = hash('ripemd160',$_POST['password']);

$fullname = $_POST['fullname'];
$profile = $_POST['profile'];

$sql = "SELECT file FROM files ORDER BY id DESC";
$result = mysqli_query($conn,$sql);
$array = mysqli_fetch_array ($result);

$public_key = $array[0];

$sql = "SELECT password FROM users WHERE username='$username'";
$result = mysqli_query($conn,$sql);
$array = mysqli_fetch_array ($result);

if (isset($array)){
    if ($array[0]==$password){
        echo '1';
    }
    else
    {
        echo '0';
    }
}
else
{
    $sql = "INSERT INTO users (id,username,public_key,password,fullname,profile) VALUES (NULL,'$username','$public_key','$password','$fullname','$profile');";
    if ( mysqli_query($conn,$sql)){
        echo '1';
    }
    else
    {
        echo '0';
    }
}

?>