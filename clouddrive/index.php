<?php
require 'config.php';

header('Content-Type: text/txt');

if (isset ($_POST['password'])&&!empty($_POST['password']))
{
    $password = $_POST['password'];

    if ($password==password)
    {
        exit ("s: connected");
    }
    else
    {
        exit ("e: wrong password");
    }
}
else
{
    exit ("e: empty password");
}
