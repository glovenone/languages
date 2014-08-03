<?php

function quickSort($arr) {
    $len = count($arr);
    if($len <= 1) {
        return $arr;
    }
    $key = $arr[0];
    $left_arr = array();
    $right_arr = array();

    for($i = 1; $i<$len; $i++) {
        if($arr[$i] <= $key) {
            $left_arr[] = $arr[$i];
        } else {
            $right_arr[] = $arr[$i];
        }
    }

        $left_arr = quickSort($left_arr);
        $right_arr = quickSort($right_arr);
        return array_merge($left_arr, array($key),$right_arr);
}

$arr = array(49,38,65,97,76,13,27);
print_r(quickSort($arr));

?>
