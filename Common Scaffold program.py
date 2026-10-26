from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Scaffolds import MurckoScaffold
from rdkit.Chem import rdFMCS
from IPython.display import display


def identify_common_nucleus(smiles_list):
    molecules = []

    # Validate the SMILES inputs
    for i, smiles in enumerate(smiles_list, start=1):
        mol = Chem.MolFromSmiles(smiles)

        if mol is not None:
            molecules.append(mol)
        else:
            print(f"Invalid SMILES skipped: {smiles}")

    if len(molecules) < 2:
        print("Please provide at least two valid SMILES.")
        return

    # Extract Bemis-Murcko scaffolds
    scaffolds = [
        MurckoScaffold.GetScaffoldForMol(mol)
        for mol in molecules
    ]

    # Find the maximum common substructure
    result = rdFMCS.FindMCS(
        scaffolds,
        ringMatchesRingOnly=True,
        completeRingsOnly=True,
        matchValences=True,
        timeout=30
    )

    if result.canceled:
        print("The result may be incomplete.")

    if result.numAtoms == 0:
        print("No common scaffold found.")
        return

    # Generate and display the common structure
    common_mol = Chem.MolFromSmarts(result.smartsString)

    if common_mol is None:
        print("Could not generate the common structure.")
        return

    print("\n========== RESULTS ==========")
    print("Common nucleus (SMARTS):")
    print(result.smartsString)

    print("\nNumber of atoms:", result.numAtoms)
    print("Number of bonds:", result.numBonds)

    display(
        Draw.MolToImage(
            common_mol,
            size=(500, 400),
            legend="Common molecular nucleus"
        )
    )


# Interactive SMILES input system
smiles_input = []

print("Common Molecular Nucleus Detector")
print("Enter one SMILES string per line.")
print("Type 'done' when you have entered all molecules.\n")

while True:
    smiles = input("Enter SMILES: ").strip()

    if smiles.lower() == "done":
        break

    if smiles:
        smiles_input.append(smiles)

# Run the analysis
if len(smiles_input) >= 2:
    identify_common_nucleus(smiles_input)
else:
    print("Please enter at least two SMILES strings.")
