<?php

require 'config.php';

$username = $_POST['username'];
$password = hash('ripemd160',$_POST['password']);
$fullname = $_POST['fullname'];

$sql = "SELECT password FROM users WHERE username='$username'";
$result = mysqli_query ($conn,$sql);
$array = mysqli_fetch_array ($result);

if (isset($array))
{
    if ($array[0]==$password)
    {
        echo '1';
    }
    else
    {
        echo '0';
    }
}
else
{
    $sql = "INSERT INTO users (id,username,password,fullname) VALUES (NULL,'$username','$password','$fullname');";
    if (mysqli_query ($conn,$sql))
    {
        echo '1';
    }
    else
    {
        echo '0';
    }
}

?>