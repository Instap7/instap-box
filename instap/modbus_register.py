"""
Instap Modbus Register main module.
"""
from pymodbus.client import mixin
from .item import fetch_item, fetch_items
from .logger import get_logger


class ModbusRegister:
    """Main Modbus Register class."""

    def __init__(self, data):
        self.data = data
        self.slug = data.get('slug')
        self.name = None
        self.logger = get_logger("instap.modbus_register")
        self.logger.debug(f"Initializing ModbusRegister with data: {self.data}")
        self._process_data()
        # TODO:
        self.client = None

    # To trzeba przeniesc do processora
    def _process_data(self):
        self.name = self.data.get('name')
        self.created_at = self.data.get('created_at')
        self.tags = self.data.get('tags')
        self.type = self.data.get('type')
        self.unit = self.data.get('unit')
        self.gain = self.data.get('gain')
        self.offset = self.data.get('offset')
        self.quantity = self.data.get('quantity')
        self.address = self.data.get('address')
        self.device_model = self.data.get('device_model')
        self.parameter = self.data.get('parameter')
        self.function = self.data.get('function')
        self.label = self.data.get('label')
        self.type_reg = self.data.get('type_reg')
        DATA_TYPE = mixin.ModbusClientMixin.DATATYPE
        try:
            if self.function == 3:
                result = self.client.read_holding_registers(self.address, count=int(self.quantity))
            elif self.function == 4:
                result = self.client.read_input_registers(self.address, count=int(self.quantity))
            else:
                self.logger.error(f"Invalid function: {self.function}")

            if result.isError():
                self.logger.error(f"Error reading register {self.address}: {result}")
            else:
                # Dekodowanie wartości
                registers = result.registers

                if self.type_reg == "I16":
                    value = self.client.convert_from_registers(registers, data_type=DATA_TYPE.INT16)
                elif self.type_reg == "U16":
                    value = self.client.convert_from_registers(registers, data_type=DATA_TYPE.UINT16)
                elif self.type_reg == "I32" and len(registers) >= 2:
                    value = client.convert_from_registers(registers, data_type=DATA_TYPE.INT32)
                elif self.type_reg == "U32" and len(registers) >= 2:
                    value = client.convert_from_registers(registers, data_type=DATA_TYPE.UINT32)
                elif self.type_reg == "F32" and len(registers) >= 2:
                    pass
                elif self.type_reg == "H64":
                    byte_array = bytearray()
                    for reg in registers:
                        byte_array.extend(reg.to_bytes(2, byteorder="big"))
                    value = byte_array.decode("utf-8", errors="ignore").strip("\x00")
                else:
                    value = registers[0]

                self.logger.info(f"Register {self.address}: {value} {self.unit}")

        except Exception as e:
            self.logger.error(f"Error processing record {self.label}: {e}")

    def __str__(self):
        """String representation of the ModbusRegister."""
        return f"ModbusRegister(slug='{self.slug}', name='{self.name}', address='{self.address}', function='{self.function}', type='{self.type}', gain='{self.gain}')"
