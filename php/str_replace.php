<?php

$tags_rm = array('<b>', '</b>', '<strong>', '</strong>', '<pre.+?/>', '</pre>');
$str = '<pre id="best-answer-content" class="reply-text mb10">上船地点在北海北海客运港，侨港镇去银滩的路上往右边看就可以看到了。蛮近的了，在北海之窗去就10分钟车程。</pre>';

//$res = str_replace($tags_rm, '', strip_tags($str));

//echo $res;

$tags_rm1 = array(' ');
$str1 = '                    长滩岛（Boracay）属于菲律宾的Aklan地区，距离马尼拉1小时的飞行距离，形状如同一个哑铃，是个以白色沙滩闻名的热带岛屿。白色海滩长约四公里，被誉为“世界上沙子最细的沙滩”，海滩边尚有许多度假村、饭店、度假套房、餐厅和其他的观光设施。这里的水上活动设施齐全，有众多餐馆酒吧，娱乐服务完善。岛的北部和南部那些海拔不过百米的小山，蜿蜒小路穿过雨林，连接起座座村庄，是轻松而不失趣味的徒步路线。



        

        长滩岛的沙滩曾被LonelyPlanet、《英国BMW旅游杂志》等旅游书评选为全世界最美丽的沙滩之一。
        ';

$res1 = str_replace($tags_rm1, '', strip_tags($str1));

?>
