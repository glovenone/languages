<?php

date_default_timezone_set('America/Los_Angeles');
/*
echo strtotime("now"), "\n";
echo strtotime("10 September 2000"), "\n";
echo strtotime("+1 day"), "\n";
echo strtotime("+1 week"), "\n";
echo strtotime("+1 week 2 days 4 hours 2 seconds"), "\n";
echo strtotime("next Thursday"), "\n##";
$timestamp = strtotime("last Monday");
echo date('l dS of F Y h:i:s A', $timestamp);

echo "\n";
$str = 'Not Good';

if (($timestamp = strtotime($str)) === false) {
    echo "The string ($str) is bogus";
} else {
    echo "$str == " . date('l dS of F Y h:i:s A', $timestamp);
}

echo date('Y-m-d H:i:s', time()-60*60*24);
*/

$str="test"; 
$test = 'yes';
$yes = 'yes2';
$result = $$$str;

$t0 = strtotime("-1 month");
$t0 = strtotime("20140305");
$t = strtotime("20140306");
$t_d = $t - $t0;
echo $t_d;
echo "\n";
echo "\n";
//echo date("Y-m-d H:i:s", $t);
echo "\n";

?>
