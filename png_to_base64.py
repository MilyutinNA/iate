import base64

#path - путь где хранится картинка и где будет записан файл .txt
path = 'C:\\Users\\MilyutinNA\\Desktop\\' #Рабочий стол

#Функция конвертации фото. В качестве аргумента задается имя файла
def png_dict(*png_list):
    for png_name in png_list:
        with open(path + png_name, "rb") as img_file:
            encoded_string= base64.b64encode(img_file.read())
            data = encoded_string.decode('utf-8')
        with open(f'{path}{png_name}.txt', 'w') as f_base64:
            f_base64.write(data)

png_dict('SBP.png')