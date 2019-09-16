<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Color Change per Hour</title>
</head>
<style>
.for{
    margin-left:500px;
    margin-top:100px;
}
input[type=text]{
    margin:20px;
    padding:10px;
    border-radius:20px;
    outline:none;

}
input[type=submit]{
    margin:20px;
    padding:9px;
    background:black;
    color:#fff;
    border:black;
    cursor:pointer;
    border-radius:10px;
    font-size:15px; 

}
</style>
<?php
$color = array('#481E80','#0F1F3F','#9D0E10','#0E9D2A ','#0E9D8C','#0E3E9D','black','red','blue','grey');
$rand = $color[array_rand($color)];
?>

<body style="background: <?php  echo $rand; ?>">
    <?php
    $date = date("D  M  Y");
    echo "<h1 style='color:white;'>";
    echo $date;
    echo  "</h1>";
    ?>
<div class="for">
<form action="" method="post">
<input type="text" name="color"><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" name="submit">
</form>
</div>
  </body>

<?php
if(isset($_POST['submit'])){
    $color = $_POST['color'];
    if($color == "1"){
        echo "<body style='background:$rand'>";
        echo "</body>";
    }
    if($color == "2"){
        echo "<body style='background:$rand'>";
        echo "</body>";
    }
    if($color == "3"){
        echo "<body style='background:$rand'>";
        echo "</body>";
    }
    if($color == "4"){
        echo "<body style='background:$rand'>";
        echo "</body>";
    }
    if($color == "5"){
        echo "<body style='background:$rand'>";
        echo "</body>";
    }
    if($color == "6"){
        echo "<body style='background:$rand'>";
        echo "</body>";
    }
    if($color == "7"){
        echo "<body style='background:$rand'>";
        echo "</body>";
    }
    if($color == "8"){
        echo "<body style='background:$rand'>";
        echo "</body>";
    }
    if($color == "9"){
        echo "<body style='background:$rand'>";
        echo "</body>";
    }
    if($color == "10"){
        echo "<body style='background:$rand'>";
        echo "</body>";
    }
    if($color == "11"){
        echo "<body style='background:$rand'>";
        echo "</body>";
    }
    if($color == "12"){
        echo "<body style='background:$rand'>";
        echo "</body>";
    }
}

?>

</body>
</html>