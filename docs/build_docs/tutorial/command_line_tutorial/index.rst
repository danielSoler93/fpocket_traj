From Command Line
==========================

Analyze Pocket characteristics along MD
-----------------------------------------

The command below will output a results.csv with all the pocket caracteristics along the snapshots
of the MD that the pocket has been correctly found

::

  python -m fpocket_traj.main <trajectory> --traj_len 130000 --sieve 1000 --output md_fpocket_analysis (folder of the output) --residues pocket_residues --top topology --nocopy (remove snapshots after being used) --nooutput (remove fpocket output)

  python -m fpocket_traj.main MD.xtc --residue 210 211 223 356 --top topology.pdb --traj_len 130000 --sieve 1000
