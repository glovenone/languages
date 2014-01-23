<?php

function cutstr_cn2($string, $strlen = 20,$code='UTF-8', $etc = '..', $keep_first_style = false) {
    $strlen = $strlen*2;
    $string = trim($string);
    if ( strlen($string) <= $strlen )    {
        return $string;
    }
    $str = strip_tags($string);
    $j = 0;
    for($i=0;$i<$strlen;$i++) {
      if(ord(substr($str,$i,1))>0xa0) $j++; 
    }
    if($j%2!=0) $strlen++; 
    $rstr=substr($str,0,$strlen);
    if (strlen($str)>$strlen  ) {$rstr .= $etc;} 

    if ( $keep_first_style == true && ereg('^<(.*)>$',$string) )    {
        if ( strlen($str) <= $strlen )    {
            return $string;
        }
        $start_pos = strpos($string,substr($str,0,4));
        $end_pos = strpos($string,substr($str,-4));
        $end_pos = $end_pos+4;
        $rstr = substr($string,0,$start_pos) . $rstr . substr($string,$end_pos,strlen($string));
    }
    return $rstr; 
}

$str1 = "我爱北京天安门，天安门上彩旗飘~";
$res1 = cutstr_cn2($str1, 15, 'UTF-8', '');
print_r($res1);

?>
