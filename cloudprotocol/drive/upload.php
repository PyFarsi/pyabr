<?php
require 'config.php';

$uploaddir = 'files/';
$sentime = date("Y.m.d.h.i.sa");
$uploadfile = $uploaddir . hash('md5',time());
if (move_uploaded_file($_FILES['file']['tmp_name'], $uploadfile)){
    $sql = "INSERT INTO files (id,file) VALUES (NULL,'$uploadfile')";
    if (mysqli_query($conn,$sql)){
        echo '1';
    }
    else
    {
        echo '0';
    }
}
else
{
    echo '0';
}

?>