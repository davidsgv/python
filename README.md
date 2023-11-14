# comandos
## actualizar requisitos
pipreqs ./

## correr aplicación
python app.py

# Docker
## contenedor app tienda
aqui se contruye la imagen con el docker file se hace por consola ubicado en la carpeta del proyecto
- docker build -t tienda .
- docker run --name app --rm -itdp 8080:80 tienda

## contenedor mysql
aqui se contruye la imagen de mysql con la bd tiene que ejecutarse en la carpeta bd
- docker build -t mysql_bd . 
- docker run --name tienda_bd --rm -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123 mysql_bd

## revisar ip de mysql
- docker network inspect bridge (buscar contenedor de mysql)