<?php

//simple_html_dom/simple_html_dom.php
//https://github.com/samacs/simple_html_dom
include('simple_html_dom/simple_html_dom.php');
$filename = '481870.html';

$html = file_get_html($filename);

$detail_arr_ori = $html->find('.details_block');
$detail_arr     = $detail_arr_ori[0];
$detail_arr     = explode("\t", $detail_arr->plaintext);
$detail_str     = trim(implode('', $detail_arr));
$detail_arr     = explode("\n", $detail_str);
foreach ($detail_arr as $key => &$value) {
    $value = trim($value);
}
$game['title']        = $detail_arr[0];
$game['type']         = $detail_arr[1];
$game['developer']    = $detail_arr[2];
$game['publisher']    = $detail_arr[3];
$game['publish_time'] = $detail_arr[4];

$desc_short_ori     = $html->find('.game_description_snippet');
$desc_short         = trim($desc_short_ori[0]->plaintext);
$game['desc_short'] = $desc_short;

$desc_long_ori     = $html->find('.game_area_description');
$desc_long         = trim($desc_long_ori[0]->plaintext);
$game['desc_long'] = trim(str_replace('关于这款游戏', '', $desc_long));

$pics_ori = $html->find('.highlight_strip_screenshot');
$pic_str  = '';
foreach ($pics_ori as $key => $value) {
    $pic     = $value->children[0]->attr['src'];
    $pic     = str_replace('.116x65', '', $pic);
    $pic_str = $pic_str . ',' . $pic;
}
$game['pic'] = trim($pic_str, ',');

/*
$video_ori = $html->find('.highlight_movie');
print_r($video_ori[0]->children[0]);
 */

$area_details = $html->find('.game_area_details_specs');
foreach($area_details as $key=>$value) {
    $game['special'][$value->plaintext] = 1;
}

/*
//todo 
$language = $html->find('table[class=game_language_options]');
print_R($language->plaintext);
 */

$system_tabs = $html->find('.sysreq_tabs')[0]->children;
foreach($system_tabs as $key=>$value) {
    $system_key = trim($value->plaintext);
    if($system_key) {
        $system_keys[] = $system_key;
    }
}

$system_data = $html->find('.game_area_sys_req_full');
$sys_config = [];
foreach($system_keys as $syskey_key=>$syskey_value) {
    $system_tmp = $system_data[$syskey_key]->children[0]->plaintext;
    $system_tmp = explode("\n",$system_tmp);
    foreach($system_tmp as $value) {
        $system_value = trim($value);
        if($system_value) {
            $system_config[$syskey_value][] = $system_value;
        }
    }
}
$game['system_config'] = $system_config;



print_r($game);
$html->clear();

?>
