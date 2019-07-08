import subprocess
import os

_POCKET_NUMBER = "pocket_number"
_FRAME = "frame"

class FPocket():

    def __init__(self, file, residues):
        self.file = file
        self.residues = residues
    
    def run(self):
        command = "fpocket -f {} > /dev/null 2>&1".format(self.file)
        subprocess.call(command.split())
        self.basename = self.file.rsplit(".", 1)[0]
        self.output_dir = self.basename + "_out/"
        self.output_name = os.path.join(self.output_dir, os.path.basename(self.basename + "_info.txt")) 
        self.output_pockets = os.path.join(self.output_dir, "pockets")
        return self.output_name, self.output_dir

    def analyze_results(self):
        self.pockets = [Pocket(pocket_info) for pocket_info in self._retrieve_pocket_info().values()]
        self.pocket_info = self._identify_chosen_pocket()
        return self.pocket_info
        

    def _retrieve_pocket_info(self):
        pockets ={}
        pocket_idx = 0
        with open(self.output_name, "r") as f:
            for line in f:
                if line.strip("\n"):
                    if line.startswith("Pocket"):
                         if not pocket_idx == 0:
                             pockets[pocket_idx] = pocket_info
                         pocket_info = {}
                         pocket_idx += 1
                    else:
                         field, value = line.split(":") 
                         pocket_info[field.strip()] = value.strip()
                         pocket_info[_POCKET_NUMBER] = pocket_idx
                         pocket_info[_FRAME] = os.path.basename(self.basename)
        return pockets


    def _identify_chosen_pocket(self):
        for pocket in self.pockets:
            idx = pocket.pocket_number
            pocket_file = os.path.join(self.output_pockets, "pocket{}_atm.pdb".format(idx))
            with open(pocket_file, "r") as f:
                lines = f.readlines()
                found = 0
                import pdb; pdb.set_trace()
                for residue in self.residues:
                    for line in lines:
                        #Not to get a coordinate
                        if " " + residue + " " in line:
                            found += 1
                            print(line)
                            print(found)
                            break
                     
                    #if any(residue in line  for line in lines):
                    #    found += 1
                if found == len(self.residues):
                    print(pocket_file)
                    print(pocket.__dict__)
                    print(idx)
                    return pocket
        print("Residue not found  in snapshot {}".format(self.basename))    


class Pocket(FPocket):
    
    def __init__(self, pocket_info):
        self.retrieve_attributes(pocket_info)
    
    def retrieve_attributes(self, pocket_info):
        for key, value in pocket_info.items():
            setattr(self, key, value)
        return self
