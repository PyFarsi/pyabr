<?php
/*
 *  Send cloud mail
 *
*/
require 'config.php';

if (isset($_POST['sender'])&&!empty($_POST['sender'])&&isset($_POST['password'])&&!empty($_POST['password'])&&isset($_POST['subject'])&&!empty($_POST['subject'])&&isset($_POST['giver'])&&!empty($_POST['giver'])) {
    $subject = $_POST['subject'];
    $sender = $_POST['sender'];
    $giver = $_POST['giver'];
    $password = hash('sha3-512',$_POST['password']);

    $sql = "SELECT file FROM files ORDER BY id DESC";
    $result = mysqli_query($conn,$sql);
    $array = mysqli_fetch_array ($result);

    $last = $array[0];

    $sql = "SELECT password FROM users WHERE username='$sender'";
    $result = mysqli_query($conn,$sql);
    $array = mysqli_fetch_array ($result);
    

    if (isset($array)){
        if ($password==$array[0]){
            $sql = "SELECT password FROM users WHERE username='$giver'";
            $result = mysqli_query($conn,$sql);
            $array = mysqli_fetch_array ($result);

            if (isset($array))
            {
                $sql = "INSERT INTO mails (id,subject,sender,giver,data) VALUES (NULL,'$subject','$sender','$giver','$last')";

                if (mysqli_query($conn,$sql)){
                    echo 'S';
                }
                else {
                    echo 'E1';
                }
            }
            else
            {
                echo 'E4';   
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