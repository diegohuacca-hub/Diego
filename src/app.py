import os
import configparser

def cargar_configuracion():
    env = os.getenv("APP_ENV", "dev")

    config_name = {
        "test": "config_test.ini",
        "prod": "config_prod.ini"
    }.get(env, "config_dev.ini")

    config = configparser.ConfigParser()
    config.read(config_name, encoding="utf-8")

    return env, config

def main():
    env, config = cargar_configuracion()

    print("==============================")
    print(f"Aplicación : {config['app']['name']}")
    print(f"Entorno    : {env}")
    print(f"Mensaje    : {config['app']['message']}")
    print(f"Debug      : {config['app'].getboolean('debug')}")
    print("==============================")

if __name__ == "__main__":
    main()
