import argparse
import os
import json
import jsonschema
from jsonschema import validate

def parse_arguments():
    parser = argparse.ArgumentParser(description='Program do konwersji danych.')
    parser.add_argument('input_file', type=str, help='Ścieżka do pliku wejściowego')
    parser.add_argument('output_file', type=str, help='Ścieżka do pliku wyjściowego')
    
    args = parser.parse_args()
    
    #sprawdzenie czy pliki mają odpowiednie rozszerzenia
    input_ext = os.path.splitext(args.input_file)[1]
    output_ext = os.path.splitext(args.output_file)[1]
    valid_extensions = ['.json', '.xml', '.yml', '.yaml']
    
    if input_ext not in valid_extensions:
        raise ValueError(f"Niewłaściwe rozszerzenie pliku wejściowego: {input_ext}. Dozwolone rozszerzenia to: {valid_extensions}")
    
    if output_ext not in valid_extensions:
        raise ValueError(f"Niewłaściwe rozszerzenie pliku wyjściowego: {output_ext}. Dozwolone rozszerzenia to: {valid_extensions}")
    
    return args

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def validate_json(data, schema):
    try:
        validate(instance=data, schema=schema)
        print("JSON jest poprawny.")
    except jsonschema.exceptions.ValidationError as err:
        print("Błąd walidacji JSON:", err)
        raise

def main():
    args = parse_arguments()
    print(f"Plik wejściowy: {args.input_file}")
    print(f"Plik wyjściowy: {args.output_file}")

    if args.input_file.endswith('.json'):
        data = load_json(args.input_file)
        print("Dane z pliku JSON:", data)
        
        #przykładowy schemat JSON
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "number"},
            },
            "required": ["name", "age"]
        }
        validate_json(data, schema)

if __name__ == "__main__":
    main()
