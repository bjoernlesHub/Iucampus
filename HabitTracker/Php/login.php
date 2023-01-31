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
//session_start();
//$_SESSION["blubb"] = "blubber";
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
    header('Access-Control-Max-Age: 3000');
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
		$sudo = "";
		if(str_contains(PHP_OS, "Linux")){
			$sudo = "sudo ";
		}
		$forShell  =$sudo."python ".$file." ".$parameters;
		//echo $forShell;
		$command = escapeshellcmd($forShell); // $var1 $var2 $var3
		$output = shell_exec($forShell);
		if(str_contains($output, "User logged in")){
			
			$array=explode("-", getBetween($output, "(",")"));
			
			session_start();
			$_SESSION["username"] = $array[0];
			$_SESSION["id"] = $array[1];
			//echo "<h1>".$array[0]."</h1>";
			$path= "start.php";

			//echo $webpath;
			//echo $output;
			if(str_contains(PHP_OS, "Linux")){
				header('Location: '.$path);
			}
			else{
				echo $output;
			}
			
			//exit();
			//echo $output;
		}
		else{
			//echo $output;
		}
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
	      
	</head>
	  
	<body>
<div class="form-structor">
	<div class="login slide-up">
		<div class="center">
			<h2 class="form-title" id="login">Log in</h2>
			<div class="form-holder">
				<input type="text" class="input" id="login-user_name" placeholder="Your username" />
				<input type="password" class="input" id="login-user_password" placeholder="Your password" />
			</div>
			<button class="submit-btn" id="login-submit-btn">Log in</button>
		</div>
	</div>
	<div class="signup">
		<h2 class="form-title" id="signup"><span>or </span>Sign up</h2>
		<div class="form-holder">
				<input type="text" class="input" id="signup-user_name" placeholder="Your username" />
				<input type="password" class="input" id="signup-user_password" placeholder="Your password" />
		</div>
		<button class="submit-btn" id="signup-submit-btn">Sign up</button>
	</div>
</div>
		
		<div id="fieldForAnswer"></div>
	<script type="text/javascript">
		$(document).ready(() => {
		
			console.clear();

			//loginBtn.addEventListener('click', (e) => {
			$("#login-submit-btn").click(() => {
				//console.log("jnkjnkj klnkjkj jkkj");
				sendToPhp("LoginUser");
			});

			$("#signup-submit-btn").click(() => {
				sendToPhp("SignupUser");
			});	
			
		});
		
		function sendToPhp(loginOrSignup){
			const audio = new Audio("../Html/assets/mp3/elevator.mp3");
			audio.play();
			//$("#btn").click(() => {
			//$('#marquee').marquee();
			var myArray = {}
			myArray["action"]=loginOrSignup;
			//myArray.websiteSelected=$("#website-select").val();
			var whichClass="";
			
			if(loginOrSignup=="LoginUser"){
				whichClass=$(".login :input");
			}
			else if(loginOrSignup=="SignupUser"){
				whichClass=$(".signup :input");
			}
			console.log("whichclass selected");
			whichClass.each(function(){
				var input = $(this);
				var name=input.attr('id').replace("login-","").replace("signup-","");
				var value="";
				
				if(input.attr("type")=="checkbox")
				{
					value=input.is(':checked');				
				}
				else{
					value=input.val();
				}
				
				if(name!="submit-btn"){
					myArray[name]=value.toString().replace(" ","³");
				}
				
			});
			
			$.each(myArray, function( index, value ) {
				console.log(index+"="+value)
				//alert( value );
			})
			
			

		    // Fetching key's input field data
		    const key = $("#key").val();
		  
		    // Fetching values input field data
		    const value = $("#value").val();
		  
		    // Initializing array of objects to 
		    // store key-value pairs
		    
		    let data = {};
		  
		    // assigning key-value pair to data object
		    data = myArray;
		  
		    // jQuery Ajax Post Request
			//var dirSeparator = "<?php if(DIRECTORY_SEPARATOR == "/"){echo DIRECTORY_SEPARATOR;}else{echo DIRECTORY_SEPARATOR; echo DIRECTORY_SEPARATOR;} ?>";
			//var path = "..<?php echo DIRECTORY_SEPARATOR; echo DIRECTORY_SEPARATOR; ?>Php<?php echo DIRECTORY_SEPARATOR; echo DIRECTORY_SEPARATOR; ?>loginShield.php";
			//var path = ".."+dirSeparator+"Php"+dirSeparator+"loginShield.php";
			var path = "login.php";
			console.log(path)
			//alert(path);
		    $.post(
		      path,
		      {
		        data,
		      },
		      (response) => {
		        // response from PHP back-end
		        //console.log(`Response from sever side is: ${response}`);
				
				audio.pause();
				audio.currentTime = 0;
				
				document.write(response);
				//console.log(response);
				//if(response.includes("Location: ")){
					//alert(response);
				
				$("#fieldForAnswer").html(response); //.replace("\n","<br>")
				if(response.includes("User logged in")){
					var mySubString = response.substring(
						response.indexOf("(") + 1, 
						response.lastIndexOf(")")
					);
					myArray=mySubString.split("-");
					console.log(myArray[0]+" -> "+myArray[1]);
					
					$.post( 'start.php', { 'username' : myArray[0], 'id' : myArray[1] }, function() {
						window.location.href = 'start.php';
					});
					
					//window.location.href = "start.html";
				}
				
				
				var $target = $("#fieldForAnswer");
				 $('html, body').stop().animate({
				  'scrollTop': $target.offset().top
				 }, 900, 'swing', function () {
					
				  //window.location.hash = "#fieldForAnswer";
				 });
				//location.href = "#fieldForAnswer";
		      }
		    );
			
		  //});
		//});
		
		}

	</script>
	</body>
</html>