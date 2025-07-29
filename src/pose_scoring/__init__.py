import numpy as np
from rich import print as rprint
import gemmi

def titration(pdb_path, chain, insertion_id, map_path):
    # Load files
    try:
        st = gemmi.read_structure(str(pdb_path))
    except:
        rprint(f'Error! Unable to open file {pdb_path}.')
        exit()
    try:
        ccp4 = gemmi.read_map_file(str(map_path))
        zmap = ccp4.grid
        zmap_array = np.array(zmap)
    except:
        rprint(f'Error! Unable to open file {map_path}.')
        exit()

    # Get ligand res
    try:
        res = st[0][str(chain)][str(insertion_id)]
    except:
        rprint(f'Error! Chain {chain} insertion {insertion_id} not in {pdb_path}.')
        exit()

    # Get a grid
    mask = gemmi.FloatGrid(zmap.nu, zmap.nv, zmap.nw)
    mask.set_unit_cell(zmap.unit_cell)

    # Integrate around each atom
    for atom in res:
        mask.set_points_around(atom.pos, radius=1.0, value=1.0)

        values = zmap_array[mask.array == 1.0]

        mask.set_points_around(atom.pos, radius=1.0, value=0.0)

        rprint(f'{atom.name} : {np.mean(values)}')


    # readout

    ...