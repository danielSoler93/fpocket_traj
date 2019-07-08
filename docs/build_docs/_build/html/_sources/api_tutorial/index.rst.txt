From python API
=================


Load your query molecule and your database
--------------------------------------------

::

  from rdkit import Chem

  database = "examples/database.sdf"
  qmolecule = "examples/substructure_1.sdf"

  molecules_db= Chem.SDMolSupplier(database)
  molecule_query = next(Chem.SDMolSupplier(qmolecule))


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
  for m in similars_no_duplicates: w.write(m)


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
  for m in similars_no_duplicates: w.write(m)


Substructure Search
-----------------------

The search_substructure will output molecules
with at least one of the substructures on you query sdf file

::

  substructures = "example/substructure2.sdf"

  molecule_query = Chem.SDMolSupplier(substructures)
  similars  = mt.search_substructure(molecule_query, molecules_db)
  similars_no_duplicates = hp.remove_duplicates(similars)
  
  w = Chem.SDWriter(output)
  for m in similars_no_duplicates: w.write(m)

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
 
  substructures_sdf = glob.glob("examples/subs*.sdf")

  similars = mt.combi_substructure_search(substructures_sdf, molecules_db)
  similars_no_duplicates = hp.remove_duplicates(similars)
  
  w = Chem.SDWriter(output)
  for m in similars_no_duplicates: w.write(m)


Similarity and Substructure hybrid search
------------------------------------------

The most_similar_with_substructure method will output
molecules with a tanimoto similarity coefficient higher 
than certain treshold that also contain certain substructure

::

  molecule_query = next(Chem.SDMolSupplier("examples/query_molecule.sdf"))
  substructure_file = "examples/substructure.sdf"

  similars = most_similar_with_substructure(molecule_query, molecules_db, substructure_file, treshold)
  similars_no_duplicates = hp.remove_duplicates(similars)
  
  w = Chem.SDWriter(output)
  for m in similars_no_duplicates: w.write(m)




