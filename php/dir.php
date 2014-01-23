<?php

function getDir($path){ //$path 为要遍历的目录路径
    if(is_dir($path)){ //判断是否为目录
        $dir_resource = opendir($path);
        if(is_resource($dir_resource)){ //判断是否返回目录句柄
            while($read_result = readdir($dir_resource)){
                if($read_result != "." && $read_result != ".."){ //排除目录中存在的 "." 和 ".."
                    $newPath = $path."/".$read_result; //将遍历出的结果拼接在上一级目录名后生成新的路径
                    if(is_dir($newPath)){ //判断新路径是否为目录 true 则递归遍历 否则直接输出
                        getDir($newPath);
                    }else {
                        echo $read_result."<br/>";
                    }
                }
            }
        }
    }
}


getDir('/home/glove/www/something/php');


function getPath($path) {
    if(is_dir($path) {
        $dir_resource = opendir($path);
        if(is_resource($dir_resource)) { 
            while($read_result = readdir($dir_rescource)) {
                if($read_result != "." && $read_result != "..") {
                    $newPath = $path."/".$resad_result;
                }
            }
        }
    }
}

?>
