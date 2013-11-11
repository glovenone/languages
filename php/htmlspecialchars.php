<?php



$str='<a href="test.html">测试页面</a>'; 
echo htmlentities($str); 

echo "\n";

$str='<a href="test.html">测试页面</a>'; 
echo htmlspecialchars($str); 
echo "\n";


?>
