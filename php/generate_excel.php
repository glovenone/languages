<?php
$url_pre_old = 'http://jingdian.travel.sina.com.cn/';
$url_pre_new = 'http://travel.sina.com.cn/';
$url_suffix_new = 'lvyou';
$con = mysql_connect("127.0.0.1", "root", "");
mysql_select_db("jingdiantravel");

$sql = "select * from jd_info limit 5";
mysql_query("set names utf8");
$query = mysql_query($sql);
$pattern = array("\r\n", "\r", "\n");
$count = 0;
$file_name = date("Y-m-d-h-i-s", time());
$fp = fopen('data/'.$file_name.'_data.xls', 'w');
while($res = mysql_fetch_assoc($query)) {
    foreach($res as $key=>$value) {
        if($count==0) {
            fwrite($fp, $key."\t");
        } else {
            $value_without_wrap = str_replace($pattern, "<br />", $value);
            fwrite($fp, $value_without_wrap."\t");
        }
    }
    fwrite($fp, "\n");
    $count ++;

    $result[] = $res;
}
fclose($fp);
/*
 * $xlsname = date("Y-m-d", time());
 * $xls = new Excel_XML();
 * $xls->addArray($result);
 * $str=$xls->generateXML($xlsname);    //获取资源
 *
 * $fp=fopen('data/'.$xlsname.'data.xls','w'); //按照生成日期创建一个名字
 * fwrite($fp,$str);
 * fclose($fp);
 * */



?>

