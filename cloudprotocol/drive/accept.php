<?php

require 'config.php';

$name = $_POST['name'];
$username = $_POST['username'];
$password = hash('ripemd160',$_POST['password']);

$sql = "SELECT id FROM files ORDER BY id DESC";
$result = mysqli_query($conn,$sql);
$array = mysqli_fetch_array ($result);

$last = $array[0];

$sql = "SELECT password FROM users WHERE username='$username'";
$result = mysqli_query($conn,$sql);
$array = mysqli_fetch_array ($result);

if (isset($array)){
    if ($password==$array[0]){
        $sql = "UPDATE files SET username='$username',name='$name' WHERE id='$last'";

        if (mysqli_query($conn,$sql)){
            echo '1';
        }
        else {
            echo '0';
        }

    }
    else
    {
        echo '0';
    }
}
?>