		$(document).ready(() => {

			

			$body = $("body");

			$(document).on({
				ajaxStart: function() { 
				$body.addClass("loading");
				
					  $(function(){
						$('.marquee').marquee({
					  
						//If you wish to always animate using jQuery
						allowCss3Support: true,
					  
						//works when allowCss3Support is set to true - for full list see http://www.w3.org/TR/2013/WD-css3-transitions-20131119/#transition-timing-function
						css3easing: 'linear',
					  
						//requires jQuery easing plugin. Default is 'linear'
						easing: 'linear',
					  
						//pause time before the next animation turn in milliseconds
						delayBeforeStart: 0,
						//'left', 'right', 'up' or 'down'
						direction: 'left',
					  
						//true or false - should the marquee be duplicated to show an effect of continues flow
						duplicated: false,
					  
						//speed in milliseconds of the marquee in milliseconds
						duration: 10000,
					  
						//gap in pixels between the tickers
						gap: 20,
					  
						//on cycle pause the marquee
						pauseOnCycle: false,
					  
						//on hover pause the marquee - using jQuery plugin https://github.com/tobia/Pause
						pauseOnHover: false,
					  
						//the marquee is visible initially positioned next to the border towards it will be moving
						startVisible: false
						
						});
					  });

				},
				 ajaxStop: function() { $body.removeClass("loading"); }    
			});

			$(document).on("change", '#website-select', function() {
				if ($(this).val() == 'e-kleinanzeigen'){
				  $('#inputarea').load('Html/html_templates/e-kleinanzeigen.html').fadeIn("fast");
				  $('#btn').show();
				  $('#btnSaveCookie').show();
				  
				  //alert("loaded");
				} else {
					$('#inputarea').html("");
					$('#btn').hide();
					$('#btnSaveCookie').hide();
				}
				$(".invi").hide();
			});
			/*
			$(document).on("change", '#use_sql_sqlite',  function() {
				if($(this).val!="sqlite"){
					//$('input:disabled').prop( "disabled", false );
					$('.usesql').show();
				}
				else{
					$('.usesql').hide();
				}
			});
			*/
            $(document).on("change", '#send_mail',  function() {
				if($(this).is(':checked')){
					//$('input:disabled').prop( "disabled", false );
					$('.sendmail').show();
				}
				else{
					$('.sendmail').hide();
				}
			});			

		  // Adding 'click' event listener to button
		  $("#btn").click(() => {
			//$('#marquee').marquee();
			var myArray = {}
			myArray.websiteSelected=$("#website-select").val();
			$("#inputarea :input").each(function(){
				var input = $(this);
				var name=input.attr('id');
				var value="";
				if(input.attr("type")=="checkbox")
				{
					value=input.is(':checked');				
				}
				else if(input.attr("id")=="words"){
					if(input.val()!=""){
						value='"'+input.val()+'"';
					}
					console.log("Words: "+value);
				}
				else{
					value=input.val();
				}
				myArray[name]=value.toString().replace(" ","³");
			});
			/*
			$.each(myArray, function( index, value ) {
			  alert( value );
			})
			*/

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
			const audio = new Audio("Html/assets/mp3/elevator.mp3");
			audio.play();
		    $.post(
		      "Php/shellExec.php",
		      {
		        data,
		      },
		      (response) => {
		        // response from PHP back-end
		        //alert(`Response from sever side is: ${response}`);
				
				audio.pause();
				audio.currentTime = 0;
				
				//console.log(response);
				$("#fieldForAnswer").html(response); /*.replace("\n","<br>")*/
				
				
				var $target = $("#fieldForAnswer");
				 $('html, body').stop().animate({
				  'scrollTop': $target.offset().top
				 }, 900, 'swing', function () {
					
				  //window.location.hash = "#fieldForAnswer";
				 });
				//location.href = "#fieldForAnswer";
		      }
		    );
			
		  });
		});