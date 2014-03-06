<?php

function _sortForHotPic($a, $b) {
$a['total'] = $a['wantto_num'] + $a['wantto_num_m'] + $a['been_num'] + $a['been_num_m'];
$b['total'] = $b['wantto_num'] + $b['wantto_num_m'] + $b['been_num'] + $b['been_num_m'];
if($a['total'] == $b['total']) {
return 0;
}
return ($a['total'] > $b['total']) ? -1 : 1;
}

?>
