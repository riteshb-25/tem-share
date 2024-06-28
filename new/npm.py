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
    run_with_timeout(function_to_run, 120)
