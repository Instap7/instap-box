"""
Instap Device Model main module.
"""
from .item import fetch_item, fetch_items
from .logger import get_logger
from .modbus_register import ModbusRegister


class DeviceModel:
    """Main Device Model class."""
    
    def __init__(self, slug):
        self.slug = slug
        self.name = None
        self.modbus_registers = []
        self.logger = get_logger("instap.device_model")
        self.logger.debug(f"Initializing DeviceModel with slug: {self.slug}")
        self._process_data()
    
    def _process_data(self):
        """Process device model data."""
        self.logger.debug(f"Processing device model data for slug: {self.slug}")
        data = fetch_item(f"http://five.instap.app/api/sql/oneau/device_model?slug=eq.{self.slug}")
        self.name = data.get('name')
        self.created_at = data.get('created_at')
        self.tags = data.get('tags')
        self.type = data.get('type')
        self.label = data.get('label')
        for modbus_register in fetch_items(f"http://five.instap.app/api/sql/oneau/modbus_register?device_model=eq.{self.slug}"):
            modbus_register_slug = modbus_register.get('slug')
            self.modbus_registers.append(ModbusRegister(modbus_register_slug))
    
    def __str__(self):
        """String representation of the DeviceModel."""
        return f"DeviceModel(slug='{self.slug}', name='{self.name}', label='{self.label}')"
