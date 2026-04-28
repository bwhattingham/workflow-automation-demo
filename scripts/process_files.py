import os
import json

def process_files(directory):
    summary = {
        "total_files": 0,
        "file_types": {}
    }

    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)

        if os.path.isfile(path):
            summary["total_files"] += 1

            ext = filename.split(".")[-1]
            summary["file_types"][ext] = summary["file_types"].get(ext, 0) + 1

    return summary

if __name__ == "__main__":
    directory = "input"
    os.makedirs(directory, exist_ok=True)

    result = process_files(directory)

    print(json.dumps(result, indent=2))
