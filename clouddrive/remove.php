<?php
require 'config.php';

header('Content-Type: text/txt');

if (isset ($_POST['password'])&&!empty($_POST['password']))
{
    $password = $_POST['password'];

    if ($password==password)
    {
        if (isset ($_POST['filename'])&&!empty($_POST['filename']))
        {
        	$filename = rootpath.'/'.$_POST['filename'];


        	if (is_file($filename))
        	{
        		unlink ($filename);
        	}
        	else
        	{
            		exit ("e: file not found");
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
