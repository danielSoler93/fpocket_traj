From python API
=================

Download examples
-------------------

From command line: git clone https://github.com/NostrumBioDiscovery/analogs_finder.git


Load your query molecule and your database
--------------------------------------------

::

  from rdkit import Chem

  database = "analogs_finder/examples/database.sdf"
  qmolecule = "analogs_finder/examples/substructre_1.sdf"

  molecules_db= Chem.SDMolSupplier(database)
  molecule_query = next(Chem.SDMolSupplier(qmolecule))

Analyze your dataset
-----------------------

The command below will output the tanimoto similarity distribution among
all dataset and all fingerprints, at the same time will show a plot
of the two first components of the PCA over the fingerprint space coloured
by similarity to your query molecule. If we hover the points of the plot
we can inspect the different structures of the molecules.

::
  
  from analogs_finder.analysis import analysis_dataset as an


  #Use Uniform manifold to plot the chemical space
  an.main(molecule_query, molecules_db, dim_type="umap")

  #Use PCA to plot the chemical space
  an.main(molecule_query, molecules_db, dim_type="pca")
 

We find the similarity_hist_DL.png:

.. figure:: ../../images/fp_dist.png
    :scale: 80%
    :align: center

And a firefox window opens retrieving and interactive plot:


.. figure:: ../../images/chemical_space.png
    :scale: 80%
    :align: center

Most Similars n Molecules
--------------------------------------

The search_most_similars method will output the n
molecules from your database most similar to your
query molecule

::
  
  from analogs_finder.search_methods import methods as mt
  from analogs_finder.helpers import helpers as hp

  output = "most_similars.sdf"
  n_structs = 50

  similars  = mt.search_most_similars(molecule_query, molecules_db, n_structs)
  similars_no_duplicates = hp.remove_duplicates(similars)
  
  w = Chem.SDWriter(output)
  for m in similars_no_duplicates: w.write(m.molecule)


Tanimoto Similarity Search
------------------------------

The search_similarity_tresh method will output
all molecules that have a tanimoto similarity higher
than a desired treshold

::

  treshold = 0.6

  similars  = mt.search_similarity_tresh(molecule_query, molecules_db, treshold)
  similars_no_duplicates = hp.remove_duplicates(similars)
  
  w = Chem.SDWriter(output)
  for m in similars_no_duplicates: w.write(m.molecule)


Substructure Search
-----------------------

The search_substructure will output molecules
with at least one of the substructures on you query sdf file

::

  substructures = "analogs_finder/examples/substructre_2.sdf"

  molecule_query = Chem.SDMolSupplier(substructures)
  similars  = mt.search_substructure(molecule_query, molecules_db)
  similars_no_duplicates = hp.remove_duplicates(similars)
  
  w = Chem.SDWriter(output)
  for m in similars_no_duplicates: w.write(m.molecule)

Combinatorial Substructure Search
---------------------------------------

The combi_substructure_search will output all molecules
with at least one substructures of each of the inputted
substructures sdf files

For example: I could look for structures with a 6 and 5 memeber ring,
so I will pass this two substructures in a sdf so at least one of them
have to be in the outputted molecules. But, at the same time I also want to
have an amide so I will pass another sdf file with  the amide substructure.
Finally, I will obtain structures with an amide and either a 5 or 6 memebr ring


::

  import glob

  substructures_sdf = glob.glob("analogs_finder/examples/subs*.sdf")

  similars = mt.combi_substructure_search(substructures_sdf, molecules_db)
  similars_no_duplicates = hp.remove_duplicates(similars)
  
  w = Chem.SDWriter(output)
  for m in similars_no_duplicates: w.write(m.molecule)


Similarity and Substructure hybrid search
------------------------------------------

The most_similar_with_substructure method will output
molecules with a tanimoto similarity coefficient higher 
than certain treshold that also contain certain substructure

::

  substructure_file = "analogs_finder/examples/substructre_3.sdf"

  similars = mt.most_similar_with_substructure(molecule_query, molecules_db, substructure_file, treshold=0.1)
  
  w = Chem.SDWriter(output)
  for m in similars_no_duplicates: w.write(m.molecule)



Use different fingerprints
------------------------------

::

  molecule_query = next(Chem.SDMolSupplier("examples/query_molecule.sdf"))
  substructure_file = "examples/substructure.sdf"

  similars_daylight = mt.search_most_similars(molecule_query, molecules_db, 2, fp_type="DL")
  similars_circular = mt.search_most_similars(molecule_query, molecules_db, 2, fp_type="circular")
  similars_torsions = mt.search_most_similars(molecule_query, molecules_db, 2, fp_type="torsions")
  similars_MACCS = mt.search_most_similars(molecule_query, molecules_db, 2, fp_type="MACCS")
  similars_pharm = mt.search_most_similars(molecule_query, molecules_db, 2, fp_type="pharm")


Use all four fingerprints to query one database with different tresholds
-------------------------------------------------------------------------------

::

  tresholds = [0.7, 0.4, 0.4, 0.6]
  fp_types = ["DL", "circular", "torsions", "MACCS"]
  similarts = mt.search_similarity_tresh_several_fp(molecule_query, molecules_db, tresholds=tresholds, fp_types=fp_types)

Turbo search method:
----------------------

Instead of just querying the reference molecule and setting a tanimoto treshold,
we first look for the N most similar neighbours and we run similarity search with
the reference molecule and theses neghbours, finally performing data fusion.

For more details: https://onlinelibrary.wiley.com/doi/abs/10.1002/sam.10037

::

 import analogs_finder.search_methods.fusion as fs
 turbo_similars = fs.turbo_similarity(molecule_query, molecules_db, neighbours=5, treshold=0.4, fp_type="circular") 
