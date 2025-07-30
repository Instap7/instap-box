"""
Global logger configuration for the Instap Box application.
"""
import logging
import sys
from typing import Optional


def setup_logger(
    name: str = "instap_box",
    level: int = logging.INFO,
    format_string: Optional[str] = None,
    log_to_file: bool = False,
    log_file: str = "instap_box.log"
) -> logging.Logger:
    """
    Setup and configure the global logger for the application.
    
    Args:
        name: Logger name
        level: Logging level (default: INFO)
        format_string: Custom format string for log messages
        log_to_file: Whether to log to file in addition to console
        log_file: Log file path if log_to_file is True
    
    Returns:
        Configured logger instance
    """
    # Configure root logger to propagate to all child loggers
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    
    # Clear existing handlers
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    # Default format string
    if format_string is None:
        format_string = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Create formatter
    formatter = logging.Formatter(format_string)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)
    
    # File handler (optional)
    if log_to_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)
    
    # Return the specific logger
    return logging.getLogger(name)


def get_logger(name: str = "instap_box") -> logging.Logger:
    """
    Get a logger instance with the specified name.
    
    Args:
        name: Logger name
    
    Returns:
        Logger instance
    """
    return logging.getLogger(name)


# Create default logger instance
logger = setup_logger() 