<?php
/*
 *  Remove files from Cloud
 *
*/
require 'config.php';

if (isset($_POST['username'])&&!empty($_POST['username'])&&isset($_POST['password'])&&!empty($_POST['password'])&&isset($_POST['name'])&&!empty($_POST['name'])) {
    $name = $_POST['name'];
    $username = $_POST['username'];
    $password = hash('sha3-512',$_POST['password']);

    $sql = "SELECT password FROM users WHERE username='$username'";
    $result = mysqli_query($conn,$sql);
    $array = mysqli_fetch_array ($result);

    if (isset($array)){
        if ($password==$array[0]){
            $sql = "SELECT file FROM files WHERE name='$name' AND username='$username' ORDER BY id DESC";
            $result = mysqli_query($conn,$sql);
            $array = mysqli_fetch_array ($result);

            if (isset($array))
            {
                unlink ($array[0]);
                echo 'S';
            }
            else
            {
                echo 'E6';
            }
        }
        else
        {
            echo 'E5';
        }
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