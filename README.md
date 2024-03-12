# Entrega 5 - Prueba de concepto final

Repositorio con código de la implementación de la entrega 5, donde se incluye el uso de un Backend for Frontend BFF usando GraphQL como lenguaje de consulta.

## Descripción de actividades realizadas por cada miembro del equipo:

https://uniandes-my.sharepoint.com/:w:/g/personal/d_chala_uniandes_edu_co/EfFy2FoZkuJLpw1aIypSdgMBkWHQkq1dCzGeVlzRl20ssg?e=GPHxH

## Postman de ejecución de pruebas (documentación):

https://documenter.getpostman.com/view/33329544/2sA2xcbFWC

## Estructura del proyecto

Este repositorio sigue en general la misma estructura del repositorio de origen. Sin embargo, hay un par de adiciones importante mencionar:

- El directorio **src/bff_web/** incluye el código del BFF Web. Este servicio cuenta con la siguiente estructura:
    - **consumidores**: Código con la lógica para leer y procesar eventos del broker de eventos.
    - **despachadores**: Código con la lógica para publicar comandos al broker de eventos.
    - **main**: Archivo con la lógica de despliegue y configuración del servidor.
    - **api**: Módulo con la diferentes versiones del API, routers, esquemas, mutaciones y consultas.

- Nuestro proyecto de propiedades de los Alpes contiene los siguientes archivos:
    - **api**: Contiene el archivo contratos.py con las apis expuestas
    - **modulos/../aplicacion**: Este módulo considera los sub-módulos: `queries` y `comandos`. En dichos directorios pdrá ver como se desacopló las diferentes operaciones lectura y escritura.
    - **modulos/../aplicacion/handlers.py**: Estos son los handlers de aplicación que se encargan de oir y reaccionar a eventos.
    - **modulos/../dominio/eventos.py**: Este archivo contiene todos los eventos de dominio que son disparados cuando una actividad de dominio es ejecutada de forma correcta.
    - **modulos/../infraestructura/consumidores.py**: Este archivo cuenta con toda la lógica en términos de infrastructura para consumir los eventos y comandos que provienen del broker de eventos. Desarrollado de una forma funcional.
    - **modulos/../infraestructura/despachadores.py**: Este archivo cuenta con toda la lógica en terminos de infrastructura para publicar los eventos y comandos de integración en el broker de eventos. Desarrollado de manera OOP.
    - **modulos/../infraestructura/schema**: En este directorio encontramos la definición de los eventos y comandos de integración. Puede ver que se usa un formato popular en la comunidad de desarrollo de software open source, en donde los directorios/módulos nos dan un indicio de las versiones `/schema/v1/...`. De esta manera podemos estar tranquilos con versiones incrementales y menores, pero listos cuando tengamos que hacer un cambio grande.
    - **seedwork/aplicacion/comandos.py**: Definición general de los comandos, handlers e interface del despachador.
    - **seedwork/infraestructura/queries.py**: Definición general de los queries, handlers e interface del despachador.
    - **seedwork/infraestructura/uow.py**: La Unidad de Trabajo (UoW) mantiene una lista de objetos afectados por una transacción de negocio y coordina los cambios de escritura. Este objeto nos va ser de gran importancia, pues cuando comenzamos a usar eventos de dominio e interactuar con otros módulos, debemos ser capaces de garantizar consistencia entre los diferentes objetos y partes de nuestro sistema.

### Ejecutar Aplicación
#ATENCION

Ejecución de los servicios backend como aplicaciones flask:

flask --app src/aeroalpes/api --debug run -p 5001
flask --app src/companias/api --debug run -p 5002
flask --app src/inquilinos/api --debug run -p 5003
flask --app src/propiedades/api --debug run -p 5004
flask --app src/procesador/api --debug run -p 5005

Desde el directorio principal desde 3 consolas diferentes ejecute los 3 siguientes comandos en este orden
docker-compose up -d db
docker-compose up -d db_companias
docker-compose up -d db-inquilinos
docker-compose up -d db-propiedades
docker-compose --profile pulsar up

docker-compose up aeroalpes
docker-compose up companias
docker-compose up inquilinos
docker-compose up propiedades
docker-compose up bff


sudo find . -name "__pycache__" -exec sudo rm -r {} +

pulsar puede estar fallando por los archivos en la carpeta data,
borrar la carpeta y volver a crear con los siguientes comandos permite que se ejecute normalmente
(extraido del .gitpod)

sudo rm -r data
sudo mkdir -p data/bookkeeper && 
      sudo mkdir -p data/zookeeper && 
      sudo chmod -R 777 ./data

COMANDOS PULSAR (abrir una consola del contenedor broker)

bin/pulsar-admin topics list public/default
bin/pulsar-admin topics subscriptions persistent://public/default/<topico>
bin/pulsar-admin topics subscriptions persistent://public/default/eventos-propiedad
bin/pulsar-admin topics stats persistent://public/default/<topico>
bin/pulsar-admin topics stats persistent://public/default/eventos-propiedad


```bash
flask --app src/aeroalpes/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/aeroalpes/api --debug run
```

### Ejecutar pruebas

```bash
coverage run -m pytest
```

### Ver reporte de covertura
```bash
coverage report
```

### Crear imagen Docker

Desde el directorio principal ejecute el siguiente comando.

```bash
docker build . -f aeroalpes.Dockerfile -t aeroalpes/flask
```

### Ejecutar contenedora (sin compose)

Desde el directorio principal ejecute el siguiente comando.

```bash
docker run -p 5000:5000 aeroalpes/flask
```

## Sidecar/Adaptador
### Instalar librerías

En el mundo real es probable que ambos proyectos estén en repositorios separados, pero por motivos pedagógicos y de simpleza, 
estamos dejando ambos proyectos en un mismo repositorio. Sin embargo, usted puede encontrar un archivo `sidecar-requirements.txt`, 
el cual puede usar para instalar las dependencias de Python para el servidor y cliente gRPC.

```bash
pip install -r sidecar-requirements.txt
```

### Ejecutar Servidor

Desde el directorio principal ejecute el siguiente comando.

```bash
python src/sidecar/main.py 
```

### Ejecutar Cliente

Desde el directorio principal ejecute el siguiente comando.

```bash
python src/sidecar/cliente.py 
```

### Compilación gRPC

Desde el directorio `src/sidecar` ejecute el siguiente comando.

```bash
python -m grpc_tools.protoc -Iprotos --python_out=./pb2py --pyi_out=./pb2py --grpc_python_out=./pb2py protos/vuelos.proto
```

### Crear imagen Docker

Desde el directorio principal ejecute el siguiente comando.

```bash
docker build . -f adaptador.Dockerfile -t aeroalpes/adaptador
```

### Ejecutar contenedora (sin compose)

Desde el directorio principal ejecute el siguiente comando.

```bash
docker run -p 50051:50051 aeroalpes/adaptador
```

## Microservicio Notificaciones
### Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.

```bash
python src/notificaciones/main.py
```

### Crear imagen Docker

Desde el directorio principal ejecute el siguiente comando.

```bash
docker build . -f notificacion.Dockerfile -t aeroalpes/notificacion
```

### Ejecutar contenedora (sin compose)

Desde el directorio principal ejecute el siguiente comando.

```bash
docker run aeroalpes/notificacion
```

## BFF: Web

Desde el directorio `src` ejecute el siguiente comando

```bash
uvicorn bff_web.main:app --host localhost --port 8003
```

## UI Websocket Server
### Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.

```bash
python src/ui/main.py
```

### Crear imagen Docker

Desde el directorio principal ejecute el siguiente comando.

```bash
docker build . -f ui.Dockerfile -t aeroalpes/ui
```

### Ejecutar contenedora (sin compose)

Desde el directorio principal ejecute el siguiente comando.

```bash
docker run aeroalpes/ui
```

## Docker-compose

Para desplegar toda la arquitectura en un solo comando, usamos `docker-compose`. Para ello, desde el directorio principal, ejecute el siguiente comando:

```bash
docker-compose up
```

Si desea detener el ambiente ejecute:

```bash
docker-compose stop
```

En caso de querer desplegar dicha topología en el background puede usar el parametro `-d`.

```bash
docker-compose up -d
```

### Comandos útiles para ejecución en cloud - máquina virtual

sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q)

sudo docker build . -f aeroalpes.Dockerfile -t contratos/flask &&
sudo docker build . -f companias.Dockerfile -t companias/flask &&
sudo docker build . -f inquilinos.Dockerfile -t inquilinos/flask &&
sudo docker build . -f propiedades.Dockerfile -t propiedades/flask &&
sudo docker build . -f bff.Dockerfile -t aeroalpes/bff 

sudo rm -r data
sudo mkdir -p data/bookkeeper && 
      sudo mkdir -p data/zookeeper && 
      sudo chmod -R 777 ./data

sudo docker compose up -d db &&
sudo docker compose up -d db-inquilinos &&
sudo docker compose up -d db_companias &&
sudo docker compose up -d db-propiedades &&
sudo docker compose --profile pulsar up

sudo docker compose up aeroalpes
sudo docker compose up companias
sudo docker compose up inquilinos
sudo docker compose up propiedades
sudo docker compose up bff


GitPod

docker stop $(sudo docker ps -a -q)
docker rm $(sudo docker ps -a -q)

docker build . -f aeroalpes.Dockerfile -t contratos/flask &&
docker build . -f companias.Dockerfile -t companias/flask &&
docker build . -f inquilinos.Dockerfile -t inquilinos/flask &&
docker build . -f propiedades.Dockerfile -t propiedades/flask &&
docker build . -f bff.Dockerfile -t aeroalpes/bff 

sudo rm -r data
sudo mkdir -p data/bookkeeper && 
      sudo mkdir -p data/zookeeper && 
      sudo chmod -R 777 ./data

sudo docker compose up -d db &&
sudo docker compose up -d db-inquilinos &&
sudo docker compose up -d db_companias &&
sudo docker compose up -d db-propiedades &&
sudo docker compose --profile pulsar up

sudo docker compose up aeroalpes
sudo docker compose up companias
sudo docker compose up inquilinos
sudo docker compose up propiedades
sudo docker compose up bff

