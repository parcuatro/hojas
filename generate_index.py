import csv
import json
import os

def main():
    csv_file = 'mapeo.csv'
    json_file = 'indice.json'
    
    data = []
    
    with open(csv_file, mode='r', encoding='utf-8-sig') as f:
        # The CSV is separated by semicolons and has no headers
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if not row or len(row) < 2:
                continue
            codigo = row[0].strip()
            nombre = row[1].strip()
            
            # Create the dictionary
            item = {
                "codigo": codigo,
                "nombre": nombre,
                "archivo": f"pdfs/{nombre}.pdf"
            }
            data.append(item)
            
    with open(json_file, mode='w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print(f"Successfully generated {json_file} with {len(data)} entries.")

if __name__ == '__main__':
    main()
