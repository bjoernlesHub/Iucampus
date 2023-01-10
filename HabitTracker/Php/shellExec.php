<?php

if(!empty($_POST)) {
	//echo json_encode($_POST);
	//echo $_POST["data"]["zeugs"];
	$parameters="";
	foreach($_POST["data"] as $key=>$value)
	{
	  $parameters=$parameters."$key=$value ";
	}
	//echo $parameters;
	
	$command = escapeshellcmd("python ..\Python\HabitTracker.py ".$parameters); // $var1 $var2 $var3
	$output = shell_exec($command);
	echo $output;
	
}
?>
