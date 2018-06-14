import subprocess

def run(command, *args, **kwargs):
    print("+ {}".format(command))
    subprocess.run(command, *args, **kwargs)

run("git submodule update --init", shell=True)
run("pip install -e magma", shell=True)
run("pip install -e mantle", shell=True)
run("pip install -e loam", shell=True)
run("pip install fabricate", shell=True)
run("pip install jupyter", shell=True)
