"""
Instap Device Model main module.
"""
from .item import fetch_item, fetch_items
from .logger import get_logger


class DeviceModel:
    """Main Device Model class."""
    
    def __init__(self, data):
        self.data = data
        self.slug = data.get('slug')
        self.name = data.get('name')
        self.logger = get_logger("instap.device_model")
        self.logger.debug(f"Initializing DeviceModel with slug: {self.slug}")
        self._process_data()
    
    def _process_data(self):
        """Process device model data."""
        self.logger.debug(f"Processing device model data for slug: {self.slug}")
        self.created_at = self.data.get('created_at')
        self.tags = self.data.get('tags')
        self.type = self.data.get('type')
        self.label = self.data.get('label')
    
    def __str__(self):
        """String representation of the DeviceModel."""
        return f"DeviceModel(slug='{self.slug}', name='{self.name}', label='{self.label}')"
