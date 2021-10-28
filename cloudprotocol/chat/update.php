<?php
require 'config.php';

$username = $_POST['username'];
$password = hash('ripemd160',$_POST['password']);

$fullname = $_POST['fullname'];
$phone = $_POST['phone'];
$bloodtype = $_POST['bloodtype'];
$email = $_POST['email'];
$company = $_POST['company'];
$birthday = $_POST['birthday'];
$gender = $_POST['gender'];
$country = $_POST['country'];
$city = $_POST['city'];
$website = $_POST['website'];
$profile = $_POST['profile'];

$sql = "SELECT password FROM users WHERE username='$username'";
$result = mysqli_query($conn,$sql);
$array = mysqli_fetch_array ($result);

if (isset($array)){
    if ($array[0]==$password){
        $sql = "UPDATE users SET fullname='$fullname',phone='$phone',bloodtype='$bloodtype',email='$email',company='$company',birthday='$birthday',gender='$gender',country='$country',city='$city',website='$website',profile='$profile' WHERE username='$username'";
        
        if ( mysqli_query($conn,$sql)){
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
}
else
{
    echo '0';
}

?>