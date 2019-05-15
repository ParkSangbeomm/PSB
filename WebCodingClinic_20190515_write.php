/*
<html>
<head>
</head>
<body>
  <h3> 새 상품 추가 </h3>
  <form method="post" action="write_ok.php" enctype="multipart/form-data">
    상품명 : <input type='text' name='title'><br>
    후기개수 : <input type='text' name='review'><br>
    이미지 소스 : <input type='text' name='imgUrl'><br>
    가격 : <input type='text' name='price'><br>
    색깔 : <input type='text' name='color'><br>
    사이즈 : <input type='text' name='size'><br>
    <input type='submit' value='저장'>
    <input type='reset' value='취소'>
  </form>
</body>
</html>
*/

/*
//write_ok.php
<?php
  $title = $_POST['title'];
  $imgUrl = $_POST['imgUrl'];
  $review = $_POST['review'];
  $price = $_POST['price'];
  $color = $_POST['color'];
  $size = $_POST['size'];

  $conn = mysqli_connect("localhost", "shb598999", "park990501", "shb598999");
  $sql = "INSERT INTO tomonari (title, imgUrl, review, price, color, size) VALUES ('$title', '$imgUrl', '$review', '$price', '$color', '$size');";
  mysqli_query( $conn, $sql);
  mysqli_close($conn);
  mysqli
?>
<script>
  alert("Add!!");
  location.href='index.php';
</script>
*/
