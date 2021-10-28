<?php

require 'config.php';

$me = $_POST['me'];
$username = $_POST['username'];
$password = hash('ripemd160',$_POST['password']);

$sql = "SELECT fullname,profile FROM users WHERE username='$username'";
$result = mysqli_query ($conn,$sql);
$array = mysqli_fetch_array ($result);

$fullname = $array[0];
$profile = $array[1];

$sql = "SELECT password FROM users WHERE username='$me'";
$result = mysqli_query ($conn,$sql);
$array = mysqli_fetch_array ($result);

if (isset($array)){
    if ($password==$array[0]){
        $sql = "INSERT INTO contacts (id,me,username,fullname,profile) VALUES (NULL,'$me','$username','$fullname','$profile');";
         mysqli_query ($conn,$sql);
         
        $sql = "SELECT fullname,profile FROM users WHERE username='$me'";
        $result = mysqli_query ($conn,$sql);
        $array = mysqli_fetch_array ($result);
        
        $fullname = $array[0];
        $profile = $array[1];
        
        $sql = "INSERT INTO contacts (id,me,username,fullname,profile) VALUES (NULL,'$username','$me','$fullname','$profile');";
        mysqli_query ($conn,$sql);
    }
}


?>