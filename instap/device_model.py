"""
Instap Device Model main module.
"""
from .item import fetch_item, fetch_items
from .logger import get_logger
from .modbus_register import ModbusRegister
from .modbus.client import ModbusClient


class DeviceModel:
    """Main Device Model class."""
    
    def __init__(self, slug):
        self.slug = slug
        self.name = None
        self.modbus_registers = []
        self.modbus_client = None
        self.logger = get_logger("instap.device_model")
        self.logger.debug(f"Initializing DeviceModel with slug: {self.slug}")
        data = fetch_item("device_model", f"slug=eq.{self.slug}")
        self.name = data.get('name')
        self.created_at = data.get('created_at')
        self.tags = data.get('tags')
        self.type = data.get('type')
        self.label = data.get('label')
        self.host = data.get('host')
        self.port = data.get('port')
        self.framer = data.get('framer')
        self.modbus_client = ModbusClient(self.host, self.port, self.framer)
        for modbus_register in fetch_items("modbus_register", f"device_model=eq.{self.slug}"):
            self.modbus_registers.append(ModbusRegister(modbus_register))
    
    def __str__(self):
        """String representation of the DeviceModel."""
        return f"DeviceModel(slug='{self.slug}', name='{self.name}', label='{self.label}')"
