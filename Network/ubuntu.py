import fire
import yaml


class Load:

    def netplan(self, config_path: str = '/etc/netplan/00-installer-config.yaml'):
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)


class Save:
    config: dict

    def __init__(self, config: dict) -> None:
        self.config = config

    def netplan(self, config_path: str = '/etc/netplan/00-installer-config.yaml'):
        with open(config_path, 'w') as file:
            yaml.dump(self.config, file)


class ConfigureNetwork:
    interface: str | None

    def __init__(self, interface: str) -> None:
        self.interface = interface

    def static_ip(self):
        config = Load().netplan()


    def dns_client(self):
        pass


