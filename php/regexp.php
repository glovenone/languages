<?php

$str = '早安……@Nuni-SunFun @天才天才樱木花道 @tamtam余金香 @刘伟盛不带V @李江君 @AB_阿不 我在这里:http://t.cn/zjtlZZv';

$replace = '我在这里:http';

$res1 = str_replace($replace, 'tobedeleted_iamhere', $str);

print_r($res1);
echo '<br/>';

$reg = "/tobedeleted_iamhere:[a-zA-Z.\/0-9]*/";

$res2 = preg_replace($reg, '', $res1);

print_r($res2);



?>
