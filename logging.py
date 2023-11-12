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


