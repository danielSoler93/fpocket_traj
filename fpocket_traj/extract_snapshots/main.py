import mdtraj as md
import os
import subprocess
import fpocket_traj.helpers.main as hp



CPPTRAJ_COMMAND=" \
parm {}\n \
trajin {} {} {}\n \
trajout {} onlyframes 1\n \
"


def extract_snapshot(traj, top, snapshot_index, snapshot_file="snap.pdb"):
    cpptraj_file = write_cpptraj_input(traj, top, snapshot_index, snapshot_file)
    command = "cpptraj -i {} -o cpptraj.log".format(cpptraj_file)
    subprocess.call(command.split())
    return os.path.abspath(snapshot_file)


def write_cpptraj_input(traj, top, index, name, cpptraj_file="cpptraj.in"):
    with open(cpptraj_file, "w") as f:
        f.write(CPPTRAJ_COMMAND.format(top, traj, index, index+1, name))
    return os.path.abspath(cpptraj_file)
