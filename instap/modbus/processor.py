"""
Modbus processor module.
"""
from ..logger import get_logger


class ModbusProcessor:
    """Modbus processor class."""
    
    def __init__(self):
        self.logger = get_logger("instap.modbus.processor")
    
    def start(self):
        """Start the Modbus processor."""
        self.logger.info("ModbusProcessor started") 