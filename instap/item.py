"""
Instap Item module for fetching item data from API.
"""
import requests
from .logger import get_logger


def fetch_items(url):
    """
    Fetch item data from the Instap API.
    
    Args:
        context (str): API context (e.g., 'oneau')
        definition (str): Item definition (e.g., 'instap_box')
        slug (str): Item slug
    
    Returns:
        dict: Item data from API response, or None if error occurs
    """
    logger = get_logger("instap.item")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        logger.debug(f"Fetched item data for {url}: {data}")
        return data
        
    except requests.RequestException as e:
        logger.error(f"Error fetching item data for {url}: {e}")
        return None 
    
def fetch_item(url):
    data = fetch_items(url)
    return data[0]