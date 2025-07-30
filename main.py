#!/usr/bin/env python3
"""
Main entry point for the Instap Box application.
Reads INSTAP_BOX from command line argument.
"""

import sys
import argparse
import logging
import traceback
from instap.box import InstapBox
from instap.modbus.processor import ModbusProcessor
from instap.logger import setup_logger, get_logger

def main_process(logger, instap_box_slug):
    # Initialize the main Instap Box
    instap_box = InstapBox(instap_box_slug)
    logger.info(f"Instap Box: {instap_box}")
    for device in instap_box.devices:
        logger.info(f" * Device: {device}")

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
    
    try:
        main_process(logger, instap_box_slug)
        logger.info("Instap Box application started successfully")
    except Exception as e:
        logger.error(f"Error starting Instap Box application: {e}")
        logger.error(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main() 