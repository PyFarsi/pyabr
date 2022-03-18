<?php
/*
 *  Create a Cloud Account
 *
*/
require 'config.php';

/*
E0   - Empty fields
E1   - Connection failed
E2   - User Exists
E3   - Cannot move file
E4   - User not found
E5   - Wrong password
E6   - File not found
E7   - Access denid
E8   - Package exists
E9   - Mail not found
*/

if (isset($_POST['username'])&&!empty($_POST['username'])&&isset($_POST['password'])&&!empty($_POST['password']))
{
    $username = $_POST['username'];
    $password = hash("sha3-512",$_POST['password']);
    // Check user exists
    $sql = "SELECT * FROM users WHERE username='$username'";
    $result = mysqli_query($conn,$sql);
    $array  = mysqli_fetch_array ($result);

    if (isset($array))
    {
        echo 'E2';
    }
    else
    {
        // Create Account
        $sql = "INSERT INTO users (id,username,password) VALUES (NULL,'$username','$password')";
        if (mysqli_query($conn,$sql))
        {
            echo 'S';
        }
        else
        {
            echo 'E1';
        }
    }
}
else
{
    echo "E0";
}

?>