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
$var = session_start();
//echo dirname(__FILE__) .DIRECTORY_SEPARATOR. 'tmp';
//echo $_SESSION['blubb'];
/*
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
*/
?>

<!DOCTYPE html>
<html lang="de">
  
	<head>
	    <meta charset="UTF-8">
	     
	    <meta name="viewport" 
	          content="width=device-width, initial-scale=1.0">
	      
	    <!-- CSS file -->
	    <link rel="stylesheet" href="../Html/css/style.css">  
	    <!-- jQuery Ajax CDN -->
	    <script src="../Html/js/jquery-3.6.1.min.js"></script>
	
		<script type="text/javascript">
			var user_id = <?php echo ( isset( $_SESSION['id'] ) && $_SESSION['id'] != '') ? $_SESSION['id'] : '0';?>
		</script>
		
		<script type="text/javascript" src="../Html/js/cookies.js"></script>
		<script type="text/javascript" src="../Html/js/events.js"></script>
	      
	</head>
	<body>
		<h1>Habit tracker</h1>
		<div id="user_infos" width="100%">
			<h3 id="username">
				User: <?php echo ( isset( $_SESSION['username'] ) && $_SESSION['username'] != '') ? $_SESSION['username'] : 'No username';?>
			</h3>
		</div>
		<label for="function_select">Which action?</label>
		<select id="function_select"  width="100%">
			<option value=""></option>
			<option value="autoTests">Test project automatically</option>
			<option value="createHabit">Create habit</option>
			<option value="createActivity">Create activity</option>
			<option value="showAll">Show all</option>
			<option value="analyseDataFull">Analyse your data (full)</option>
			<option value="analyseDataSummary">Analyse your data (summary)</option>
		</select>
		<div  width="100%" style="padding-top:20px;">
			<div id="inputarea" width="49%" style="float:left">
				<label for="wait">Wait for testing the entertainment while loading process?</label>
				<input type="number" id="wait" name="wait">
				<br><br>
				<div id="inputareaCreated">
				
				</div>
			</div>
			<div id="outputarea" width="49%" style="float:left">
				<div class="direct-contact-container">
					<article>
						<div class="stand">
							<div class="monitor">
								<pre id="fieldForAnswer"></pre>
							</div>
						</div>
					<article>
				</div>
				<!--
				<div class="left">
				</div>
				<div class="right">
					<div id="habits">
					</div>
					
					<div id="habits_lasttime">
					</div>			
				</div>
				-->
			</div>		
		</div>

		<div class="modal" style="display:none; position:fixed; top:0;left:0; width:100%; height:100%;z-index:1000;background: rgba( 255, 255, 255, .8 )url('../Html/assets/gif/loading2.gif') 50% 50% no-repeat; background-size: 100px;" >
		
		<marquee id="marquee" style="position: relative; top: 40%; font-size: 20px;">
<pre>Please wait... and wait and wait.. wait and wait and wait and wait and wait and wait and wait and wait and wait and wait and wait and wait and	...   Oh! Now!..		 wait longer! and wait and wait and wait and wait and wait..			Ha! Now, really!	---			No, just joking! ^^ Just wait a little longer. You know... Wait and wait and wait and wait and wait and wait...
</pre>
		</marquee>
		
		<!-- Place at bottom of page --></div>


		<script type="text/javascript">
		
		</script>
	</body>
</html>