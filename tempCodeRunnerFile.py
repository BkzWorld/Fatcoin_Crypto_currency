import subprocess

scripts = ['Create Cryptocurrency/fatcoin_node_5005.py', 'Create Cryptocurrency/fatcoin_node_5006.py', 'Create Cryptocurrency/fatcoin_node_5007.py']

for script in scripts:
    subprocess.Popen(['python', script])