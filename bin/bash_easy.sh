#!/bin/bash
# USAGE:
# chmod +x ./bin/bash_easy.sh
# ./bin/bash_easy

input_file="./data/bash/lower_case.txt"
output_file="./data/bash/upper_case.txt"
verbose=1

echo "Running Python script with arguments..."
python ./src/lessons/CLA/bash.py \
    --input_path "$input_file" \
    --output_path "$output_file" \
    --verbose "$verbose"
