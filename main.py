#!/usr/bin/env python3
"""
Main entry point for the Instap Box application.
Reads INSTAP_BOX from command line argument.
"""

import sys
import argparse
import logging
import traceback
import time
from instap.box import InstapBox
from instap.logger import setup_logger, get_logger
from instap.modbus.processor import ModbusProcessor

modbus_registers = []

def main_process(instap_box_slug):
    """
    Main process function that processes all modbus registers in a loop.
    
    Args:
        instap_box_slug (str): The Instap Box slug
    """
    instap_box = InstapBox(instap_box_slug)
    logger = get_logger("main")
    
    while True:
        try:
            logger.info(f"Starting processing cycle for Instap Box: {instap_box_slug}")
            all_modbus_registers = instap_box.get_all_modbus_registers()
            
            for modbus_register in all_modbus_registers:
                try:
                    modbus_processor = ModbusProcessor(modbus_register)
                    modbus_processor.process_modbus_register()
                except Exception as e:
                    logger.error(f"Error processing modbus register {modbus_register}: {e}")
                    logger.error(traceback.format_exc())
            
            logger.info(f"Completed processing cycle. Processed {len(all_modbus_registers)} registers.")
            logger.info("Waiting 60 seconds before next cycle...")
            time.sleep(60)
            
        except KeyboardInterrupt:
            logger.info("Received interrupt signal. Stopping...")
            break
        except Exception as e:
            logger.error(f"Error in main process: {e}")
            logger.error(traceback.format_exc())
            logger.info("Waiting 60 seconds before retry...")
            time.sleep(60)
    
    return all_modbus_registers

def main():
    """Main function that initializes and runs the Instap Box application."""
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Instap Box Application')
    parser.add_argument('--instap-box', '-i', required=True,
                       help='INSTAP_BOX value')
    parser.add_argument('--log-level', '-l', default='INFO',
                       choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                       help='Logging level (default: INFO)')
    parser.add_argument('--log-file', '-f', 
                       help='Log file path (optional)')
    args = parser.parse_args()
    
    instap_box_slug = args.instap_box
    
    # Setup logger
    log_level = getattr(logging, args.log_level.upper())
    log_to_file = args.log_file is not None
    logger = setup_logger(level=log_level, log_to_file=log_to_file, log_file=args.log_file)
    
    logger.info(f"Starting Instap Box with value: {instap_box_slug}")
    logger.info("Running in continuous loop mode (60s interval)")
    
    try:
        main_process(instap_box_slug)
        logger.info("Instap Box application completed successfully")
    except Exception as e:
        logger.error(f"Error in Instap Box application: {e}")
        logger.error(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main() 