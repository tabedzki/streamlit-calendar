from hatchling.builders.hooks.plugin.interface import BuildHookInterface
import subprocess
import os

class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        frontend_dir = os.path.join(self.root, "streamlit_calendar", "frontend")
        subprocess.run(["npm", "install"], cwd=frontend_dir, check=True)
        subprocess.run(["npm", "run", "build"], cwd=frontend_dir, check=True)
