<?php
session_start();
?>
<!DOCTYPE html>
<html lang="de">
  
	<head>
	    <meta charset="UTF-8">
	     
	    <meta name="viewport" 
	          content="width=device-width, initial-scale=1.0">
	      
	    <!-- CSS file -->
	    <link rel="stylesheet" href="css/style.css">  
	    <!-- jQuery Ajax CDN -->
	    <script src="js/jquery-3.6.1.min.js"></script>
	
		<script type="text/javascript">
			var user_id = <?php echo ( isset( $_SESSION['id'] ) && $_SESSION['id'] != '') ? $_SESSION['id'] : '0';?>
		</script>
		
		<script type="text/javascript" src="js/cookies.js"></script>
		<script type="text/javascript" src="js/events.js"></script>
	      
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
			<option value="autoTests">Test project automatic</option>
			<option value="createHabit">Create habit</option>
			<option value="createActivity">Create activity</option>
			<option value="showAll">Show all</option>
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

		<div class="modal" style="display:none; position:fixed; top:0;left:0; width:100%; height:100%;z-index:1000;background: rgba( 255, 255, 255, .8 )url('assets/gif/loading2.gif') 50% 50% no-repeat; background-size: 100px;" >
		
		<marquee id="marquee" style="position: relative; top: 40%; font-size: 20px;">
<pre>Please wait... and wait and wait.. wait and wait and wait and wait and wait and wait and wait and wait and wait and wait and wait and wait and	...   Oh! Now!..		 wait longer! and wait and wait and wait and wait and wait..			Ha! Now, really!	---			No, just joking! ^^ Just wait a little longer. You know... Wait and wait and wait and wait and wait and wait...
</pre>
		</marquee>
		
		<!-- Place at bottom of page --></div>


		<script type="text/javascript">
		
		</script>
	</body>
</html>