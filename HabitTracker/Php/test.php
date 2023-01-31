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
$_SESSION["SameSite"] = "None";
$_SESSION["username"] = "blubb";
echo $_SESSION["username"];
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
    header('Access-Control-Max-Age: 3000');
    header('Access-Control-Allow-Headers: Origin, Content-Type, X-Auth-Token , Authorization');
}
		if (!function_exists('str_contains')) {
			function str_contains($haystack, string $needle): bool
			{
				return '' === $needle || false !== strpos($haystack, $needle);
			}
		}

	//echo json_encode($_POST);
	//echo $_POST["data"]["zeugs"];
	$parameters="action=LoginUser user_name=admin user_password=pwd";

	//echo $parameters;
	//__DIR__ . DIRECTORY_SEPARATOR .
	$file= realpath('..'.DIRECTORY_SEPARATOR."Python".DIRECTORY_SEPARATOR."HabitTracker.py");
	//echo($file);
	
	if(file_exists($file)){
		$sudo = "";
		//if(str_contains(PHP_OS, "Linux")){
		//	$sudo = "sudo ";
		//}
		$forShell  =$sudo."python ".$file." ".$parameters;
		//echo $forShell;
		$command = escapeshellcmd($forShell); // $var1 $var2 $var3
		echo $command;
		$output = shell_exec($forShell);
		if(str_contains($output, "User logged in")){
			
			$array=explode("-", getBetween($output, "(",")"));
			
			//session_start();

			// Set session variables
			$_SESSION["username"] = $array[0];
			$_SESSION["id"] = $array[1];
			
			$path= "start.php";

			//echo $webpath;
			echo $output;
			//header('Location: '.$path);
			exit();
			//echo $output;
		}
		else{
			echo $output;
		}
	}
	else{
		echo "--".$file."-- not exist";
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