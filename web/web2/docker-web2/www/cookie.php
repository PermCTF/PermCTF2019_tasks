<?php

if(!isset($_COOKIE['mode'])) {
    setcookie('mode', 'guest');
}
if (SetCookie("mode","guest"))  echo "<script>alert('Hello,guest!')</script>>";
if (SetCookie("mode","admin"))  echo "<script>alert('Hello,admin!')</script>>";
?>
