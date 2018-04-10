<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Settu inn upplýsingar</title>
</head>
<body>

<form action="/db/add" method="POST">
    <fieldset>
        <legend>Settu inn upplýsingar</legend>
        <label for="">Skráningarnúmer: </label>
        <input type="text" name="skr_nr" required>
        <br>
        <label for="">Tegund: </label>
        <input type="text" name="tegund" required>
        <br>
        <label for="">Verksmiðjunúmer: </label>
        <input type="text" name="vrk_nr" required>
        <br>
        <label for="">Skráningardagur: </label>
        <input type="text" name="skr_dags" placeholder="áááá-mm-dd" required>
        <br>
        <label for="">CO2: </label>
        <input type="number" name="co2" required>
        <br>
        <label for="">Þyngd: </label>
        <input type="number" name="tyngd" required>
        <br>
        <label for="">Skoðunardagur: </label>
        <input type="text" name="sko_dags" placeholder="áááá-mm-dd" required>
        <br>
        <label for="">Staða: </label>
        <input type="text" name="stada" required>
        <br><br>
        <input type="submit" value="Skrá">
    </fieldset>
</form>

<p><a href="/">Til baka</a></p>

</body>
</html>