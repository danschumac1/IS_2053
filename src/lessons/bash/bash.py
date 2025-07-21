# myscript.py
import argparse

def main():
    parser = argparse.ArgumentParser(description='Demo Script')
    parser.add_argument('--input_path', required=True)
    parser.add_argument('--output_path', required=True)
    parser.add_argument('--verbose', type=int, default=0)

    args = parser.parse_args()

    if args.verbose:
        print(f"Processing {args.input_path} -> {args.output_path}")

    with open(args.input_path, 'r') as infile, open(args.output_path, 'w') as outfile:
        data = infile.read()
        outfile.write(data.upper())

if __name__ == '__main__':
    main()
