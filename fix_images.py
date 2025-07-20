import os
import re

def replace_markdown_images(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Tìm và thay thế tất cả các đường dẫn hình ảnh
        pattern = r'!\[(.*?)\]\((\/images\/.*?)\)'
        replacement = r'{{< img src="\2" alt="\1" >}}'
        new_content = re.sub(pattern, replacement, content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated: {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                replace_markdown_images(file_path)

# Thư mục gốc của dự án
project_root = r'd:\000060-GuardDuty\content'
process_directory(project_root)
print("Completed!")