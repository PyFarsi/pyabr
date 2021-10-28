<?php
// ** MySQL settings ** //
/** The name of the database for WordPress */
define( 'DB_NAME', '');

/** MySQL database username */
define( 'DB_USER', '');

/** MySQL database password */
define( 'DB_PASSWORD', '');

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

$conn = mysqli_connect (DB_HOST,DB_USER,DB_PASSWORD,DB_NAME);

?>