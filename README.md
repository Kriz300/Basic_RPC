# Basic_RPC

_Este proyecto es un ejemplo basico del uso de RCP._

### Consideraciones de Ejecución 🔧

Si no se ejecuta correstamente revise que tenga instalado Python 3.8+ y la ultima versión de Redis disponible. A continuación se dejan algunos comandos que podrian ser de utilidad.

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

## Construido con 🛠️

**Python**


## Autores ✒️

* **Christian Muñoz I.** [Kriz](https://github.com/Kriz300)
* **Camilo Rubilar** [Niyet](https://github.com/niyetsin)
* **Raimundo Perez** [Raimundo Perez](https://github.com/raimundoperez8)

## Licencia 📄

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para detalles.