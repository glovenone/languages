<?php

exec('rm photo.*');

$imgData_test = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFoAAAAeCAYAAACsYQl4AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA9ZJREFUeNrsWl9P1EAQ35nuHYeSGOBEIiEm/nn0RQyo38L4ZOIXNPhBBOET+IRIhHiEF+Du+mfHmW0r5Wh7vbZ3YOwkl+7fudnfzs7O7iwQkWpo+oQNBLMhnVWxr+em9qfdzTXs7R6Zsv0XN1b12f6xf1dA3PCHY9tAlulIA7r79gkqCqRbopTsqiAjfEhZfpRoEqVBJYqD4JHS+kTF/w1cSmSzZL+ExP/DSbR5Y5IrDx1jXgQI30dElzYGAEzIEhQghukwzxJa2ZAzRsoMhbLbukTaMuO+wkNks7wUl/O3t/PTlAFaF9LArTUGmNrKH7ZZUC3gMrCORU7S9mOHIe00KYpBxgjwaMCgCMBXg8EH1elsJ+YCVQiCtiAbM0dkOuGXWlze4vx81NgxrveJ2nr771QTcwVgBjAkmXgAj399CpEbcl1AIgPFQIrM3I4ESRVEbBxJc4kAakj6Oc6QZfYB0AUHPZ44t7v52OV6t7cz2Yocq9G8zLUywUJv7/issbSR4r1eXVSOc85g+0U1GsfZ0gbkmyR4UBAsWHyqeh3drXVZzu0G5HQ6FbDJtGtw78RmFmf0XxLjs1xQq7Mbhd6DbtDMwdmXDbrYgW8MkFTYBo1uCPFmGpfX6ZdPg2fMdxKexgQdNBpjr6rsZhi6cBMOfBTgf4XKyMvu5zzb6To0upx2ZWlFWtuslTCuLo9v0dWVBu4kWm1kD7t+mLr9u47kAOIB5q2EoqskC7xJVlcRJUnX6KAuG10fVbWnaf2nZauLI83HUVJ3S6PHaXsVm357+wFpttN3S6Onoe3S71Y3XVCevXiahUan2cGyGprXL6uurJdTxwSBQh8QzMxMR3Kwk9jNvH7T5jnKq8yEMcj961fGOW2zbu8O3j1FZfyl3t7J7+YMmE4PXi4+h1b74NnuD7+iRoNp4MxBB2CAWNVG2+iC8hs4c4DWzkUckamg0QI0ug2ceTbacQF1NY3u7RzyTIFrowkN3aCljZVlsCGtw+peh41Uo3PegD0C8quVZQXO+em3X4VNa6EoeBiyobYNBCSDs2XPU/3+e7x/78vEPCJRzeDyI3TmPyeM3FW1vUaXwKtE0u01r8iOJjCt8CRHEviV9e5IGuSWUokckHTbLu1hJPSTh+joCy4dgMa+DdQiukmQa31uEIW2lLpqX9oHJ897CK3WSRkeNsLueWuq1Tq6AhputonkjMUNxylPFyQCbuxThvCJQxi9T8BsIHyfYCPmljd/xbtgmyzmVJ3uXn9yUPu7jrqo+2Yde18PS7uOVR/gTOOupjTQDdVLzdu7GdEfAQYA0GVEhPs9qdMAAAAASUVORK5CYII=';


$img_base64 = $_POST['img_base64'];
$imgData = isset($img_base64)?$img_base64:$imgData_test;

preg_match('/^(data:\s*image\/(\w+);base64,)/', $imgData, $result);
    print_r($result);
$photo_suffix = $result[2];

$photo = base64_decode(str_replace('data:image/'.$photo_suffix.';base64,', '', $imgData));

file_put_contents('photo.'.$photo_suffix, $photo);

?>

<html>
<body>
<img src="photo.<?php echo $photo_suffix?>" />
</body>
</html>
