<?php

$a['a'] = 'aaa';
$a['b'] = 'bbb';
$b['a'] = 'baaa';

$res1 = implode('&', $a);
$res2 = implode('&', $b);
print_r($res1);
echo "\n";
print_r($res2);
echo "\n";

?>
