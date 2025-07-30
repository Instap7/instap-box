"""
Instap Box main module.
"""
from .item import fetch_item
from .logger import get_logger


class InstapBox:
    """Main Instap Box class."""
    
    def __init__(self, slug):
        self.slug = slug
        self.name = None
        self.logger = get_logger("instap.box")
        self.logger.debug(f"Initializing InstapBox with slug: {slug}")
        self._fetch_item_data()
    
    def _fetch_item_data(self):
        """Fetch item data from the API based on slug."""
        self.logger.debug(f"Fetching item data for slug: {self.slug}")
        data = fetch_item(f"http://five.instap.app/api/sql/oneau/device?instap_box=eq.ibox00002")
        self.name = data.get('name')
        self.ip_address = data.get('ip_address')
        self.port = data.get('port')
    
    def __str__(self):
        """String representation of the InstapBox."""
        return f"InstapBox(slug='{self.slug}', name='{self.name}', ip_address='{self.ip_address}', port='{self.port}')" 
