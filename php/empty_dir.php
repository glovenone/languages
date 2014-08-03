<?php

function isEmptyDir($path) {
    $dh = opendir($path);
    while(($f = readdir($dh)) !== false) {
        if(!in_array($f, array('.', '..'))) {
            return true; 
        }
    }
    return false;
}

$res = isEmptyDir('.');
var_dump($res);

?>
