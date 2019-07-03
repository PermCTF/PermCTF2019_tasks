<!doctype html>
<html lang="en">
  <head>
      <style>
          body{
              background-image: url(used/not_a_fl4g.jpg);
          }
      </style>
    <meta charset="utf-8">
    <title>Task</title>
  </head>
  <body>
    <div class="col-md-4 col-md-offset-4" style="padding-top: 10%">

          <div class="checkbox">
          <?php
          
			if (isset($_GET['needed'])){
			
				if ($_GET['needed'] ==='gimmeflag' ){

					echo '<style>#mask {background-color:rgba(0,0,0,.6);height:100%;position:fixed;width:100%;top:0;left:0;color: azure;text-align: center;} img{display: block;margin-left: auto;margin-right: auto;}</style><div id="mask"><h2 class="form-signin-heading">Your flag is: PermCTF{}</h2></br><img src="./used/.kotik.jpg" style="width:50%;"></br></div>';
				}
			}
		  ?>
          </div>
      </div>
  </body>
</html>
</body>
</html>