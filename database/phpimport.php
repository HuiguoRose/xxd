<?php

$db_name		  = $argv[1];
$db_sql_file      = $argv[2];

require_once dirname(__FILE__)."/config.php";

$cfg = $db_config[$db_name];
echo shell_exec("php $db_sql_file {$cfg['host']} {$cfg['user']} '{$cfg['pass']}' {$cfg['name']} {$cfg['port']}");

?>
