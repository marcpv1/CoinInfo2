<?php

function curl($url) {
        $ch = curl_init();  // Initialising cURL
        curl_setopt($ch, CURLOPT_URL, $url);    // Setting cURL's URL option with the $url variable passed into the function
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE); // Setting cURL's option to return the webpage data
        $data = curl_exec($ch); // Executing the cURL request and assigning the returned data to the $data variable
        curl_close($ch);    // Closing cURL
        return $data;   // Returning the data from the function
    }

//$valor = curl("https://api.coingate.com/v2/rates/merchant/BTC/EUR");

//$valorf = (float) $valor;
//$quant = 0.02442289;
//$total = $valorf * $quant;
?>
<!DOCTYPE html>
<html lang="ca">
<head>
  <title>Bitcoin</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
  <link rel="icon" href="https://assets.bitstamp.net/widgets/s/widgets/widgets/img/btc.5e2d1332.svg">
</head>
<body style="background-color:\"#000000\";" onload="inici();">
<button onclick="mode()">MODE</button>
<div class="container">
 <div class="row">
 <div class="col-sm-3"></div>
 <div class="col-sm-6">
<?php
$user=$_GET["user"];
$cookie_name = "mode";
$cookie_value = "DIA";
setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/");


echo "<h1><b><br>COINBASE<br></b></h1>";
echo "<p><font size=\"+3\">";
$command = 'python /home/pi/coinbase/coin1.py';
$command = "sudo runuser -l pi -c 'python /home/pi/coinbase/coin1.py " . $user . "'";
$output = shell_exec($command);
echo $output;
echo "</font></p>";

if ($user=="") print("ERROR: Cal un usuari");
?>
 </div>
 <div class="col-sm-3"></div>
 </div>
</div>
<script>
function inici() {
var mode=getCookie("MODE");

 if (mode!=null) {

  if (mode=="NIT") mode_nit();

  } 
}

function mode_nit() {
	var list1= document.getElementsByTagName('p');
	var list2= document.getElementsByTagName('font');
	var list3= document.getElementsByTagName('h1');
	
	document.body.style.backgroundColor = "#000000";

    for (var i = 0; i < list1.length; i++) {
         list1[i].style.color = "white";
    }
	for (var i = 0; i < list2.length; i++) {
         list2[i].style.color = "white";
    }
	for (var i = 0; i < list3.length; i++) {
         list3[i].style.color = "white";
    }
}
function mode_dia() {
	var list1= document.getElementsByTagName('p');
	var list2= document.getElementsByTagName('font');
	var list3= document.getElementsByTagName('h1');
	
    document.body.style.backgroundColor = "";

    for (var i = 0; i < list1.length; i++) {
         list1[i].style.color = "black";
    }
	for (var i = 0; i < list2.length; i++) {
         list2[i].style.color = "black";
    }
	for (var i = 0; i < list3.length; i++) {
         list3[i].style.color = "black";
    }
}


function mode() {
	
  if ((document.body.style.backgroundColor == "#FFFFFF" )||(document.body.style.backgroundColor == ""))
  {    
	mode_nit();
	setCookie("MODE","NIT",99);	
  } else 
  {
	mode_dia();
	setCookie("MODE","DIA",99);	
  }  
}

function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}

function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

function eraseCookie(name) {   
    document.cookie = name +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}
</script>
</body>
</html>
