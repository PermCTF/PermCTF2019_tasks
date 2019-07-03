<?php
  if (isset($_POST['n33d3d'])){
    if ($_POST['n33d3d'] ==='f14g' ){
      echo 'Y0ur f14g 15: PermCTF{U_n33d_1t_U_g07_1t}\n';
    } else {
      echo 'W311, I gu355 y0u n33d s0m3thing m0re 31337\n';
    }
  }
?>
<!doctype html>
<html lang="en">
  <head>
      <style>
          body{
          <?php
            date_default_timezone_set("Asia/Yekaterinburg");
            $hour = date('H', time());
            if($hour > 6 && $hour <= 22) {
              echo 'background-image: url(background/a2620cbc10f5198dd03e3f5a1569eb5dcf9a6a87.jpg);';
            } else {
              echo 'background-image: url(background/1be2a44cb53dde903be8466c08dee9067da8ede3.jpg);';
            }
          ?>    
          }
      </style>
    <meta charset="utf-8">
    <title>Task</title>
  </head>
  <body>
    <div class="col-md-4 col-md-offset-4" style="padding-top: 10%">
          <div class="checkbox"> 
          <!-- Should BE implemented -->
          <!--Send us what you need as n33d3d value via POST -->
          </div>
      </div>
  </body>
</html>
</body>
</html>
