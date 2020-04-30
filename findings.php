<!doctype html>

<html lang="en">
<head>
    <meta charset="utf-8">
    
    <title>Predicting COVID-19</title>
    <meta name="description" content="Tracking COVID-19">
    <meta name="author" content="465-EC-Team">
    
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">    
    <link rel="stylesheet" href="css/styles.css?v=1.0">

    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    
    <link rel="shortcut icon" type="image/png" href="images/favicon-16x16.png">

</head>

<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="index.html">Predicting COVID-19</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Click Me!
                </a>
                <!-- Here's the magic. Add the .animate and .slide-in classes to your .dropdown-menu and you're all set! -->
                <div class="dropdown-menu dropdown-menu-right animate slideIn" aria-labelledby="navbarDropdown">
                    <a class="dropdown-item" href="about.html">About Us</a>
                    <a class="dropdown-item" href="research.html">Research</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="findings.php">Findings</a>
                </div>
                </li>
            </ul>
            </div>
        </div>
        </nav>
<form method="post">
  <div class="form-group">
    <label for="formGroupExampleInput">Enter a rate in decimal form (ie. 50% = 0.5)</label>
    <input type="text" name = "rate" class="form-control" id="formGroupExampleInput" placeholder="Rate">
  </div>
</form>

<?php 
    $rate = $_POST['rate'];
    $command = 'python3 seir.py ' . $rate;
    $python = `$command`;
    echo $python
?>
<img src='my_plot.png'>
</div>
</body>
</html>