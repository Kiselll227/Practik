from PIL import Image
import os
import shutil

def change_image_extension(input_path, output_path):
    """Изменяет расширение изображения."""
    img = Image.open(input_path)
    img.save(output_path)
    print(f"Изображение сохранено как: {output_path}")

def move_image(source, destination):
    """Перемещает изображение в указанную папку."""
    shutil.move(source, destination)
    print(f"Изображение перемещено в: {destination}")

def main():
    # Запрос пути к изображению у пользователя
    input_path = input("Введите путь к изображению (например, image.png): ")
    
    # Проверка существования файла
    if not os.path.isfile(input_path):
        print("Ошибка: Указанный файл не существует.")
        return

    # Запрос типа конвертации у пользователя
    conversion_type = input("Введите тип конвертации (JPG или PNG): ").strip().upper()

    if conversion_type not in ['JPG', 'PNG']:
        print("Ошибка: Неверный тип конвертации. Пожалуйста, введите 'JPG' или 'PNG'.")
        return

    # Формирование нового пути для сохранения изображения
    base_name = os.path.basename(input_path)
    name, _ = os.path.splitext(base_name)
    new_extension = 'jpg' if conversion_type == 'JPG' else 'png'
    output_path = os.path.join(os.path.dirname(input_path), f"{name}.{new_extension}")

    # Конвертация изображения
    change_image_extension(input_path, output_path)

    # Перемещение изображения в новую папку
    destination_folder = input("Введите путь к папке назначения (например, new_folder/): ")
    
    # Создание папки, если она не существует
    os.makedirs(destination_folder, exist_ok=True)

    destination_path = os.path.join(destination_folder, f"{name}.{new_extension}")
    
    move_image(output_path, destination_path)

if __name__ == "__main__":
    main()
