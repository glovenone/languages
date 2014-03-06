<?php

function replaceUrl($src_string){
    $result = str_replace((https?|ftp|file):\/\/[-a-zA-Z0-9+&@#\/%?=~_|!:,.;]*)/g,"<a target=_blank href=\"$1\">$1</a>");
    return $result;
}

$str = 'http://www.hanguoyou.org';

print_r(replaceUrl($str));

?>
