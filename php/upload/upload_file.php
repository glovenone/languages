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

if ($_FILES["file"]["error"] > 0)
{
    echo "Error: " . $_FILES["file"]["error"] . "<br />";
}
else
{
    echo "Upload: " . $_FILES["file"]["name"] . "<br />";
    echo "Type: " . $_FILES["file"]["type"] . "<br />";
    echo "Size: " . ($_FILES["file"]["size"] / 1024) . " Kb<br />";
    echo "Stored in: " . $_FILES["file"]["tmp_name"];

    /*
    $nname = $_FILES["file"]["name"];//获取上传的文件名称
    $tname = $_FILES["file"]["tmp_name"];//获取上传文件的临时文件名 
    $res_move = move_uploaded_file($tname,$nname);//移动上传文件,在这之前其实文件已经上传成功!此处作一个命名处理而已!此处还是以原来的名称命名文件!
     */
    $dir = getcwd();//获取当前目录
    $nname = $_FILES["file"]["name"];//获取上传的文件名称
    $tname = $_FILES["file"]["tmp_name"];//获取上传文件的临时文件名 

    $res_move = move_uploaded_file($tname,$nname);//移动上传文件,在这之前其实文件已经上传成功!此处作一个命名处理而已!此处还是以原来的名称命名文件!
    //echo "winrar x $dir\\$nname $dir";

    print_r($dir);
    //unlink($nname);//此命令为删除文件,意思上传后删除原来上传的压缩文件,只留解压后的文件夹!
    echo '<br/>';
    var_dump($res_move);
    echo '<br/>';
    print_r($nname);
    echo '<br/>';
    unzipFile($nname,'.');
}
?>
