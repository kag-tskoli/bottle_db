<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Skráðu nýjar upplýsingar</title>
</head>
<body>

<form action="/db/update" method="POST">
    <fieldset>
        <legend>Breyta upplýsingum</legend>
        <label for="">Skráningarnúmer: </label>
        <input type="text" name="skr_nr" required value="{{bill[0]}}">
        <br>
        <label for="">Tegund: </label>
        <input type="text" name="tegund" required value="{{bill[1]}}">
        <br>
        <label for="">Verksmiðjunúmer: </label>
        <input type="text" name="vrk_nr" required value="{{bill[2]}}">
        <br>
        <label for="">Skráningardagur: </label>
        <input type="text" name="skr_dags" placeholder="áááá-mm-dd" required value="{{bill[3]}}">
        <br>
        <label for="">CO2: </label>
        <input type="number" name="co2" required value="{{bill[4]}}">
        <br>
        <label for="">Þyngd: </label>
        <input type="number" name="tyngd" required value="{{bill[5]}}">
        <br>
        <label for="">Skoðunardagur: </label>
        <input type="text" name="sko_dags" placeholder="áááá-mm-dd" required value="{{bill[6]}}">
        <br>
        <label for="">Staða: </label>
        <input type="text" name="stada" required value="{{bill[7]}}">
        <br><br>
        <input type="submit" value="Uppfæra">
    </fieldset>
</form>

<p><a href="/">Til baka</a></p>

</body>
</html>