"""
Instap Box main module.
"""
from .item import fetch_item, fetch_items
from .logger import get_logger
from .device import Device


class InstapBox:
    """Main Instap Box class."""
    
    def __init__(self, slug):
        self.slug = slug
        self.name = None
        self.devices = []
        self.all_modbus_registers = []
        self.logger = get_logger("instap.box")
        self.logger.debug(f"Initializing InstapBox with slug: {slug}")
        self._fetch_item_data()
    
    def _fetch_item_data(self):
        """Fetch item data from the API based on slug."""
        self.logger.debug(f"Fetching item data for slug: {self.slug}")
        data = fetch_item("instap_box", f"slug=eq.{self.slug}")
        self.name = data.get('name')
        self.ip_address = data.get('ip_address')
        self.port = data.get('port')
        for device in fetch_items("device", f"instap_box=eq.{self.slug}"):
            device_slug = device.get('slug')
            self.devices.append(Device(device_slug))

    def get_all_modbus_registers(self, refresh=False):
        """Return all modbus registers for the Instap Box."""
        if refresh or len(self.all_modbus_registers) == 0:
            for device in self.devices:
                self.logger.info(f" * Device: {device}")
                self.logger.info(f"   > Model: {device.model}")
                for modbus_register in device.model.modbus_registers:
                    self.logger.info(f"     * Modbus Register: {modbus_register}")
                    self.all_modbus_registers.append(modbus_register)
        return self.all_modbus_registers
    
    def __str__(self):
        """String representation of the InstapBox."""
        return f"InstapBox(slug='{self.slug}', name='{self.name}', ip_address='{self.ip_address}', port='{self.port}')" 
