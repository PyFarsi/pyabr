<?php

require 'config.php';

$sender = $_POST['sender'];
$password = hash('ripemd160',$_POST['password']);
$giver = $_POST['giver'];
$data = $_POST['data'];

$sql = "SELECT password,fullname FROM users WHERE username='$sender'";
$result = mysqli_query ($conn,$sql);
$array = mysqli_fetch_array ($result);

if (isset($array))
{
    if ($array[0]==$password)
    {
        $fullname = $array[1];
        $sql = "SELECT * FROM users WHERE username='$giver'";
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
                $sql = "SELECT * FROM contacts WHERE username='$giver'";
                $result = mysqli_query ($conn,$sql);
                $array = mysqli_fetch_array ($result);
                
                if (!isset ($array))
                {
                    $sql = "INSERT INTO contacts (id,me,username,fullname) VALUES (NULL,'$giver','$sender','$fullname');";
                    
                    mysqli_query ($conn,$sql);
                }
                
                $sql = "INSERT INTO chats (id,sender,giver,data) VALUES (NULL,'$sender','$giver','$data');";
                if (mysqli_query ($conn,$sql))
                {
                    echo '1';
                }
                else
                {
                    echo '0';
                }
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