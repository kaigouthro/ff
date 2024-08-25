
import os
import subprocess

os.environ['PIP_BREAK_SYSTEM_PACKAGES'] = '1'
subprocess.call([ 'uv', 'pip', 'install', 'inquirer', '-q' ])

from facefusion import installer

if __name__ == '__main__':
	installer.cli()
