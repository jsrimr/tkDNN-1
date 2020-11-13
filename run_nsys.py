import os
import glob
import subprocess

# cfgs = glob.glob(r"build/test_custom_cfgbuilder_*")
cfgs = glob.glob(r"tests/darknet/cfg/target_*.cfg")
n = 100
##build/test_custom_cfgbuilder tests/darknet/cfg/target_*.cfg [n_iteration]

for cfg in cfgs:
    print(f"Let's run {cfg}")

    process = subprocess.run(
        ['sudo', '/opt/nvidia/nsight_systems/nsys', 'profile', '-t', 'cuda,nvtx', '-o', f'/sdcard/nsys_results/{os.path.basename(cfg)}', '--force-overwrite', 'true', '--export', 'sqlite', 'build/test_custom_cfgbuilder',f'{cfg}', n],
        stdout=subprocess.PIPE,
        universal_newlines=True)
    print(process)