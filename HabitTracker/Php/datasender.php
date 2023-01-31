<?php
if (!function_exists('str_contains')) {
	function str_contains($haystack, string $needle): bool
	{
		return '' === $needle || false !== strpos($haystack, $needle);
	}
}
if(str_contains(PHP_OS, "Linux")){
	ini_set('session.save_path','/tmp');
	ini_set('session.gc_probability', 1);
}
session_start();
//$_SESSION["SameSite"] = "None";
//echo("Session: ".session_status());
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
    header('Access-Control-Max-Age: 30000');
    header('Access-Control-Allow-Headers: Origin, Content-Type, X-Auth-Token , Authorization');
}

if(!empty($_POST)) {
	//echo json_encode($_POST);
	//echo $_POST["data"]["zeugs"];
	$parameters="";
	foreach($_POST["data"] as $key=>$value)
	{
	  $parameters=$parameters."$key=$value ";
	}
	//echo $parameters;
	//__DIR__ . DIRECTORY_SEPARATOR .
	$file= realpath('..'.DIRECTORY_SEPARATOR."Python".DIRECTORY_SEPARATOR."HabitTracker.py");
	//echo($file);
	
	if(file_exists($file)){

		$forShell  ="python ".$file." ".$parameters;
		//echo $forShell;

		$command = escapeshellcmd($forShell); // $var1 $var2 $var3
		echo $command;
		$output = shell_exec($command);

			
			//$array=explode("-", getBetween($output, "(",")"));

			//echo $webpath;
			echo $output;
			//header('Location: '.$path);
			//exit();
			//echo $output;
	}
	else{
		echo "--".$file."-- not exist";
	}
	
}
function getBetween($string, $start = "", $end = ""){
    if (strpos($string, $start)) { // required if $start not exist in $string
        $startCharCount = strpos($string, $start) + strlen($start);
        $firstSubStr = substr($string, $startCharCount, strlen($string));
        $endCharCount = strpos($firstSubStr, $end);
        if ($endCharCount == 0) {
            $endCharCount = strlen($firstSubStr);
        }
        return substr($firstSubStr, 0, $endCharCount);
    } else {
        return '';
    }
}
?>