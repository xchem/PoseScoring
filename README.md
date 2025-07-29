# PoseScoring
A repository for evaluating the evidence for a known ligand pose in electron density/PanDDA statistical maps. 

Example usage includes titration series scoring.

## Installation

```bash
git clone https://github.com/xchem/PoseScoring
cd PoseScoring
python -m pip install .
```

## Usage

### Titration Series

In order to evaluate the evidence for a fragment in a titration series you need:

1. A reference PDB containing the ligand pose
2. The insertion ID of the ligand
3. A PanDDA Z map

```bash
python scripts/titration.py pdb_path insertion_id z_map_path 
```

