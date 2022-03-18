<?php
/*
 *  Check exists repo
 *
*/
require 'config.php';

if (isset($_POST['name'])&&!empty($_POST['name']))
{
    $name = $_POST['name'];
    $sql = "SELECT * FROM packages WHERE name='$name'";
    $result = mysqli_query($conn,$sql);
    $array = mysqli_fetch_array($result);

    if (isset($array)){
        echo 'E8';
    }
    else {
        echo 'S';
    }
}
else
{
    echo 'E0';
}

?>