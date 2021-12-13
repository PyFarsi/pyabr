<?php

require 'config.php';

$sender = $_POST['sender'];
$password = hash('ripemd160',$_POST['password']);
$giver = $_POST['giver'];

$sql = "SELECT password FROM users WHERE username='$sender'";
$result = mysqli_query ($conn,$sql);
$array = mysqli_fetch_array ($result);

if (isset($array))
{
    if ($array[0]==$password)
    {
        $sql = "SELECT fullname FROM users WHERE username='$giver'";
        $result = mysqli_query ($conn,$sql);
        $array = mysqli_fetch_array ($result);
        
        if (isset($array))
        {
            if ($sender==$giver)
            {
                echo '0';
            }
            else
            {
                $sql ="SELECT * FROM chats WHERE (sender='$sender' AND giver='$giver') OR (sender='$giver' AND giver='$sender') ORDER BY id DESC";
                $result = $conn->query($sql);
                $arrylist=array();
                $array=$result->fetch_all(MYSQLI_ASSOC);
                echo json_encode($array);
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
}

?>