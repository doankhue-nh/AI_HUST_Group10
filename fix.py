import os
folder_path = "./Dataset/labels/val"  

list_file = os.listdir(folder_path)

for filename in list_file:
    file_path = os.path.join(folder_path, filename)

    with open(file_path, "r") as file:
        lines = file.readlines()

    # Xóa các hàng có phần tử đầu tiên là 2
    lines = [line for line in lines if not line.strip().startswith("2")]

    # Ghi lại nội dung đã chỉnh sửa vào file
    with open(file_path, "w") as file:
        file.writelines(lines)