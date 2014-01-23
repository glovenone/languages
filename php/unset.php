<?php
/*
echo memory_get_usage()."\n";
$a = str_repeat("A", 1000);
echo memory_get_usage()."\n";
$b=&$a;  //下面的内存大小不会变，unset只是解除$a的绑定
unset($a);
echo memory_get_usage()."\n";
unset($b);
echo memory_get_usage()."\n";
*/

$a = array('a'=>'a', 'b'=>'b');
unset($a['c']);
print_r($a);
?>
