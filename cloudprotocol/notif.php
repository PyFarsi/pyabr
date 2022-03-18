<?php
/*
 *  Get all notifs
 *
*/
require 'config.php';

if (isset($_POST['username'])&&!empty($_POST['username'])&&isset($_POST['password'])&&!empty($_POST['password'])) {
    $username = $_POST['username'];
    $password = hash('sha3-512',$_POST['password']);

    $sql = "SELECT password FROM users WHERE username='$username'";
    $result = mysqli_query($conn,$sql);
    $array = mysqli_fetch_array ($result);

    if (isset($array)){
        if ($password==$array[0]){
            $sql = "SELECT id,title,text,app,open FROM notifications WHERE username='$username' ORDER BY id ASC";
            $result = mysqli_query($conn,$sql);
            $array = mysqli_fetch_array ($result);

            if (isset($array)){
                $id_ = $array[0];
                $title_ = $array[1];
                $text_ = $array[2];
                $app_ = $array[3];
                $open_ = $array[4];

                echo "$id_:::$title_:::$text_:::$app_:::$open_";

                $sql = "DELETE FROM notifications WHERE username='$username' AND id='$id_'";
                mysqli_query($conn,$sql);
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