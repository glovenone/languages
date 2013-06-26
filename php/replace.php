<?php

$str1 = '<b>【旺季】</b>';

$res1 = str_replace(array('<b>', '</b>'), '', $str1);
print_r($res1);
echo "<br/>"."\n";
$str2 = '&nbsp;&nbsp;大家觉得咋样？？？？可爱的话帮我顶哦';
echo str_replace('&nbsp;', '', $str2); 


?>
