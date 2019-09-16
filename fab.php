

<?php 

function fab($n){
    $num1 = 0;
    $num2 = 1;
    $counter = 0;
    $series = '';
    while($counter < $n){
        $series.=$num1;
        if($counter < ($n-1)){

            $series.=',';
        }
        $num3 = $num1 + $num2;
        $num1 = $num2;
        $num2 = $num3;
        $counter++;
    }
    echo "<h1>";
    echo $series;
    echo "</h1>";

}

$num = 10;
$fab = fab($num);

?>

<style>
h1{
    font-family: 'Courier New', Courier, monospace;

}
</style>