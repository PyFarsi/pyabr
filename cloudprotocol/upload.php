<?php
/*
 *  Upload files
 *
*/
require 'config.php';

$uploaddir = 'files/';
$sentime = date("Y.m.d.h.i.sa");
$uploadfile = $uploaddir . hash('md5',time());
if (move_uploaded_file($_FILES['file']['tmp_name'], $uploadfile)){
    $sql = "INSERT INTO files (id,file) VALUES (NULL,'$uploadfile')";
    if (mysqli_query($conn,$sql)){
        echo 'S';
    }
    else
    {
        echo 'E1';
    }
}
else
{
    echo 'E3';
}

?>