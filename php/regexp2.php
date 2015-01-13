<?php

$whiteList = array('immomo.com');
$callback = urlencode('http://www.immomo.baidu.com/');

$url_data = parse_url(urldecode($callback));
$host = $url_data['host'];
$match = 0;
foreach($whiteList as $white_host) {
    $reg = "/".$white_host."$/";
    if(preg_match($reg, $host) == 1) {
        $match = 1;
    }
}
print_r($match);
?>
