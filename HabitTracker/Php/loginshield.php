<?php
session_start();
//echo phpversion();
if(!empty($_POST)) {
	//echo json_encode($_POST);
	//echo $_POST["data"]["zeugs"];
	$parameters="";
	foreach($_POST["data"] as $key=>$value)
	{
	  $parameters=$parameters."$key=$value ";
	}
	//echo $parameters;
	$file= realpath(__DIR__ . DIRECTORY_SEPARATOR . '..'."\Python\HabitTracker.py");
	if(file_exists($file)){
		$forShell  ="python ".$file." ".$parameters;
		//echo $forShell;
		$command = escapeshellcmd($forShell); // $var1 $var2 $var3
		$output = shell_exec($forShell);
		if(str_contains($output, "User logged in")){
			
			$array=explode("-", getBetween($output, "(",")"));
			
			//session_start();

			// Set session variables
			$_SESSION["username"] = $array[0];
			$_SESSION["id"] = $array[1];
			
			
			$path= realpath('..' . DIRECTORY_SEPARATOR . 'Html' . DIRECTORY_SEPARATOR . 'start.php');
			$webpath=str_replace("C:\\xampp\\htdocs", "http://localhost", $path);
			$webpath=str_replace("\\", "/", $webpath);
			//echo $webpath;
			echo 'Location: '. $webpath;
			//echo $output;
		}
		else{
			echo $output;
		}
	}
	else{
		echo $file." not exist";
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