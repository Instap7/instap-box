"""
Modbus processor module for handling modbus register processing.
"""

from instap.logger import get_logger


class ModbusProcessor:
    """Class for processing modbus registers."""
    
    def __init__(self, modbus_client):
        """Initialize the ModbusProcessor."""
        self.logger = get_logger(__name__)
        self.modbus_client = modbus_client

    def process_register(self, register):
        """Process register from the modbus client."""
        self.logger.info(f"Processing register {register} from modbus client {self.modbus_client}")
