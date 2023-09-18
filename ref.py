import re
import sys
import os

def find_file_references(script_content, script_type):
    referenced_files = []
    
    if script_type == 'sh':  # Shell Script
        referenced_files = re.findall(r'(?:\b(?:cp|mv|rm|touch|cat|grep|less|more|nano|vi|vim) )([^\s]+)', script_content)
        
    elif script_type == 'py':  # Python Script
        referenced_files = re.findall(r'open\([\'"]([^\'"]+)[\'"]', script_content)
        
    elif script_type == 'js':  # JavaScript
        referenced_files = re.findall(r'fs\.(?:readFile|writeFile|appendFile)\([\'"]([^\'"]+)[\'"]', script_content)
        
    elif script_type == 'rb':  # Ruby Script
        referenced_files = re.findall(r'File\.open\([\'"]([^\'"]+)[\'"]', script_content)
        
    elif script_type == 'pl':  # Perl Script
        referenced_files = re.findall(r'open\([^,]+, [\'"]?([^\'"\s]+)[\'"]?', script_content)
    
    return referenced_files

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ref.py <script_file>")
        sys.exit(1)

    script_file = sys.argv[1]
    script_type = os.path.splitext(script_file)[1][1:]  # Get the file extension without the dot

    with open(script_file, 'r', errors='ignore') as f:
        script_content = f.read()

    referenced_files = find_file_references(script_content, script_type)
    print(referenced_files)
