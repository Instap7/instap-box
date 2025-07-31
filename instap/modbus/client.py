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

    def connect(self):
        """Connect to the modbus client."""
        self.logger.info(f"Connecting to modbus client {self}")
    
    def disconnect(self):
        """Disconnect from the modbus client."""
        self.logger.info(f"Disconnecting from modbus client {self}")

    def __str__(self):
        return f"ModbusClient(host='{self.host}', port='{self.port}', framer='{self.framer}')"
    