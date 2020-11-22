import cv2, os, logging


logging.basicConfig(level=logging.INFO, format='%(message)s', filename='MainLog.log', filemode="w")


def pick_resize(new_size, path, new_path):
    logging.info(f"Обработка датасета '{path}'")
    logging.info("---------------------------------------")
    files = os.listdir(path)
    errors = 0
    for img in files:
        try:
            image = cv2.imread(path+img)
        except:
            logging.error("ОШИБКА в открытии фото")
            errors += 1
            continue
        try:
            resized_img = cv2.resize(image, new_size)
        except:
            logging.error("ОШИБКА в изменении размера фото.")
            errors += 1
            continue
        try:
            cv2.imwrite(new_path+img, resized_img)
        except:
            logging.error("ОШИБКА в сохранении фото.")
            errors += 1
            continue
    logging.info(f"\nОбработано {len(files)} файлов:")
    logging.info(f"{errors} битых файлов.")
    logging.info("---------------------------------------\n\n")