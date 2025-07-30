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
        self.unit = self.data.get('unit')
        self.gain = self.data.get('gain')
        self.offset = self.data.get('offset')
        self.quantity = self.data.get('quantity')
        self.address = self.data.get('address')
        self.device_model = self.data.get('device_model')
        self.parameter = self.data.get('parameter')
        self.function = self.data.get('function')
        self.label = self.data.get('label')
    
    def __str__(self):
        """String representation of the ModbusRegister."""
        return f"ModbusRegister(slug='{self.slug}', name='{self.name}', address='{self.address}', function='{self.function}', type='{self.type}')" 