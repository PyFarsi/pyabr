<?php
/*
 *  Accept public key files via uploader user
 *
*/
require 'config.php';


if (isset($_POST['username'])&&!empty($_POST['username'])&&isset($_POST['password'])&&!empty($_POST['password']))
{
    $username = $_POST['username'];
    $password = hash('sha3-512',$_POST['password']);

    $sql = "SELECT id FROM files ORDER BY id DESC";
    $result = mysqli_query($conn,$sql);
    $array = mysqli_fetch_array ($result);

    $last = $array[0];

    $sql = "SELECT password FROM users WHERE username='$username'";
    $result = mysqli_query($conn,$sql);
    $array = mysqli_fetch_array ($result);

    if (isset($array)){
        if ($password==$array[0]){
            $sql = "SELECT file FROM files WHERE id='$last'";
            $result = mysqli_query($conn,$sql);
            $array  = mysqli_fetch_array($result);

            $file_ = $array[0];

            if (isset($array))
            {
                $sql = "UPDATE users SET public_key='$file_' WHERE username='$username'";
                if (mysqli_query($conn,$sql))
                {
                    echo 'S';
                }
                else
                {
                    echo 'E1';
                }
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