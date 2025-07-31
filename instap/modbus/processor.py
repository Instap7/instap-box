"""
Modbus processor module for handling modbus register processing.
"""
from pymodbus.client import mixin

from instap.logger import get_logger


class ModbusProcessor:
    """Class for processing modbus registers."""
    
    def __init__(self, modbus_client):
        """Initialize the ModbusProcessor."""
        self.logger = get_logger(__name__)
        self.modbus_client = modbus_client.client

    def process_register(self, register):
        """Process register from the modbus client."""
        self.logger.info(f"Processing register {register} from modbus client {self.modbus_client}")
        DATA_TYPE = mixin.ModbusClientMixin.DATATYPE
        try:
            if register.function == 3:
                result = self.modbus_client.read_holding_registers(register.address, count=int(register.quantity))
            elif register.function == 4:
                result = self.modbus_client.read_input_registers(register.address, count=int(register.quantity))
            else:
                self.logger.error(f"Invalid function: {register.function}")

            if result.isError():
                self.logger.error(f"Error reading register {register.address}: {result}")
            else:
                registers = result.registers

                if register.type_reg == "I16":
                    value = self.modbus_client.convert_from_registers(registers, data_type=DATA_TYPE.INT16) / register.gain
                elif register.type_reg == "U16":
                    value = self.modbus_client.convert_from_registers(registers, data_type=DATA_TYPE.UINT16) / register.gain
                elif register.type_reg == "I32" and len(registers) >= 2:
                    value = self.modbus_client.convert_from_registers(registers, data_type=DATA_TYPE.INT32) / register.gain
                elif register.type_reg == "U32" and len(registers) >= 2:
                    value = self.modbus_client.convert_from_registers(registers, data_type=DATA_TYPE.UINT32) / register.gain
                elif register.type_reg == "F32" and len(registers) >= 2:
                    pass
                elif register.type_reg == "H64":
                    byte_array = bytearray()
                    for reg in registers:
                        byte_array.extend(reg.to_bytes(2, byteorder="big"))
                    value = byte_array.decode("utf-8", errors="ignore").strip("\x00")
                else:
                    value = registers[0]

                self.logger.info(f"Register {register.address}: {value} {register.unit}")

        except Exception as e:
            self.logger.error(f"Error processing record {register.label}: {e}")
