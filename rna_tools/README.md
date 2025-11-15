# RNA Structure Processing and Prediction Tool

This directory contains Python scripts for processing RNA structure data from CIF files, predicting secondary structures, and saving the results.

## `process_rna_data.py`

This script demonstrates how to:
1. Parse a `.cif` file containing RNA 3D structure data using Biopython.
2. Extract the RNA sequence from the parsed structure.
3. Predict the RNA secondary structure (in dot-bracket notation) and its Minimum Free Energy (MFE) using the ViennaRNA package.
4. Save the extracted sequence and the predicted secondary structure with MFE to text files.

### Setup

To run this script, you need to set up a Python virtual environment and install the required libraries.

1.  **Create a virtual environment (if you haven't already):**
    ```bash
    python3 -m venv .venv
    ```

2.  **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```
    (On Windows, use `.venv\Scripts\activate`)

3.  **Install the required Python packages:**
    ```bash
    .venv/bin/pip install biopython viennarna
    ```

### Usage

The script is designed to process a single `.cif` file. You can modify the `example_cif_file` variable in the `if __name__ == "__main__":` block to point to any `.cif` file in your `rna3db-mmcifs` database.

**Example:**

```bash
.venv/bin/python3 code/rna_tools/process_rna_data.py
```

### Database Structure

The script expects the `rna3db-mmcifs` database to be located at `code/databases/rna3db-mmcifs` relative to the project root. The database has a nested structure:

```
code/databases/rna3db-mmcifs/
├── train_set/
│   ├── component_1/
│   │   ├── 1c2w_B/
│   │   │   └── 1c2w_B.cif
│   │   ├── ...
│   ├── component_X/
│   │   └── ...
└── test_set/
    └── ...
```

To process a different file, update the `example_cif_file` variable in `process_rna_data.py` accordingly.

### Output

The script will create an `output` directory (if it doesn't exist) in the project root. For each processed RNA chain, it will generate two text files:

*   `[structure_id]_[chain_id]_sequence.txt`: Contains the extracted RNA sequence.
*   `[structure_id]_[chain_id]_secondary_structure.txt`: Contains the predicted secondary structure in dot-bracket notation and its Minimum Free Energy (MFE).

**Example Output Files:**

*   `output/RNA_structure_B_sequence.txt`
*   `output/RNA_structure_B_secondary_structure.txt`

## Future Enhancements

*   **Batch Processing:** Extend the script to iterate through all `.cif` files in the database or a specified directory.
*   **Visualization:** Integrate with a more robust RNA secondary structure visualization library (e.g., VARNA, RNAplot from ViennaRNA, or a web-based viewer) to generate graphical representations.
*   **3D Structure Analysis:** Add functionality to perform basic analysis on the 3D coordinates using Biopython or other libraries.
*   **Error Handling:** Improve error handling for cases where CIF files are malformed or do not contain valid RNA sequences.
