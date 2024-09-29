'''JPG转PNG'''
# import os

# from PIL import Image
#
# def convert_jpg_to_png(input_folder, output_folder):
#     # Create the output folder if it doesn't exist
#     os.makedirs(output_folder, exist_ok=True)
#
#     # Get a list of all files in the input folder
#     file_list = os.listdir(input_folder)
#
#     # Process each file in the input folder
#     for filename in file_list:
#         # Check if the file is a JPG image
#         if filename.endswith('.jpg') or filename.endswith('.jpeg'):
#             # Open the image file
#             image = Image.open(os.path.join(input_folder, filename))
#
#             # Convert the image to PNG format
#             png_filename = os.path.splitext(filename)[0] + '.png'
#             png_filepath = os.path.join(output_folder, png_filename)
#             image.save(png_filepath, 'PNG')
#
#             # Close the image file
#             image.close()
#
#             print(f"Converted {filename} to {png_filename}")
#
# # Specify the input and output folders
# input_folder = 'out1'
# output_folder = 'png'
#
# # Call the function to convert JPG images to PNG
# convert_jpg_to_png(input_folder, output_folder)

'''BMP图片批量转JPG'''
# from PIL import Image
# import os
#
# # 输入文件夹路径和输出文件夹路径
# input_folder = r"C:\Users\86199\Desktop\VOC2007\JPEGImages"
# output_folder = r"C:\Users\86199\Desktop\VOC2007\JPEGImages"
#
# # 确保输出文件夹存在
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#
# # 遍历输入文件夹中的所有文件
# for filename in os.listdir(input_folder):
#     if filename.endswith(".bmp"):
#         # 拼接输入和输出文件的完整路径
#         input_path = os.path.join(input_folder, filename)
#         output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
#
#         # 打开BMP图片并保存为JPEG格式
#         image = Image.open(input_path)
#         image.save(output_path, "JPEG")
#         print(f"Converted {filename} to {os.path.basename(output_path)}")


'''
JPG转BMP，无损，并删除原有的jpg图片
'''

# from PIL import Image
# import os
#
# def convert_images(source_dir, target_dir):
#     # Create the target directory if it doesn't exist
#     if not os.path.exists(target_dir):
#         os.makedirs(target_dir)
#
#     # Get a list of all JPG files in the source directory
#     jpg_files = [f for f in os.listdir(source_dir) if f.endswith('.jpg')]
#
#     # Convert each JPG file to BMP format and save it in the target directory
#     for jpg_file in jpg_files:
#         jpg_path = os.path.join(source_dir, jpg_file)
#         bmp_file = os.path.splitext(jpg_file)[0] + '.bmp'
#         bmp_path = os.path.join(target_dir, bmp_file)
#
#         # Open the JPG image and convert it to BMP format
#         image = Image.open(jpg_path)
#         image.save(bmp_path, 'BMP')
#
#         # Delete the original JPG file
#         # os.remove(jpg_path)
#
#         print(f"Converted {jpg_file} to {bmp_file}")
#
# # Specify the source directory containing JPG files
# source_directory = r'D:\Paper_latex\画图\数据增强可视化'
#
# # Specify the target directory to save the BMP files
# target_directory = r'D:\Paper_latex\画图\数据增强可视化'
#
# # Call the function to convert and delete the JPG files
# convert_images(source_directory, target_directory)

'''bmp转png'''

# from PIL import Image
# import os
#
# # 输入文件夹路径和输出文件夹路径
# input_folder = r"D:\Paper_latex\LaTeX\part_data"
# output_folder = r"D:\Paper_latex\LaTeX\part_data"
#
# # 遍历输入文件夹中的所有文件
# for filename in os.listdir(input_folder):
#     if filename.endswith(".bmp"):
#         # 拼接文件的完整路径
#         input_path = os.path.join(input_folder, filename)
#
#         # 构建输出文件的完整路径，将文件名的后缀改为.png
#         output_filename = os.path.splitext(filename)[0] + ".png"
#         output_path = os.path.join(output_folder, output_filename)
#
#         # 打开BMP图片并转换为PNG图片
#         img = Image.open(input_path)
#         img.save(output_path, "PNG")

'''CR2转jpg'''
# from PIL import Image
# import os

# 指定CR2文件夹和输出JPEG文件夹
# input_folder = r'E:\打印\冲洗照片'
# output_folder = r'E:\打印\JPG'
#
# # 确保输出文件夹存在
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#
# # 遍历CR2文件夹中的所有文件
# for filename in os.listdir(input_folder):
#     if filename.endswith('.CR2'):
#         cr2_path = os.path.join(input_folder, filename)
#         output_filename = os.path.splitext(filename)[0] + '.jpg'
#         jpg_path = os.path.join(output_folder, output_filename)
#
#         # 打开CR2文件并保存为JPEG格式
#         img = Image.open(cr2_path)
#         img.save(jpg_path, 'JPEG')
#
# print('转换完成')



