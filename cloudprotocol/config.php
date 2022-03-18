<?php
/*
 *  Config file
 *
*/
define( 'DB_NAME', '' );
define( 'DB_USER', '' );
define( 'DB_PASSWORD', '' );
define( 'DB_HOST', 'localhost' );
define( 'DB_CHARSET', 'utf8' );
define( 'DB_COLLATE', '' );

$conn = mysqli_connect (DB_HOST,DB_USER,DB_PASSWORD,DB_NAME);
mysqli_set_charset($conn,"utf8mb4"); // set charset utf8

?>