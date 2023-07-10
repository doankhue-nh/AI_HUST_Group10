import os
import random
import shutil
import glob

# Đường dẫn đến thư mục chứa ảnh và label
data_folder = r'D:\Hard_hat\all'

# Đường dẫn đến thư mục train, val và test
train_folder = os.path.join(data_folder, 'train')
val_folder = os.path.join(data_folder, 'val')
test_folder = os.path.join(data_folder, 'test')

# Tạo thư mục train, val và test nếu chưa tồn tại
os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Lấy danh sách các file ảnh trong thư mục
image_files = glob.glob(f"{data_folder}/*.jpg")

# Sắp xếp các file theo thứ tự ngẫu nhiên
random.shuffle(image_files)

# Tính toán số lượng file trong từng phần (train, val, test)
num_files = len(image_files)
num_train = int(0.7 * num_files)
num_val = int(0.2 * num_files)
num_test = num_files - num_train - num_val

# Chia các file ảnh vào các thư mục train, val và test
train_files = image_files[:num_train]
val_files = image_files[num_train:num_train+num_val]
test_files = image_files[num_train+num_val:]

# Di chuyển các file ảnh vào các thư mục tương ứng
for file in train_files:
    shutil.move(file, train_folder)

for file in val_files:
    shutil.move(file, val_folder)

for file in test_files:
    shutil.move(file, test_folder)

# Chia các file label tương ứng vào các thư mục train, val và test
for file in train_files:
    txt_file = os.path.splitext(file)[0] + '.txt'
    shutil.move(txt_file, train_folder)

for file in val_files:
    txt_file = os.path.splitext(file)[0] + '.txt'
    shutil.move(txt_file, val_folder)

for file in test_files:
    txt_file = os.path.splitext(file)[0] + '.txt'
    shutil.move(txt_file, test_folder)
