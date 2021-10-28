<?php

$name = $_POST['name'];
$username = $_POST['username'];
$password = hash('ripemd160',$_POST['password']);

require 'config.php';

$sql = "SELECT password FROM users WHERE username='$username'";
$result = mysqli_query($conn,$sql);
$array = mysqli_fetch_array ($result);

if (isset($array)){
    if ($password==$array[0]){
        $sql = "SELECT file FROM files WHERE username='$username' AND name='$name' ORDER BY id DESC";
        $result = mysqli_query($conn,$sql);
        $array = mysqli_fetch_array ($result);
        
        if (isset($array)){
            echo $array[0];
        }
    }
}

?>