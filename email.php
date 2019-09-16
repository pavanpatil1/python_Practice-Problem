<?php

if(isset($_POST['email']) == true && empty($_POST['email']) == false){
    $email = $_POST['email'];
    if(filter_var($email,FILTER_VALIDATE_EMAIL)==true){
        echo "<h1>";
        echo "Valid Email Address";
        echo "</h1>";
    }
    else{
        echo "<h1>";
        echo "Email Address is not Valid";
        echo "</h1>";
    }
}

?>

<html>
<head>
<title>Email-validation</title>
</head>
<style>
.form{
    margin-left:500px;
    margin-top:50px;
    width:350px;
    box-shadow:0px 10px 10px grey;
}
.form form{
    padding:30px;
}
input[type=text],input[type=password]{
    margin:10px;
    padding:7px;
    width:100%;
    font-family: 'Courier New', Courier, monospace;
}
input[type=submit]{
    margin:10px;
    padding:10px;
    background:black;
    color:#fff;
    font-size:15px;
    width:100px;
    border:black;
    border-radius:10px;
    cursor:pointer;
    font-family: 'Courier New', Courier, monospace;
    outline:none;
}
input[type=submit]:hover{
   background:white;
   color:black;
   border:2px solid black;
}
span{
    font-family: 'Courier New', Courier, monospace;
    font-size:30px;
}
p{
    margin-top:240px;
    font-size:23px;
    font-family: 'Courier New', Courier, monospace;

}
</style>
<body>
<br><br>
 <center><span>Login</span></center>
    <div class="form">
    <form action="email.php" method="post">
    <input type="text" name="email" placeholder="Enter your Email">
    <br><br>
    <input type="text" name="name" placeholder="Enter your Password">
    <br><br>
    <input type="submit" value="Login">
    </form>
    </div>

<div class="footer">
<center><p>&copy; All Rights reserved 2019-20</p></center>
</div>

</body>
</html>