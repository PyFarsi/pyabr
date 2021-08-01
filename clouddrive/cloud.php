<?php
require 'config.php';

header('Content-Type: text/txt');

$address = $_POST['address']; # projop.ir
$data = $_POST['data']; # index.py

if (isset($address))
{
	if (is_dir (server.'/'.$address))
	{
		if (is_file(server.'/'.$address.'/'.$data))
		{
			readfile (server.'/'.$address.'/'.$data);
		}
		else
		{
			exit ('e: data not found');
		}
	}
	else
	{
		exit ('e: address not found');
	}
}
else
{
	exit ('e: no address');
}

?>
