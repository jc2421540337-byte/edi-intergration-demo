import json
import requests


def parse_edi(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    segments = content.replace('\n', '').replace('\r', '').split('~')
    
    data = {}
    
    for seg in segments:
        parts = seg.split('*')
        tag = parts[0]
        
        if tag == "BEG":
            data["order_number"] = parts[3]
            data["date"] = parts[5]

        elif tag == "N1":
            data["store"] = parts[2]

        elif tag == "PO1":
            data["item"] = {
                "quantity": parts[2],
                "price": parts[4],
                "sku": parts[7]
            }

    return data


if __name__ == "__main__":
    parsed = parse_edi("../data/sample.edi")

    with open("../output/parsed.json", "w") as f:
        json.dump(parsed, f, indent=2)

    print("Parsed EDI:", parsed)

    # Connet parser + API
    response = requests.post(
        "http://127.0.0.1:5000/process-order",
        json=parsed
    )

    print("API Response:", response.json())