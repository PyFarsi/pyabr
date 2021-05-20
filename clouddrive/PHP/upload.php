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


        	if (is_dir ($filename))
        	{
        		exit ("e: is a directory.");
        	}
        	else
        	{
			    if (isset ($_POST['data']))
			    {
				    $data = $_POST['data'];
				    $file = fopen($filename,"w");
				    fwrite($file,$data);
				    fclose($file);
			    }
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
