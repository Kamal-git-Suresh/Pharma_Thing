<?php
    if($_SERVER["REQUEST_METHOD"] == "POST"){
        $username = $_POST["username"];
        $password = $_POST["Password"];
        echo "Hello $username";
    }
    else{
        echo "How is this even possible"
    }
?>