import subprocess
import re

def run_npm_start_and_get_localhost_link(folder_path):
    # Run npm start in the specified folder
    process = subprocess.Popen(['npm', 'start'], cwd=folder_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Capture the output
    stdout, stderr = process.communicate()

    # Check for localhost link in the output
    localhost_link = None
    for line in stdout.split('\n'):
        match = re.search(r'(http://localhost:\d+)', line)
        if match:
            localhost_link = match.group(1)
            break

    if localhost_link:
        return localhost_link
    else:
        raise RuntimeError("Failed to find localhost link in npm start output")

# Example usage
folder_path = '/path/to/your/project'
try:
    link = run_npm_start_and_get_localhost_link(folder_path)
    print(f"Localhost link: {link}")
except Exception as e:
    print(f"Error: {e}")




import signal

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException

def function_to_run():
    # Your function logic here
    while True:
        print("Running...")
        time.sleep(1)  # Simulating long-running process

def run_with_timeout(func, timeout):
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)
    
    try:
        func()
    except TimeoutException:
        print("Function execution stopped after timeout.")
    finally:
        signal.alarm(0)  # Disable the alarm

if __name__ == "__main__":
    import time

    # Run the function with a timeout of 120 seconds
    run_with_timeout(function_to_run, 120






import threading
import time

def function_to_run():
    # Simulating a long-running process (5 minutes)
    for i in range(300):  # 300 seconds (5 minutes)
        print(f"Running... {i+1} seconds")
        time.sleep(1)  # Sleep for 1 second each iteration

def run_with_timeout(func, timeout):
    def wrapper():
        try:
            func()
        except Exception as e:
            print(f"Function stopped with exception: {e}")

    # Start the function in a separate thread
    thread = threading.Thread(target=wrapper)
    thread.start()

    # Wait for the specified timeout
    thread.join(timeout)

    if thread.is_alive():
        print("Function execution stopped after timeout.")
        # Thread is still running, need to stop it
        # Threads cannot be forcefully killed in Python
        # Therefore, you might need to structure your function to periodically check for an exit condition
        raise TimeoutException("Function execution stopped after timeout.")

class TimeoutException(Exception):
    pass

if __name__ == "__main__":
    # Run the function with a timeout of 20 seconds
    run_with_timeout(function_to_run, 20)

