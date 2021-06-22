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
        }
        else
        {
            $dirname = rootpath;
        }

        if (is_dir($dirname))
        {
            // https://stackoverflow.com/questions/24783862/list-all-the-files-and-folders-in-a-directory-with-php-recursive-function/24784144

            function getDirContents($dir) {
                $files = scandir($dir);
                foreach($files as $key => $value){

                    $path = realpath($dir.DIRECTORY_SEPARATOR.$value);
                    if(!is_dir($path)) {
                        yield $path;
                    }
                    else if ($value != "." && $value != "..") {
                        yield from getDirContents($path);
                        yield $path.'/';
                    }
                }
            }

            foreach(getDirContents($dirname) as $value) {
                echo $value."\n";
            }
        }
        else
        {
            exit ("e: directory not found");
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
