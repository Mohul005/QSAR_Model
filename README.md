# Molecular Descriptor Calculator & Common Nucleus Detector

A Python-based cheminformatics toolkit built using **RDKit** for analysing molecular structures from SMILES (Simplified Molecular Input Line Entry System).
This project currently contains two programs:

1. **Molecular Descriptor Calculator** – Calculates physicochemical and structural descriptors from SMILES input.
2. **Common Molecular Nucleus Detector** – Identifies the Maximum Common Substructure (MCS) among multiple molecules using their Bemis–Murcko scaffolds.

The toolkit is intended for educational and preliminary research applications in cheminformatics, medicinal chemistry, and Quantitative Structure–Activity Relationship (QSAR) studies.

---

## Features

### 1. Molecular Descriptor Calculator

Accepts multiple SMILES strings through an interactive input system and calculates the following molecular descriptors:

| Descriptor | Description |
|---|---|
| Molecular Weight | Molecular mass in g/mol |
| LogP | Estimated octanol–water partition coefficient |
| TPSA | Topological Polar Surface Area (Å²) |
| H-Bond Donors | Number of hydrogen-bond donor groups |
| H-Bond Acceptors | Number of hydrogen-bond acceptor groups |
| Rotatable Bonds | Number of rotatable bonds |
| Heavy Atoms | Number of non-hydrogen atoms |
| Aromatic Rings | Number of aromatic rings |
| Total Rings | Total number of rings |
| Fraction Csp3 | Fraction of saturated carbon atoms |
| Molar Refractivity | Descriptor related to molecular volume and polarizability |

**Output:**
- Molecular descriptor table.
- CSV file containing calculated descriptors for further analysis.

### 2. Common Molecular Nucleus Detector

Identifies the maximum common structural framework shared among multiple molecules.

**Workflow:**

1. Accepts multiple SMILES strings interactively.
2. Validates the molecular structures using RDKit.
3. Extracts Bemis–Murcko scaffolds from the molecules.
4. Uses RDKit's Maximum Common Substructure (MCS) algorithm.
5. Identifies the common molecular framework.
6. Displays the common structure as a 2D molecular image.

**Output:**
- Common substructure in SMARTS format.
- Number of common atoms and bonds.
- 2D visualization of the common structure.

---
### 3. QSAR Model
A machine-learning-based module that uses molecular descriptors and experimental biological activity data to develop a preliminary QSAR (Quantitative Structure–Activity Relationship) model.
The program uses **Multiple Linear Regression** to establish a mathematical relationship between molecular descriptors and biological activity (pIC₅₀).

### Features

- Uploads a QSAR dataset in CSV format.
- Trains a Multiple Linear Regression model.
- Calculates the coefficient of determination (R²).
- Displays the regression intercept and coefficients.
- Accepts molecular descriptors of a new compound interactively.
- Predicts the pIC₅₀ value of the new compound.
- Converts predicted pIC₅₀ into an estimated IC₅₀.

### Molecular Descriptors Used

| Descriptor | Description |
|---|---|
| MW | Molecular Weight |
| LogP | Lipophilicity |
| TPSA | Topological Polar Surface Area |
| HBD | Hydrogen Bond Donors |
| HBA | Hydrogen Bond Acceptors |
| RotB | Rotatable Bonds |

### Dataset Requirements

The program requires a CSV file named `qsar_dataset.csv`.

The dataset must contain the following columns:

```csv
MW,LogP,TPSA,HBD,HBA,RotB,pIC50
```

Each row represents one compound, with its molecular descriptors and corresponding experimental pIC₅₀ value.

**Important:** All compounds should ideally have activity measurements against the same biological target, obtained under comparable experimental conditions.

### Methodology

1. Upload the QSAR dataset.
2. Load the dataset using Pandas.
3. Separate molecular descriptors (independent variables) from pIC₅₀ (dependent variable).
4. Train a Multiple Linear Regression model.
5. Calculate the R² score.
6. Display the regression coefficients and intercept.
7. Accept descriptor values for a new compound.
8. Predict its pIC₅₀ using the trained model.
9. Convert the predicted pIC₅₀ into IC₅₀.

### Mathematical Model

The regression equation is:

\[
pIC_{50} = \beta_0 + \beta_1(MW) + \beta_2(LogP)
\]

\[
+ \beta_3(TPSA) + \beta_4(HBD) + \beta_5(HBA) + \beta_6(RotB)
\]

Where:

- β₀ = Regression intercept.
- β₁–β₆ = Regression coefficients.
- MW, LogP, TPSA, HBD, HBA and RotB = Molecular descriptors.

The predicted IC₅₀ is calculated using:

\[
IC_{50}(M)=10^{-pIC_{50}}
\]


### Scientific Limitations

- R² calculated on the training dataset does not establish predictive accuracy.
- A separate test dataset or appropriate cross-validation is required to evaluate generalization.
- Small datasets can lead to overfitting.
- Highly correlated molecular descriptors can affect regression coefficients.
- Predictions are meaningful only within the chemical and biological applicability domain of the training dataset.
- The model does not establish experimental biological activity.

## Installation

### Google Colab

Install RDKit using:

```python
!pip install rdkit pandas
```

### Local Python Environment

Install the dependencies:

```bash
pip install rdkit pandas
```

Import the required libraries in your Python environment.

---

## Usage

Both programs use an interactive SMILES input system.

1. Run the desired program.
2. Enter the SMILES string of the first molecule.
3. Continue entering SMILES strings for additional molecules.
4. Type `done` when all molecules have been entered.
5. The program processes the input and generates the output.

**Example input:**

```text
Enter SMILES: CC(=O)Oc1ccccc1C(=O)O
Enter SMILES: O=C(O)c1ccccc1O
Enter SMILES: O=C(O)c1ccccc1C
Enter SMILES: done
```

No manual modification of the source code is required to analyse a different set of molecules.

---

## Applications

This toolkit can be used for:

- Preliminary molecular descriptor analysis.
- QSAR dataset preparation.
- Comparative analysis of physicochemical properties.
- Identification of common molecular frameworks.
- Medicinal chemistry and scaffold analysis.
- Exploratory structure–activity relationship studies.

---

## Scientific Considerations and Limitations

- Calculated descriptors are computational estimates and should not be treated as experimental measurements.
- LogP and TPSA alone cannot establish a compound's bioavailability or permeability.
- The Common Nucleus Detector searches for shared structures within extracted Bemis–Murcko scaffolds. Consequently, it may miss common fragments outside those scaffolds.
- The detected MCS is a structural match, not necessarily a biologically relevant pharmacophore.
- A common nucleus does not establish similar biological activity.
- Reliable QSAR modelling requires suitable experimental activity data, consistent assay conditions, adequate dataset size, and appropriate model validation.

---



