
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski, rdMolDescriptors
from rdkit.Chem import Crippen
import pandas as pd


def calculate_parameters(smiles_list):
    results = []

    for i, smiles in enumerate(smiles_list, start=1):
        mol = Chem.MolFromSmiles(smiles)

        if mol is None:
            print(f"Invalid SMILES skipped: {smiles}")
            continue

        # Calculate molecular descriptors
        parameters = {
            "Compound": f"Compound {i}",
            "SMILES": smiles,
            "Molecular Weight (g/mol)": round(
                Descriptors.MolWt(mol), 2
            ),
            "LogP": round(
                Crippen.MolLogP(mol), 2
            ),
            "TPSA (Å²)": round(
                rdMolDescriptors.CalcTPSA(mol), 2
            ),
            "H-Bond Donors": Lipinski.NumHDonors(mol),
            "H-Bond Acceptors": Lipinski.NumHAcceptors(mol),
            "Rotatable Bonds": Lipinski.NumRotatableBonds(mol),
            "Heavy Atoms": Lipinski.HeavyAtomCount(mol),
            "Aromatic Rings": Lipinski.NumAromaticRings(mol),
            "Total Rings": Lipinski.RingCount(mol),
            "Fraction Csp3": round(
                rdMolDescriptors.CalcFractionCSP3(mol), 3
            ),
            "Molar Refractivity": round(
                Crippen.MolMR(mol), 2
            )
        }

        results.append(parameters)

    if not results:
        print("No valid molecules were entered.")
        return

    # Display results as a table
    df = pd.DataFrame(results)

    print("\n========== MOLECULAR DESCRIPTORS ==========\n")
    print(df.to_string(index=False))

    # Save results to CSV for QSAR analysis
    df.to_csv("molecular_descriptors.csv", index=False)
    print("\nResults saved to molecular_descriptors.csv")

    return df


# Interactive SMILES input
smiles_input = []

print("=== Molecular Parameter Calculator ===")
print("Enter one SMILES string per line.")
print("Type 'done' when finished.\n")

while True:
    smiles = input("Enter SMILES: ").strip()

    if smiles.lower() == "done":
        break

    if smiles:
        smiles_input.append(smiles)

# Calculate parameters
if smiles_input:
    descriptor_table = calculate_parameters(smiles_input)
else:
    print("No SMILES strings entered.")
