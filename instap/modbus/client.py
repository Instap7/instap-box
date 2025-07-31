"""
Modbus client module for handling modbus register processing.
"""

from instap.logger import get_logger


class ModbusClient:
    """Modbus client class."""
    
    def __init__(self, host, port, framer):
        """Initialize the ModbusClient."""
        self.logger = get_logger(__name__)
        self.host = host
        self.port = port
        self.framer = framer

    def __str__(self):
        return f"ModbusClient(host='{self.host}', port='{self.port}', framer='{self.framer}')"
    