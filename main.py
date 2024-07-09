import argparse
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description='Program do konwersji danych.')
    parser.add_argument('input_file', type=str, help='Ścieżka do pliku wejściowego')
    parser.add_argument('output_file', type=str, help='Ścieżka do pliku wyjściowego')
    
    args = parser.parse_args()
    
    #sprawdzanie rozszerzeń
    input_ext = os.path.splitext(args.input_file)[1]
    output_ext = os.path.splitext(args.output_file)[1]
    valid_extensions = ['.json', '.xml', '.yml', '.yaml']
    
    if input_ext not in valid_extensions:
        raise ValueError(f"Niewłaściwe rozszerzenie pliku wejściowego: {input_ext}. Dozwolone rozszerzenia to: {valid_extensions}")
    
    if output_ext not in valid_extensions:
        raise ValueError(f"Niewłaściwe rozszerzenie pliku wyjściowego: {output_ext}. Dozwolone rozszerzenia to: {valid_extensions}")
    
    return args

def main():
    args = parse_arguments()
    print(f"Plik wejściowy: {args.input_file}")
    print(f"Plik wyjściowy: {args.output_file}")

if __name__ == "__main__":
    main()
