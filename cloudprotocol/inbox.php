<?php
/*
 *  Show all Inbox Cloud Mails
 *
*/
require 'config.php';

if (isset($_POST['username'])&&!empty($_POST['username'])&&isset($_POST['password'])&&!empty($_POST['password'])) {
    $name = $_POST['name'];
    $username = $_POST['username'];
    $password = hash('sha3-512',$_POST['password']);

    $sql = "SELECT password FROM users WHERE username='$username'";
    $result = mysqli_query($conn,$sql);
    $array = mysqli_fetch_array ($result);

    if (isset($array)){
        if ($password==$array[0]){
            $sql = "SELECT * FROM mails WHERE giver='$username' ORDER BY id DESC";
            $result = mysqli_query($conn,$sql);
            $array = mysqli_fetch_array ($result);

            if (isset($array)){
                $result = $conn->query($sql);
                $arrylist=array();
                $array=$result->fetch_all(MYSQLI_ASSOC);
                echo json_encode($array);
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