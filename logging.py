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



/* Note: This code uses the tabulate library for formatting the table. Make sure to install it using pip install tabulate before running the code. You can customize the log_subscription_cancel method and the example usage according to your specific needs.*/

import json
from tabulate import tabulate  # Make sure to install tabulate using: pip install tabulate

class SubscriptionLogger:
    def __init__(self):
        self.logs = []

    def log_subscription_cancel(self, subscription_id, subscription_name, request_name, request_time, status, spn_id, spn_name, task):
        log_entry = {
            "subscription_id": subscription_id,
            "subscription_name": subscription_name,
            "request_name": request_name,
            "request_time": request_time,
            "status": status,
            "spn": {"spn_id": spn_id, "spn_name": spn_name},
            "task": task
        }

        self.logs.append(log_entry)

    def get_logs_table(self):
        headers = ["Subscription ID", "Subscription Name", "Request Name", "Request Time", "Status", "SPN ID", "SPN Name", "Task"]
        rows = []

        for log in self.logs:
            row = [
                log["subscription_id"],
                log["subscription_name"],
                log["request_name"],
                log["request_time"],
                log["status"],
                log["spn"]["spn_id"],
                log["spn"]["spn_name"],
                json.dumps(log["task"])
            ]
            rows.append(row)

        table = tabulate(rows, headers=headers, tablefmt="pretty")
        return table


# Example Usage:
logger = SubscriptionLogger()
logger.log_subscription_cancel(
    subscription_id="123456",
    subscription_name="Sample Subscription",
    request_name="CancelSubscription",
    request_time="2023-11-13T12:00:00",
    status=True,
    spn_id="789",
    spn_name="ServicePrincipal",
    task={"cancel_reason": "Project completion"}
)

# You can log more entries as needed

# Get the logs table
logs_table = logger.get_logs_table()
print(logs_table)


/*This example assumes that the log data is stored in a CSV file (log_table.csv). You can customize the file path and column names according to your needs. Also, make sure to install the pandas library if you haven't already:*/

import pandas as pd
from datetime import datetime

class Logger:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path
        self.columns = ["subscription_id", "subscription_name", "Request_name", "Request_time", "status",
                        "spn_id", "spn_name", "task"]

    def log_data(self, data):
        # Create or load the log file as a DataFrame
        try:
            log_df = pd.read_csv(self.log_file_path)
        except FileNotFoundError:
            log_df = pd.DataFrame(columns=self.columns)

        # Add a timestamp to the data
        data["Request_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Append the new data to the DataFrame
        log_df = log_df.append(data, ignore_index=True)

        # Save the DataFrame back to the log file
        log_df.to_csv(self.log_file_path, index=False)

if __name__ == "__main__":
    # Example of how to use the logger
    logger = Logger("log_table.csv")

    log_data = {
        "subscription_id": "123",
        "subscription_name": "Example Subscription",
        "Request_name": "Example Request",
        "status": True,
        "spn_id": "456",
        "spn_name": "Example SPN",
        "task": {"task_id": 789, "task_name": "Example Task"}
    }

    logger.log_data(log_data)


