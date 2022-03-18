<?php
/*
 *  Get direct link of shared files in Cloud Service
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
            $sql = "SELECT file FROM files WHERE username='$username' AND name='$name' ORDER BY id DESC";
            $result = mysqli_query($conn,$sql);
            $array = mysqli_fetch_array ($result);

            if (isset($array)){
                echo $array[0];
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
else {
    echo 'E0';
}

?>