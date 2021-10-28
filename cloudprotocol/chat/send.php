<?php
require 'config.php';

$sender = $_POST['sender'];
$giver = $_POST['giver'];
$password = hash('ripemd160',$_POST['password']);

$sql = "SELECT password FROM users WHERE username='$sender'";
$result = mysqli_query($conn,$sql);
$array = mysqli_fetch_array ($result);

if (isset($array)){
    if ($array[0]==$password){
        $sql = "SELECT file FROM files ORDER BY id DESC";
        $result = mysqli_query($conn,$sql);
        $array = mysqli_fetch_array ($result);
        
        $file = $array[0];
        
        $sql = "INSERT INTO chats (id,sender,giver,data) VALUES (NULL,'$sender','$giver','$file');";
        
        if (mysqli_query($conn,$sql)){
            echo "$file";
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
}
else 
{
    echo '0';
}

?>