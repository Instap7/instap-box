"""
Modbus processor module for handling modbus register processing.
"""

from instap.logger import get_logger


class ModbusProcessor:
    """Class for processing modbus registers."""
    
    def __init__(self, modbus_register):
        """Initialize the ModbusProcessor."""
        self.logger = get_logger(__name__)
        self.modbus_register = modbus_register
    
    def process_modbus_register(self):
        """
        Process a modbus register.
        
        Args:
            modbus_register: The modbus register to process
        """
        self.logger.info(f"Processing modbus register {self.modbus_register}")