html= """
<html>
    <head>
        <title></title>
        
        
    </head>
    <body>
 
    <h1>Meine Astrophotos</h1>
    <img src="img/Messier51.jpg">
    Messier 51
    <img src="img/Messier_45.jpg">
    Messier 45
    <img src="img/Ngc_2024.jpg">
    Ngc2024
</body>
</html>
"""
print(html)

#Write HTML String to file.html
with open("index.html","w") as file:
        file.write(html)