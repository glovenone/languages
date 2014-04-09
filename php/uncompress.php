<?php

error_reporting(E_ALL);
set_time_limit(0);

function unzipFile($file, $dest) {
    $fileinfo = pathinfo($file);
    $ext = strtolower($fileinfo['extension']);
    if($ext == 'zip') {
        $zip = new ZipArchive();
        if($zip->open($file) !== TRUE) {
            die('Could not open archive');
        }
        $zip->extractTo($dest);
        $zip->close();
        echo 'Archive extracted to directory';
    } elseif($ext == 'rar') {
        //使用PHP预定义的Com组件加载Shell,加载wscript.shell用来执行dos命令的组件
        $obj = new COM('wscript.shell');
        $obj->run("winrar x $path $dest",1, true);
        echo 'Archive extracted to directory';
    } else {
        die('need a zip or rar file');
    }
}

unzipFile('/Users/apple/Desktop/meme.rar', '.');
?>
