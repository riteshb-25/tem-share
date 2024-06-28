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
