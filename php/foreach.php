<?php

$arr = array('a'=>'aa', 'b'=>'bb', 'c'=>'cc');
foreach($arr as $key=>$value) {
    echo $key."\t";
    echo $value;
    echo "\n";
    echo $arr[$key];
}

?>
