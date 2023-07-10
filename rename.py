import os
import glob

# # Đường dẫn đến thư mục chứa các file ảnh và file txt cùng tên
# folder_path = r'D:\Hard_hat\all'

# # Lấy danh sách các file .txt trong thư mục
# txt_files = glob.glob(f"{folder_path}/*.txt")

# # Sắp xếp các file theo thứ tự tên tăng dần (nếu cần)
# txt_files.sort()

# # Lặp qua từng file .txt và đổi tên file ảnh và file txt tương ứng
# for index, txt_file in enumerate(txt_files, start=1):
#     # Đổi tên file ảnh
#     image_file = os.path.splitext(txt_file)[0] + '.jpg'
#     new_image_name = f"Hard_hat_{index}.jpg"
#     os.rename(image_file, os.path.join(folder_path, new_image_name))

#     # Đổi tên file txt
#     new_txt_name = f"Hard_hat_{index}.txt"
#     os.rename(txt_file, os.path.join(folder_path, new_txt_name))

#######################################################################

# Xử lý testset
import os

def rename_files(folder_path):
    # Kiểm tra xem đường dẫn của thư mục tồn tại hay không
    if not os.path.isdir(folder_path):
        print("Thư mục không tồn tại.")
        return
    
    # Lặp qua tất cả các tệp tin trong thư mục
    for index, filename in enumerate(os.listdir(folder_path)):
        # Lấy phần mở rộng của tệp tin
        extension = os.path.splitext(filename)[1]
        
        # Tạo tên mới theo định dạng "1_1_số thứ tự"
        new_filename = f"3_2_{index + 1}{extension}"
        
        # Tạo đường dẫn đầy đủ cho tệp tin cũ và mới
        old_filepath = os.path.join(folder_path, filename)
        new_filepath = os.path.join(folder_path, new_filename)
        
        # Đổi tên tệp tin
        os.rename(old_filepath, new_filepath)
        
        print(f"Đã đổi tên {filename} thành {new_filename}")

# Thay đổi đường dẫn thư mục của bạn thành đường dẫn thư mục thực tế
folder_path = "/home/n7567/yolov8/TESTSET_FINAL/3_2"
rename_files(folder_path)
 