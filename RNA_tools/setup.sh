#!/bin/bash

set -e 
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed"
    exit 1
fi

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

source .venv/bin/activate

pip install --upgrade pip

pip install viennarna biopython matplotlib

pip install numpy scipy pandas

python3 -c "
import RNA
import Bio
import matplotlib
print('✓ ViennaRNA imported successfully')
print('✓ Biopython imported successfully')
print('✓ Matplotlib imported successfully')
"

echo "To test MFE filtering, run:"
echo " source .venv/bin/activate && python test_mfe_filtering.py"