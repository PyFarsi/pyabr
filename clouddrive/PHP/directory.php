<?php
require 'config.php';

header('Content-Type: text/txt');

if (isset ($_POST['password'])&&!empty($_POST['password']))
{
    $password = $_POST['password'];

    if ($password==password)
    {
        if (isset ($_POST['dirname'])&&!empty($_POST['dirname']))
        {
        	$dirname = rootpath.'/'.$_POST['dirname'];


        	if (is_file($dirname))
        	{
        		exit ("e: is a file");
        	}
        	else if (!is_dir($dirname))
        	{
        	    mkdir($dirname, 0777);
        	}
        }
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
?>