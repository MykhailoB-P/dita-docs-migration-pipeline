import os
import sys
import xml.etree.ElementTree as ET

def validate_all_xml(docs_directory):
    print(f"=== Starting XML structural scan in: {docs_directory} ===")
    errors_found = False

    # scan the folders
    for root, dirs, files in os.walk(docs_directory):
        for file in files:
            if file.endswith('.xml'):
                full_path = os.path.join(root, file)
                try:
                    # internal Python library for parsing
                    ET.parse(full_path)
                    print(f"[SUCCESS] {file} is structurally valid.")
                except ET.ParseError as error:
                    # Error
                    print(f"[FAILED] {file} has structural errors! Detail: {error}")
                    errors_found = True

    if errors_found:
        print("=== Validation completed: ERRORS DETECTED ===")
        sys.exit(1)
    else:
        print("=== Validation completed: ALL FILES ARE HEALTHY ===")
        sys.exit(0)

if __name__ == "__main__":
    validate_all_xml("docs")
