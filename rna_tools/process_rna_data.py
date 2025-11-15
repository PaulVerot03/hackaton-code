
import os
from Bio.PDB import MMCIFParser
from Bio.PDB.PDBExceptions import PDBException
import RNA 

def process_cif_file(cif_file_path, output_dir="output"):
    """
    Parses a .cif file, predicts secondary structure, and saves the sequence and structure to text files.
    """
    if not os.path.exists(cif_file_path):
        print(f"Error: File not found at {cif_file_path}")
        return

    parser = MMCIFParser()
    try:
        structure = parser.get_structure("RNA_structure", cif_file_path)
    except PDBException as e:
        print(f"Error parsing {cif_file_path}: {e}")
        return

    print(f"Successfully parsed {cif_file_path}")
    print(f"Structure ID: {structure.id}")

    os.makedirs(output_dir, exist_ok=True)

    for chain in structure.get_chains():
        print(f"Processing chain {chain.id}...")

        sequence = ""
        for residue in chain.get_residues():
            if residue.get_resname().strip() in ("A", "U", "G", "C"):
                sequence += residue.get_resname().strip()

        if not sequence:
            print(f"No standard RNA sequence found for chain {chain.id}")
            continue

        print(f"Sequence: {sequence}")

        (ss, energy) = RNA.fold(sequence)
        print(f"Secondary Structure: {ss} (MFE: {energy:.2f})")

        sequence_output_path = os.path.join(output_dir, f"{structure.id}_{chain.id}_sequence.txt")
        with open(sequence_output_path, "w") as f:
            f.write(sequence)
        print(f"Sequence saved to {sequence_output_path}")

        structure_output_path = os.path.join(output_dir, f"{structure.id}_{chain.id}_secondary_structure.txt")
        with open(structure_output_path, "w") as f:
            f.write(f"Sequence: {sequence}\n")
            f.write(f"Secondary Structure: {ss}\n")
            f.write(f"MFE: {energy:.2f}\n")
        print(f"Secondary structure and MFE saved to {structure_output_path}")


if __name__ == "__main__":
    example_cif_file = "code/databases/rna3db-mmcifs/train_set/component_1/1c2w_B/1c2w_B.cif"
    
    try:
        import Bio
        import RNA
    except ImportError:
        print("Required libraries (biopython, viennarna) are not installed Install them using '.venv/bin/pip install biopython viennarna'")
    else:
        process_cif_file(example_cif_file)
