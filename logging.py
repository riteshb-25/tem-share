import logging

def setup_logger(log_file_path='azure_subscription_cancellation.log'):
    # Create a logger
    logger = logging.getLogger('azure_subscription_cancellation')
    logger.setLevel(logging.DEBUG)

    # Create a file handler and set the level to debug
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG)

    # Create a console handler and set the level to debug
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create a formatter and attach it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

if __name__ == "__main__":
    # Set up the logger
    logger = setup_logger()

    # Example usage of the logger
    try:
        # Your cancellation logic here

        # Log successful cancellation
        logger.info("Azure subscription cancellation successful.")
    except Exception as e:
        # Log any exceptions that occur during cancellation
        logger.error(f"Error during Azure subscription cancellation: {str(e)}", exc_info=True)



import logging

def setup_logger(log_file_path='azure_subscription_cancellation.log'):
    # Create a logger
    logger = logging.getLogger('azure_subscription_cancellation')
    logger.setLevel(logging.DEBUG)

    # Create a file handler and set the level to debug
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.DEBUG)

    # Create a console handler and set the level to debug
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create a formatter and attach it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

if __name__ == "__main__":
    # Set up the logger
    logger = setup_logger()

    # Example usage of the logger
    try:
        # Your cancellation logic here

        # Log successful cancellation
        logger.info("Azure subscription cancellation successful.")
    except Exception as e:
        # Log any exceptions that occur during cancellation
        logger.error(f"Error during Azure subscription cancellation: {str(e)}", exc_info=True)


//This script defines a Logger class with an __init__ method that takes the path of the log file as a parameter. The log_entry method is used to log data into the file in the specified JSON format.

//Please replace the example data with the actual data you want to log. Also, make sure to handle exceptions appropriately based on your specific requirements.

//Remember that this is a basic example, and depending on your use case, you might want to enhance the error handling, add more features, or use a more sophisticated logging library like logging in Python.

import json
from datetime import datetime

class Logger:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

    def log_entry(self, subscription_id, subscription_name, request_name, spn_id, spn_name, task_status):
        timestamp = datetime.utcnow().isoformat()
        entry = {
            "subscription_id": subscription_id,
            "subscription_name": subscription_name,
            "Request_name": request_name,
            "Request_time": timestamp,
            "status": task_status,
            "spn": {
                "spn_id": spn_id,
                "spn_name": spn_name
            },
            "task": {}
        }

        with open(self.log_file_path, 'a') as log_file:
            log_file.write(json.dumps(entry) + '\n')

# Example usage:
logger = Logger("log_file.json")

# Log entry for a successful task
logger.log_entry("12345678", "Azure Subscription 1", "CancelSubscription", "spn123", "SPN 1", True)

# Log entry for a failed task
logger.log_entry("87654321", "Azure Subscription 2", "CancelSubscription", "spn456", "SPN 2", False)
