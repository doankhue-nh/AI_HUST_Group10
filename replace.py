import glob

def replace_values(line):
    # Kiểm tra giá trị đầu tiên trước dấu cách và thay đổi tương ứng
    if line.startswith('15'):
        line = line.replace('15', '2', 1)  # Thay đổi chỉ một lần
    elif line.startswith('16'):
        line = line.replace('16', '1', 1)
    elif line.startswith('17'):
        line = line.replace('17', '0', 1)
    return line

# Đường dẫn đến thư mục chứa các file văn bản (.txt)
folder_path =  r'D:\other1\other\label'

# Lấy danh sách các file .txt trong thư mục
file_paths = glob.glob(f"{folder_path}/*.txt")

# Đọc và thay đổi giá trị trong từng file
for file_path in file_paths:
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Đọc tất cả các dòng

    # Thực hiện thay đổi trên từng dòng
    modified_lines = [replace_values(line) for line in lines]

    # Ghi lại các dòng đã thay đổi vào cùng file
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
