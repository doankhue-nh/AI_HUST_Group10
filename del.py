import glob

def remove_lines_starting_with_2(lines):
    # Xóa các dòng có phần tử đầu tiên là '2'
    modified_lines = [line for line in lines if not line.startswith('2')]
    return modified_lines

# Đường dẫn đến thư mục chứa các file văn bản (.txt)
folder_path = r'D:\Hard_hat\all'

# Lấy danh sách các file .txt trong thư mục
file_paths = glob.glob(f"{folder_path}/*.txt")

# Đọc và xóa các dòng có phần tử đầu tiên là '2' trong từng file
for file_path in file_paths:
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Đọc tất cả các dòng

    # Thực hiện xóa các dòng có phần tử đầu tiên là '2'
    modified_lines = remove_lines_starting_with_2(lines)

    # Ghi lại các dòng đã xóa vào cùng file
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)