import json
from datetime import datetime

def transform_tech_radar(input_file, output_file):
    with open(input_file, 'r') as infile:
        data = json.load(infile)

    # Map quadrant numbers to names
    quadrant_map = {
        0: "frameworks",
        1: "infrastructure",
        2: "languages",
        3: "process"
    }

    # Map ring numbers to ids
    ring_map = {
        0: "adopt",
        1: "trial",
        2: "assess",
        3: "hold"
    }

    # Transform entries
    entries = []
    for entry in data['entries']:
        transformed_entry = {
            "timeline": [
                {
                    "moved": entry["moved"],
                    "ringId": ring_map.get(entry["ring"], "unknown"),
                    "date": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
                    "description": f"Auto-generated entry for {entry['label']}"
                }
            ],
            "key": entry["label"].replace(" ", "-").lower(),
            "id": entry["label"].replace(" ", "-").lower(),
            "title": entry["label"],
            "quadrant": quadrant_map.get(entry["quadrant"], "unknown"),
            "description": f"This is a placeholder description for {entry['label']}.",
        }

        # Add example links (optional)
        transformed_entry["links"] = [
            {"url": f"https://example.com/{entry['label'].lower()}", "title": "Learn more"}
        ]

        entries.append(transformed_entry)

    # Build final output structure
    output_data = {
        "entries": entries,
        "quadrants": [
            {"id": "frameworks", "name": "Frameworks"},
            {"id": "infrastructure", "name": "Infrastructure"},
            {"id": "languages", "name": "Languages"},
            {"id": "process", "name": "Process"}
        ],
        "rings": [
            {"id": "adopt", "name": "ADOPT", "color": "#5BA300", "description": "Recommended technologies."},
            {"id": "trial", "name": "TRIAL", "color": "#009EB0", "description": "Promising technologies to evaluate."},
            {"id": "assess", "name": "ASSESS", "color": "#C7BA00", "description": "Technologies to watch and evaluate."},
            {"id": "hold", "name": "HOLD", "color": "#E09B96", "description": "Not recommended for use."}
        ]
    }

    # Write output to file
    with open(output_file, 'w') as outfile:
        json.dump(output_data, outfile, indent=2)

if __name__ == "__main__":
    # Input and output paths
    input_path = "tech-radar.json"  # Input file
    output_path = "generated/tech-radar-backstage.json"  # Output file

    # Ensure the output directory exists
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Transform the file
    transform_tech_radar(input_path, output_path)
    print(f"Transformed tech radar saved to {output_path}")
