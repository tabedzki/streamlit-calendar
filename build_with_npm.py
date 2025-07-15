import subprocess
import sys
import os

def main():
    original_pwd = os.getcwd()
    print(f"Current working directory: {original_pwd}")
    frontend_dir = os.path.join(os.path.dirname(__file__), 'streamlit_calendar', 'frontend')
    os.chdir(frontend_dir)

    try:
        print(f"Running npm install in {frontend_dir}...")
        npm_cmd = ['npm', 'install']
        result = subprocess.run(npm_cmd, cwd=frontend_dir)
        if result.returncode != 0:
            print("npm install failed", file=sys.stderr)
            sys.exit(result.returncode)

        print(f"Running npm install in {frontend_dir}...")
        npm_cmd = ['npm', 'audit', 'fix']
        result = subprocess.run(npm_cmd, cwd=frontend_dir)
        if result.returncode != 0:
            print("npm install failed", file=sys.stderr)
            sys.exit(result.returncode)

        print(f"Running npm build in {frontend_dir}...")
        npm_cmd = ['npm', 'run', 'build']
        result = subprocess.run(npm_cmd, cwd=frontend_dir)
        if result.returncode != 0:
            print("npm build failed", file=sys.stderr)
            sys.exit(result.returncode)
        print("npm build succeeded.")
    finally:
        os.chdir(original_pwd)

if __name__ == "__main__":
    main()
