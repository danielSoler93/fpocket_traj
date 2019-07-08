From Command Line
==========================

N most similar structures
---------------------------------------


     Given a database.sdf and a molecule.sdf will output the n most similar structures to the query molecule (--n_structs to specify the number of outputted structures)

    ::

     python -m analogs_finder.mainpy <database (sdf)> <query_molecule (sdf)> --sb --n <number of output structs> --output <outputname>

     python -m analogs_finder.main analogs_finder/examples/database.py analogs_finder/examples/substructre_1.sdf  --most_similars --n 20 --output most_similars.sdf



Tanimoto similarity search
------------------------------------------------------


     Will retrieve all molecules on the database.sdf that has a tanimoto similarity higher than treshold in respect to the query molecule (0.7 by default, you can specify by --tresh 0.6)

    ::

       python -m analogs_finder.main <database (sdf)> <query_molecule (sdf)> --treshold tanimoto_treshold --output <outputname>

       python -m analogs_finder.main analogs_finder/examples/actives_final.sdf  analogs_finder/examples/substructre_1.sdf --output most_similars.sdf --tresh 0.7



Search for  one or more substructure
--------------------------------------------------

       For each entry in database.py search for the substructure/s present in the query_molecule.sdf

    ::

       python -m analogs_finder.main <database (sdf)> <substructure_moleculeS (sdf with several entries (substructures)> --substructure --output <outputname>

       python analogs_finder.main analogs_finder/examples/actives_final.sdf analogs_finder/examples/substructre_1.sdf --output most_similars.sdf --substructure



Search for at least one of the substructures in each sdf file
-------------------------------------------------------------------

       For each entry in database.py search for **at least** one substructure present in the **each** sdf file

    ::

       python -m analogs_finder.main <database (sdf)> <substructure_moleculeS (sdf with several entries (substructures)> --combi_subsearch --output <outputname>

       python analogs_finder.main analogs_finder/examples/actives_final.sdf analogs_finder/examples/substructre_*.sdf --output most_similars.sdf --combi_subsearch




Search for similarity and substructure
----------------------------------------

       For each entry in database.py search for **at least** one substructure present in the **each** sdf file

    ::

       python -m analogs_finder.main <database (sdf)> <query_molecule (sdf with several entries (substructures)>  --output <outputname> --hybrid <substructure sdf file>

       python analogs_finder.main analogs_finder/examples/actives_final.sdf analogs_finder/examples/query_mol.sdf --output most_similars.sdf --hybrid analogs_finder/examples/substructure_1.sdf





