<?php

$arr = ['a'=>1, 'b'=>2];
foreach($arr as &$val) {
    $val = 10;
}

print_r($arr);
?>
