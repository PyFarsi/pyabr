<?php
/*
 *  Push your projects into Cloud
 *
*/
require 'config.php';

if (isset($_POST['username'])&&!empty($_POST['username'])&&isset($_POST['password'])&&!empty($_POST['password'])&&isset($_POST['name'])&&!empty($_POST['name'])) {
    $name = $_POST['name'];
    $username = $_POST['username'];
    $password = hash('sha3-512',$_POST['password']);

    $sql = "SELECT file FROM files ORDER BY id DESC";
    $result = mysqli_query($conn,$sql);
    $array = mysqli_fetch_array ($result);

    $last = $array[0];

    $sql = "SELECT password FROM users WHERE username='$username'";
    $result = mysqli_query($conn,$sql);
    $array = mysqli_fetch_array ($result);

    if (isset($array)){
        if ($password==$array[0]){
            $sql = "SELECT * FROM packages WHERE name='$name'";
            $result = mysqli_query($conn,$sql);
            $array = mysqli_fetch_array ($result);

            if (isset($array)){
                $sql = "UPDATE packages SET link='$last',merge='0' WHERE name='$name' AND username='$username'";

                if (mysqli_query($conn,$sql)){
                    echo 'S';
                }
                else {
                    echo 'E1';
                }
            }
            else {
                $sql = "INSERT INTO packages (name,username,link,merge) VALUES ('$name','$username','$last','0')";

                if (mysqli_query($conn,$sql)){
                    echo 'S';
                }
                else {
                    echo 'E1';
                }
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