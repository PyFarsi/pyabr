<?php

require 'config.php';

$username = $_POST['username'];
$password = hash('ripemd160',$_POST['password']);

$sql = "SELECT password FROM users WHERE username='$username'";
$result = mysqli_query($conn,$sql);
$array = mysqli_fetch_array ($result);

if (isset($array)){
    if ($password==$array[0]){
        echo '1';
    }
    else
    {
        echo '0';
    }
}
else {
    $sql = "INSERT INTO users (id,username,password) VALUES (NULL,'$username','$password');";
        
    if (mysqli_query($conn,$sql)){
        echo '1';
    }
    else
    {
        echo '0';
    }
}

?>