from PIL import Image
import os
import shutil

def change_image_extension(input_path, output_path):
    img = Image.open(input_path)
    img.save(output_path)

def move_image(source, destination):
    shutil.move(source, destination)

# Пример использования
input_file = 'image.png'
output_file = 'image.jpg'
change_image_extension(input_file, output_file)

source_path = output_file  # Перемещаем только что созданный файл
destination_path = 'new_folder/image.jpg'  # Папка назначения
os.makedirs(os.path.dirname(destination_path), exist_ok=True)  # Создаем папку, если она не существует
move_image(source_path, destination_path)
