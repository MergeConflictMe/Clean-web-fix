import cv2
import numpy as np
import os

def generate_pixel_motion():
    # Пути для твоего компа (диск D)
    input_folder = r"D:\new proect\frames"
    output_path = r"D:\new proect\pixel_video.avi"
    
    # 1. Собираем все ракурсы
    images = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.png'))]
    all_poses = []
    
    for img_name in images:
        img = cv2.imread(os.path.join(input_folder, img_name))
        if img is None: continue
        # Нарезка коллажа (сетка 4х3)
        h, w, _ = img.shape
        rh, cw = h // 4, w // 3
        for r in range(4):
            for c in range(3):
                pose = img[r*rh:(r+1)*rh, c*cw:(c+1)*cw]
                all_poses.append(cv2.resize(pose, (720, 1280))) # Формат под TikTok

    # 2. Настройка видео
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 30.0, (720, 1280))

    # 3. Плавный морфинг между ракурсами
    steps = 20 # Количество промежуточных кадров для плавности
    print("Создаю пиксельное движение...")
    
    for i in range(len(all_poses) - 1):
        for s in range(steps):
            alpha = s / steps
            # Смешиваем текущую позу со следующей
            mixed = cv2.addWeighted(all_poses[i], 1 - alpha, all_poses[i+1], alpha, 0)
            out.write(mixed)
            
    out.release()
    print(f"Готово! Видео лежит здесь: {output_path}")

if __name__ == "__main__":
    generate_pixel_motion()
