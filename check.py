import os


def check_txt_files_exist(image_folder):
    for file_name in os.listdir(image_folder):
        if file_name.endswith('.txt'):
            continue  # Bỏ qua các file txt
        txt_file_name = os.path.splitext(file_name)[0] + '.txt'
        txt_file_path = os.path.join(image_folder, txt_file_name)
        if os.path.isfile(txt_file_path):
            pass
        else:
            print(
                f"Không tìm thấy file txt '{txt_file_name}' cho file ảnh '{file_name}'.")

def convert_jpeg_to_jpg(image_folder):
    for file_name in os.listdir(image_folder):
        if file_name.endswith('.jpeg'):
            old_file_path = os.path.join(image_folder, file_name)
            new_file_name = os.path.splitext(file_name)[0] + '.jpg'
            new_file_path = os.path.join(image_folder, new_file_name)
            os.rename(old_file_path, new_file_path)
            print(f"Đã chuyển đổi file '{file_name}' thành '{new_file_name}'.")

def count_lines_starting_with_numbers(txt_folder):
    line_count = 0

    for file_name in os.listdir(txt_folder):
        if file_name.endswith('.txt'):
            file_path = os.path.join(txt_folder, file_name)
            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith('1'):
                        line_count += 1

    return line_count

def find_files_with_line_starting(txt_folder, start_line):
    matching_files = []

    for file_name in os.listdir(txt_folder):
        if file_name.endswith('.txt'):
            file_path = os.path.join(txt_folder, file_name)
            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith(start_line):
                        matching_files.append(file_name)
                        break
    return matching_files

# Đường dẫn đến thư mục chứa file ảnh
image_folder = r'D:\other1\other\images'
txt_folder = '/home/n7567/yolov8/other1/other/labels/val'
original_folder =''

# Gọi hàm kiểm tra
# check_txt_files_exist(image_folder)

# Gọi hàm chuyển đổi
#convert_jpeg_to_jpg(image_folder)

# Gọi hàm đếm số lượng dòng bắt đầu bằng 15
line_count = count_lines_starting_with_numbers(txt_folder)

# In kết quả
print(f"Số lượng dòng bắt đầu bằng 1: {line_count}")

# Tìm các file txt chứa dòng bắt đầu bằng '18'
# matching_files = find_files_with_line_starting(txt_folder, '18')

# if matching_files:
#     print("Các file txt chứa dòng bắt đầu bằng '18':")
#     for file_name in matching_files:
#         print(file_name)