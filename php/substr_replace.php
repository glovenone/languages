<?php

$mobile['phoneNum'] = '18610435976';
$mobile['countryCode'] = '+86';
$str_repeat = str_repeat('*', strlen($mobile['phoneNum']) - 4);
$number     = substr_replace($mobile['phoneNum'], $str_repeat, 2, -2);
$number     = $mobile['countryCode'] . $number;
print_r($number);

?>
