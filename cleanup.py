from pathlib import Path
import re

def cleanup():
    names_dir = Path('names')
    all_content = []
    
    # Recursively find all txt files in names directory and subdirectories
    for file in names_dir.rglob('*.txt'):
        content = file.read_text().splitlines()
        content = [line.lower() for line in content if line.strip()]
        file.write_text('\n'.join(content))
        all_content.extend(content)
    
    combined = sorted(set(all_content))
    combined = [name for name in combined if re.match(r"^[A-Za-z0-9_]{3,16}$", name)]
    names_dir.joinpath('all.txt').write_text('\n'.join(combined))

if __name__ == "__main__":
    cleanup()
    print("Done!")
