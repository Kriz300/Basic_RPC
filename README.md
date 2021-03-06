# Basic_RPC

_Este proyecto es un ejemplo basico del uso de RCP._

## Consideraciones de Ejecuci贸n 馃敡

### Ejecuci贸n

**Comandos:**
```
$ python server.py
```
En caso de tener m谩s de una versi贸n de python usar
```
$ python3 server.py
```

Si no se ejecuta correstamente revise que tenga instalado Python 3.8+ y la ultima versi贸n de Redis disponible. A continuaci贸n se dejan algunos comandos que podrian ser de utilidad.

* **Ubuntu/Debian**
```
$ sudo apt install -yqq build-essential
$ sudo apt update && sudo apt upgrade -y
```

* **Python**
```
$ python -m pip install --upgrade pip
$ python -m pip install grpcio
$ python -m pip install grpcio-tools
```

* **Redis**
```
$ sudo apt update
$ sudo apt install redis-server
$ sudo echo "supervised systemd" >> /etc/redis/redis.conf
$ sudo systemctl restart redis.service
$ sudo systemctl status redis
$ sudo apt update && sudo apt upgrade -y
```
### Configuraci贸n de Redis(Cache)

* Memoria maxima: 1mb.
* Politica: maxmemory-policy allkeys-lru. 
* Al reiniciar se elimina todo el cache.

## Construido con 馃洜锔?

**Python**


## Autores 鉁掞笍

* **Christian Mu帽oz I.** [Kriz](https://github.com/Kriz300)
* **Camilo Rubilar** [Niyet](https://github.com/niyetsin)
* **Raimundo Perez** [Raimundo Perez](https://github.com/raimundoperez8)

## Licencia 馃搫

Este proyecto est谩 bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para detalles.