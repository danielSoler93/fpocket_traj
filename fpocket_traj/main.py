import matplotlib
matplotlib.use("Agg")
import argparse
from tqdm import tqdm
import pandas as pd
import sys
import os
import fpocket_traj.extract_snapshots.main as es
import fpocket_traj.helpers.main as hp
import fpocket_traj.fpocket.main as fp
import fpocket_traj.visualization.main as vs


def parse_args():
    parser = argparse.ArgumentParser(description='Run fdpocket for trajectories')
    parser.add_argument('traj',  type=str, help='Trajectory file your trajectory')
    parser.add_argument('--residues',  nargs="+", type=str, help='Resnum to study', required=True)
    parser.add_argument('--top',  type=str, help='Topology file of your trajectory. Not nedd it if traj is a pdb')
    parser.add_argument('--traj_len',  type=int, required=True,  help='Trajectory length')
    parser.add_argument('--sieve',  type=int, help='Number of snapshots to jump from one frame to the other', default=1)
    parser.add_argument('--output',  type=str, help='Output directory name', default="output")
    parser.add_argument('--nocopy',  action="store_false", help='Do not copy the snapshots being used')
    parser.add_argument('--noremove',  action="store_false", help='Do not remove fpocket output')
    args = parser.parse_args()
    return os.path.abspath(args.traj), args.residues, os.path.abspath(args.top), args.traj_len, args.sieve, args.output, args.nocopy, args.noremove


def run(traj, residues, top, snapshots, sieve=1, output="snapshots", copy=True, remove=True):
    hp.create_dir(output)
    pocket_info = pd.DataFrame()
    with hp.cd(output):
        for i in tqdm(range(0, snapshots, sieve)):
            frame = "frame_{}.pdb".format(i)

            snapshot = es.extract_snapshot(traj, top, i, snapshot_file=frame)
            fpocket = fp.FPocket(snapshot, residues)
            result, result_dir = fpocket.run()
            pocket = fpocket.analyze_results()
            if pocket:
                pocket_info = pocket_info.append(pd.Series(pocket.__dict__.values(), index=pocket.__dict__.keys()), ignore_index=True)

            if remove:
                hp.remove(snapshot, copy=copy)
                hp.remove_dir(result_dir)
    pocket_info.to_csv("results_pocket.csv")


if __name__ == '__main__':
    traj, residues, top, snapshots, sieve, output, copy, remove = parse_args()
    run(traj, residues, top, snapshots, sieve=sieve, output=output, copy=copy, remove=remove)



