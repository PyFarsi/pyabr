<?php
/*
 *  Get public key of others
 *
*/
require 'config.php';

if (isset($_POST['username'])&&!empty($_POST['username']))
{
    $username = $_POST['username'];
    $sql = "SELECT public_key FROM users WHERE username='$username'";
    $result = mysqli_query($conn,$sql);
    $array  = mysqli_fetch_array ($result);
    
    if (isset($array)){
        echo $array[0];
    }
    else
    {
        echo 'E4';
    }
}
else
{
    echo 'E0';
}
?>