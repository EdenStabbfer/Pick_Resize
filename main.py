import cv2, os, logging


logging.basicConfig(level=logging.INFO, format='%(message)s', filename='MainLog.log', filemode="w")


def pick_resize(new_size, path, new_path):
    folders = os.listdir(path)
    for f in folders:
        try:
            os.makedirs(new_path+"/"+f)
        except Exception:
            print("Папка уже существует.")
    errors = 0
    logging.info(f"Обработка датасета '{path}'\n")
    
    for folder in folders:
        images = os.listdir(path+"/"+folder)
        cnt = 0
        logging.info("---------------------------------------")
        for img in images:
            cnt += 1
            try:
                pick = cv2.imread(path+"/"+folder+"/"+img)
            except:
                logging.error("ОШИБКА в открытии фото:" + folder +"/"+  img)
                errors += 1
                continue
            try:
                resized_img = cv2.resize(pick, new_size)
            except:
                logging.error("ОШИБКА в изменении размера фото: " + folder +"/"+ img)
                errors += 1
                continue
            try:
                cv2.imwrite(new_path+"/"+folder+"/"+img, resized_img)
            except:
                logging.error("ОШИБКА в сохранении фото: " + folder +"/"+  img)
                errors += 1
                continue
        logging.info(f"\nОбработано {cnt} файлов:")
        logging.info(f"{errors} битых файлов.")
        logging.info("---------------------------------------\n\n")
    
if __name__=="__main__":
    pick_resize((32, 32), "data", "new_data")