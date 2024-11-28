from PIL import Image
import os
import shutil

def change_image_extension(image_path, new_extension):
    """Изменяет расширение файла изображения.

    Args:
        image_path: Путь к файлу изображения.
        new_extension: Новое расширение (например, ".jpg", ".png").  Без точки!
    Returns:
        Путь к новому файлу, или None если произошла ошибка.
    """
    try:
        base, ext = os.path.splitext(image_path)
        new_path = base + "." + new_extension
        img = Image.open(image_path)
        img.save(new_path)
        return new_path
    except FileNotFoundError:
        print(f"Ошибка: Файл {image_path} не найден.")
        return None
    except Exception as e:
        print(f"Ошибка при изменении расширения: {e}")
        return None

def move_image(image_path, destination_folder):
    """Перемещает изображение в другую папку.

    Args:
        image_path: Путь к файлу изображения.
        destination_folder: Путь к папке назначения.
    Returns:
        True если перемещение успешно, False иначе.
    """
    try:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)  # Создаем папку, если ее нет
        shutil.move(image_path, destination_folder)
        return True
    except FileNotFoundError:
        print(f"Ошибка: Файл {image_path} или папка {destination_folder} не найдены.")
        return False
    except Exception as e:
        print(f"Ошибка при перемещении файла: {e}")
        return False


# Пример использования:

image_path = "input.png"  # Замените на путь к вашему файлу
destination_folder = "output" # Замените на путь к папке назначения

# Изменение расширения PNG to JPG
jpg_path = change_image_extension(image_path, "jpg")
if jpg_path:
    print(f"Файл успешно конвертирован в JPG: {jpg_path}")
    # Перемещаем JPG файл
    if move_image(jpg_path, destination_folder):
        print(f"Файл успешно перемещен в {destination_folder}")