<?php
require 'config.php';

$sender = $_POST['sender'];
$giver = $_POST['giver'];
$password = hash('ripemd160',$_POST['password']);

$sql = "SELECT password FROM users WHERE username='$sender'";
$result = mysqli_query($conn,$sql);
$array = mysqli_fetch_array ($result);

if (isset($array))
{

    if ($array[0]==$password){
        $sql ="SELECT * FROM `chats` WHERE (sender='$sender' AND giver='$giver') OR (sender='$giver' AND giver='$sender') ORDER BY id DESC";
        $result = $conn->query($sql);
        
        $arrylist=array();
        $array=$result->fetch_all(MYSQLI_ASSOC);
        echo json_encode($array);
    }

}

?>