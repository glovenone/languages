<?php

/*
   *功能：php多种方式完美实现下载远程图片保存到本地
   *参数：文件url,保存文件名称，使用的下载方式
   *当保存文件名称为空时则使用远程文件原来的名称
   */
function getImage($url,$filename='',$type=0){
    if($url==''){return false;}
    if($filename==''){
        $ext=strrchr($url,'.');
        if($ext!='.gif' && $ext!='.jpg'){return false;}
        $filename=time().$ext;
    }
    //文件保存路径 
    if($type){
        $ch=curl_init();
        $timeout=5;
        curl_setopt($ch,CURLOPT_URL,$url);
        curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
        curl_setopt($ch,CURLOPT_CONNECTTIMEOUT,$timeout);
        $img=curl_exec($ch);
        curl_close($ch);
    }else{
        ob_start(); 
        readfile($url);
        $img=ob_get_contents(); 
        ob_end_clean(); 
    }                                                                                
        $size=strlen($img);
        //文件大小 
        $fp2=@fopen($filename,'a');
        fwrite($fp2,$img);
        fclose($fp2);
        return $filename;
}

?>
