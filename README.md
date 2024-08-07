# DE Challenge - Globant

Este respositorio contiene el código y demás material que han sido usados para llevar a cabo la construcción del PoC que es la propuesta de solución al primer challenge planteado; PoC que luego es utilizado para resolver el segundo challenge.

El PoC se construyó en base a una arquitectura de microservicios. Para su implementación se creó 3 imágenes Docker las cuales componen la aplicación. Para su despliegue se ha hecho uso de docker-compose la cual facilita la gestión y despliegue de aplicaciones multi-contenedor como lo es la presente.

### Arquitectura

La aplicación está conformado por 3 imágenes Docker, a saber:

1. **frontend**, una simple interfaz web construida sobre _Flask_, que permite realizar la carga en lote de información hacia el motor de base de datos.

2. **api**, aquí se implementa toda la lógica de la API Rest. Este contenedor es el encargado de manejar los requerimientos del cliente y dirigirlos hacia el backend. Para su implementación se utilizó el framework _Flask_.

3. **db (backend)**, aquí está contenido el motor de base datos (PostgreSQL) y es el único elemento que forma parte backend. También se encuentran los SQL scripts que se requieren para ensamblar la base de datos.

## Instalación

Para correr la aplicación en un entorno local se requiere que [Docker](https://docs.docker.com/get-docker/) (entorno de ejecución de contenedores) haya sido instalado de forma previa. La herramienta docker-compose hace parte de la instalación básica de Docker y por lo tanto no se requiere instalarla por separado.

## Uso

Clone o descargue este repositorio, ubicarse en el interior del directorio que contiene al proyecto, abra una shell y ejecute el siguiente comando:

```bash
docker compose up
```

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
