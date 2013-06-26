<?php

function myStrRev($str) {
    $len = strlen($str);
    $res = '';
    for($i=1; $i<=$len; $i++) {
        $res .= $str[$len-$i];
    }
    return $res;
}


$str1 = 'hello, world!';
print_r(myStrRev($str1));
echo "\n";


?>
