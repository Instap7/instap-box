"""
Instap Device main module.
"""
from .item import fetch_item, fetch_items
from .logger import get_logger
from .device_model import DeviceModel


class Device:
    """Main Device class."""
    
    def __init__(self, slug):
        self.slug = slug
        self.name = None
        self.logger = get_logger("instap.device")
        self.logger.debug(f"Initializing Device with slug: {slug}")
        self._fetch_item_data()
    
    def _fetch_item_data(self):
        """Fetch item data from the API based on slug."""
        self.logger.debug(f"Fetching item data for slug: {self.slug}")
        data = fetch_item(f"http://five.instap.app/api/sql/oneau/device?slug=eq.{self.slug}")
        self.name = data.get('name')
        self.created_at = data.get('created_at')
        self.tags = data.get('tags')
        self.image = data.get('image')
        self.type = data.get('type')
        self.facility = data.get('facility')
        self.instap_box = data.get('instap_box')
        self.label = data.get('label')
        model_slug = data.get('model')
        device_model = fetch_item(f"http://five.instap.app/api/sql/oneau/device_model?slug=eq.{model_slug}")
        self.model = DeviceModel(device_model.get('slug'))
    
    def __str__(self):
        """String representation of the Device."""
        return f"Device(slug='{self.slug}', name='{self.name}', facility='{self.facility}', instap_box='{self.instap_box}', model='{self.model}')"


class Parameter:
    """Parameter class for device parameters."""
    
    def __init__(self, slug):
        self.slug = slug
        self.name = None
        self.logger = get_logger("instap.parameter")
        self.logger.debug(f"Initializing Parameter with slug: {slug}")
        self._fetch_item_data()
    
    def _fetch_item_data(self):
        """Fetch parameter data from the API based on slug."""
        self.logger.debug(f"Fetching parameter data for slug: {self.slug}")
        data = fetch_item(f"http://five.instap.app/api/sql/oneau/parameter?slug=eq.{self.slug}")
        self.name = data.get('name')
        self.device = data.get('device')
        self.parameter_type = data.get('parameter_type')
        self.register_address = data.get('register_address')
        self.scale_factor = data.get('scale_factor')
        self.unit = data.get('unit')
    
    def __str__(self):
        """String representation of the Parameter."""
        return f"Parameter(slug='{self.slug}', name='{self.name}', device='{self.device}', parameter_type='{self.parameter_type}', register_address='{self.register_address}')" 