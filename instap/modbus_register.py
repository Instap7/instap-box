"""
Instap Modbus Register main module.
"""
from .item import fetch_item, fetch_items
from .logger import get_logger


class ModbusRegister:
    """Main Modbus Register class."""
    
    def __init__(self, data):
        self.data = data
        self.slug = data.get('slug')
        self.name = None
        self.logger = get_logger("instap.modbus_register")
        self.logger.debug(f"Initializing ModbusRegister with data: {self.data}")
        self._process_data()
    
    def _process_data(self):
        self.name = self.data.get('name')
        self.created_at = self.data.get('created_at')
        self.tags = self.data.get('tags')
        self.type = self.data.get('type')
        self.label = self.data.get('label')
        self.device_model = self.data.get('device_model')
        self.register_address = self.data.get('register_address')
        self.register_type = self.data.get('register_type')
        self.data_type = self.data.get('data_type')
        self.scale_factor = self.data.get('scale_factor')
        self.unit = self.data.get('unit')
        self.description = self.data.get('description')
        self.min_value = self.data.get('min_value')
        self.max_value = self.data.get('max_value')
        self.default_value = self.data.get('default_value')
        self.read_only = self.data.get('read_only')
        self.write_only = self.data.get('write_only')
    
    def __str__(self):
        """String representation of the ModbusRegister."""
        return f"ModbusRegister(slug='{self.slug}', name='{self.name}', register_address='{self.register_address}', register_type='{self.register_type}', data_type='{self.data_type}')" 