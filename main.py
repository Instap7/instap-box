#!/usr/bin/env python3
"""
Main entry point for the Instap Box application.
Reads INSTAP_BOX from command line argument.
"""

import sys
import argparse
from instap.box import InstapBox
from instap.modbus.processor import ModbusProcessor

def main():
    """Main function that initializes and runs the Instap Box application."""
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Instap Box Application')
    parser.add_argument('--instap-box', '-i', required=True,
                       help='INSTAP_BOX value')
    args = parser.parse_args()
    
    instap_box_value = args.instap_box
    
    print(f"Starting Instap Box with value: {instap_box_value}")
    
    try:
        # Initialize the main Instap Box
        instap_box = InstapBox(instap_box_value)
        
        # Initialize Modbus processor
        processor = ModbusProcessor()
        
        # Start the application
        instap_box.start()
        processor.start()
        
        print("Instap Box application started successfully")
        
    except Exception as e:
        print(f"Error starting Instap Box application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 