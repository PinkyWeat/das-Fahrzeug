import os
import shutil
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

base_dir = 'cam_dev'
train_dir = 'train'
validation_dir = 'validation'

def organize_images(dataset_folder, tagging_file):
    tagging_file_path = os.path.join(base_dir, dataset_folder, tagging_file)
    
    # Verificar si el archivo de etiquetas existe
    if not os.path.exists(tagging_file_path):
        logging.critical(f"Tagging file not found: {tagging_file_path}")
        return
    
    # Leer el archivo de etiquetas
    with open(tagging_file_path, 'r') as f:
        for line in f:
            image_name, label = line.strip().split()
            image_name = image_name.strip(':')  # Eliminar cualquier ':' al final del nombre

            # Construir la ruta de origen de la imagen
            src = os.path.join(base_dir, dataset_folder, image_name)
            
            # Verificar si el archivo de imagen existe
            if not os.path.exists(src):
                logging.error(f"File not found: {src}")
                continue

            # Determinar las rutas de destino según la etiqueta
            if label == 'avanzar':
                dst_train = os.path.join(train_dir, 'avanzar', image_name)
                dst_validation = os.path.join(validation_dir, 'avanzar', image_name)
            elif label == 'retroceder':
                dst_train = os.path.join(train_dir, 'retroceder', image_name)
                dst_validation = os.path.join(validation_dir, 'retroceder', image_name)
            elif label == 'parar':
                dst_train = os.path.join(train_dir, 'parar', image_name)
                dst_validation = os.path.join(validation_dir, 'parar', image_name)
            else:
                logging.warning(f"Unknown label '{label}' for image: {image_name}")
                continue

            # Intentar mover el archivo
            try:
                if int(image_name.split('_')[1].split('.')[0]) % 10 == 0:
                    shutil.move(src, dst_validation)
                    logging.info(f'Moved {image_name} to validation: {dst_validation}')
                else:
                    shutil.move(src, dst_train)
                    logging.info(f'Moved {image_name} to train: {dst_train}')
            except ValueError:
                logging.warning(f"Skipping invalid file name: {image_name}")
            except IndexError:
                logging.warning(f"Skipping improperly formatted file: {image_name}")
            except Exception as e:
                logging.error(f"Error moving {image_name}: {e}")

# Llamadas a la función organize_images para cada dataset
organize_images('dataset_428', 'tagging.txt')
organize_images('dataset_433', 'tagging.txt')
organize_images('dataset_452', 'tagging.txt')
organize_images('dataset_503', 'tagging.txt')
organize_images('dataset_dev', 'tagging.txt')
organize_images('dataset_latetime', 'tagging.txt')
organize_images('dataset_prettygood', 'tagging.txt')
