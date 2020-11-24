import os
import glob
import subprocess

# cfgs = glob.glob(r"tests/darknet/cfg/target_*.cfg")
cfgs = glob.glob(r"tests/darknet/cfg/effnet_*.cfg")
# cfgs = glob.glob(r"tests/darknet/cfg/mb_*.cfg")
# cfgs = glob.glob(r"tests/darknet/cfg/*.cfg")
# cfgs = glob.glob(r"tests/darknet/new_cfg/*")

n = 100 # 몇번 반복할 것인지
# build/test_custom_cfgbuilder tests/darknet/cfg/target_*.cfg [n_iteration]

for cfg in cfgs:
    print(f"Let's run {cfg}")

    process = subprocess.run(
        # ['sudo', '/opt/nvidia/nsight_systems/nsys', 'profile', '-t', 'cuda,nvtx', '-o', f'/sdcard/nsys_results/{os.path.basename(cfg)}_{str(n)}try', '--force-overwrite', 'true', '--export', 'sqlite', 'build/test_custom_cfgbuilder',f'{cfg}', str(n)],
        ['sudo', '/opt/nvidia/nsight_systems/nsys', 'profile', '-t', 'cuda,nvtx', '-o', f'/sdcard/nsys_results/sync/{os.path.basename(cfg)}_{str(n)}try', '--force-overwrite', 'true', '--export', 'sqlite', 'build/test_custom_cfgbuilder',f'{cfg}', str(n)],
        stdout=subprocess.PIPE,
        universal_newlines=True)
    print(process)