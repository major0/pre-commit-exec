import subprocess
import sys

def main():
    result = subprocess.run(sys.argv[1:], capture_output=True, shell=False, text=True)
    sys.stderr.write(result.stderr)
    sys.stderr.flush()
    sys.stdout.write(result.stdout)
    sys.stdout.flush()
    sys.exit(result.returncode)
