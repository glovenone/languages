<html>
<head></head>
<body>
    <form method="post" action="">
        <input type="text" name="url_input"></input>Input url here.
        <br />
        <textarea type="text" name="content_input" rows="5" cols="30"></textarea> Or input contents here.
        <br />
        <input type="submit" name="submit" value="submit"></input>
    </form>
</body>


<?php
if(isset($_POST['content_input']) && $_POST['content_input']) {
    $contents = $_POST['content_input'];
} else if(isset($_POST['url_input']) && $_POST['url_input']) {
    $url_input = $_POST['url_input'];
    $contents = file_get_contents($url_input);
} else {
    echo 'Please input the url or text!';
    exit();
}
    //print_r($contents);
    $reg = '/(?:(href)=\"http:\/\/)(.*)(?:\")/U';
    $reg1 = '/<a(.*?)href=(.*?)</a>/i';
    preg_match_all($reg, $contents, $urls);

    $urls_uniqued = array_unique($urls[0]);
    $urls_sorted = sort($urls_uniqued);
    $urls_output = $urls_uniqued;
    echo 'Are these what you want?^_^'.'<br />'.'<br />';
    echo '<br />';
    echo 'There are total <font color=red>'.count($urls_output).'</font> urls';
    echo '<br />';
    echo '<br />';
    foreach($urls_output as $key => $value) {
        echo $value;
        echo '<br />';
    }

?>
</html>
