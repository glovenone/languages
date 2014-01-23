<?php

$str1 = '<a href="#" target="_blank">三地方</a> <a href="#" target="_blank">立刻就</a>';

$res1 = strip_tags($str1);

$str2 = '<font color="#dd3939">
    法国不仅是一个浪漫的旅游胜地，她也是一个美食的天堂，长时间的文化生活方式造就了法国的特色美食，这里的美食多采用当地的原材料精心制成，尼斯的海鲜大餐与沙拉，第戎的美味芥末，巴黎的鹅肝与法师面包，以及被誉为美食之都的里昂。除了各地佳肴不断刺激你的味蕾，戛纳、普罗旺斯和第戎的美丽景色，也会让你沿途的旅行更加精彩。</font>';

$res2 = strip_tags($str2);

var_dump($res1);
echo '<br />';

print_r($res2);


?>
