<?php

require 'config.php';

$username = $_POST['username'];
$password = hash('ripemd160',$_POST['password']);
$fullname = $_POST['fullname'];
$me = $_POST['me'];

$sql = "SELECT password FROM users WHERE username='$me'";
$result = mysqli_query ($conn,$sql);
$array = mysqli_fetch_array ($result);

if (isset($array))
{
    if ($array[0]==$password)
    {
        $sql = "SELECT fullname FROM users WHERE username='$username'";
        $result = mysqli_query ($conn,$sql);
        $array = mysqli_fetch_array ($result);
        
        if (isset($array))
        {
            if ($username==$me)
            {
                echo '0';
            }
            else
            {
                $sql = "INSERT INTO contacts (id,me,username,fullname) VALUES (NULL,'$me','$username','$fullname');";
            
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