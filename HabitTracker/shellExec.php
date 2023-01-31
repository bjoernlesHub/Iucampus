<?php
if (!empty($_SERVER['HTTP_ORIGIN'])) {
  $http_origin = $_SERVER['HTTP_ORIGIN'];
  $allowed_domains = array(
    'https://bjoernle.ddns.net',
    'https://localhost',
    'https://192.168.1.20',
  );
    header("Access-Control-Allow-Origin: *"); 
    header("Access-Control-Allow-Methods: *"); 
	header('Access-Control-Allow-Credentials: true');
    header('Access-Control-Allow-Methods: POST');
    header('Access-Control-Max-Age: 3000');
    header('Access-Control-Allow-Headers: Origin, Content-Type, X-Auth-Token , Authorization');
		if (!function_exists('str_contains')) {
			function str_contains($haystack, string $needle): bool
			{
				return '' === $needle || false !== strpos($haystack, $needle);
			}
		}
}
if(!empty($_POST)) {
	//echo json_encode($_POST);
	$file= realpath('..'.DIRECTORY_SEPARATOR."Python".DIRECTORY_SEPARATOR."HabitTracker.py");
	//echo($file);
	
	if(file_exists($file)){
	$parameters="";
	
	foreach($_POST["data"] as $key=>$value)
	{
	  $parameters=$parameters."$key=$value ";
	}
	
	//echo $parameters;
	$rootDir = realpath(dirname(__FILE__));
	$blubb = dirname(__DIR__, 1);
	$dir = realpath($blubb.DIRECTORY_SEPARATOR."Python");
	//echo $dir;
	
		$forShell  ="python ".$file." ".$parameters;
		//echo $forShell;
		$command = escapeshellcmd($forShell); // $var1 $var2 $var3
		echo $command;
		$output = shell_exec($forShell);
		//echo "blubb";
		echo $output;
	}
}
?>
