"""
Instap Modbus Register main module.
"""
from .item import fetch_item, fetch_items
from .logger import get_logger


class ModbusRegister:
    """Main Modbus Register class."""
    
    def __init__(self, slug):
        self.slug = slug
        self.name = None
        self.logger = get_logger("instap.modbus_register")
        self.logger.debug(f"Initializing ModbusRegister with slug: {slug}")
        self._fetch_item_data()
    
    def _fetch_item_data(self):
        """Fetch modbus register data from the API based on slug."""
        self.logger.debug(f"Fetching modbus register data for slug: {self.slug}")
        data = fetch_item(f"http://five.instap.app/api/sql/oneau/modbus_register?slug=eq.{self.slug}")
        self.name = data.get('name')
        self.created_at = data.get('created_at')
        self.tags = data.get('tags')
        self.type = data.get('type')
        self.label = data.get('label')
        self.device_model = data.get('device_model')
        self.register_address = data.get('register_address')
        self.register_type = data.get('register_type')
        self.data_type = data.get('data_type')
        self.scale_factor = data.get('scale_factor')
        self.unit = data.get('unit')
        self.description = data.get('description')
        self.min_value = data.get('min_value')
        self.max_value = data.get('max_value')
        self.default_value = data.get('default_value')
        self.read_only = data.get('read_only')
        self.write_only = data.get('write_only')
    
    def __str__(self):
        """String representation of the ModbusRegister."""
        return f"ModbusRegister(slug='{self.slug}', name='{self.name}', register_address='{self.register_address}', register_type='{self.register_type}', data_type='{self.data_type}')" 