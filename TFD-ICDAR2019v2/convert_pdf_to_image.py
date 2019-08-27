from pdf2image import convert_from_path
import sys
import os

"""
    This module converts directory containing PDF files
    to images with 600 DPI and save them in given output directory
    Usage: python convert_pdf_to_image.py <PDF_files_dir> <output_img_dir>
"""

def create_images_from_pdfs(pdf_dir, output_dir):
    '''
    Render each PDF file as image in 600 DPI
    :param pdf_dir: Directory with PDF files
    :param output_dir: Output directory for storing image files for each PDF file
    :return: None
    '''
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    pdf_files = []
    for _, _, fileList in os.walk(pdf_dir):
        pdf_files.extend(fileList)
        break
    for pdf_file in pdf_files:
        pdf_name = pdf_file.split(".pdf")[0]
        output_path = os.path.join(output_dir, pdf_name)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        pages = convert_from_path(os.path.join(pdf_dir, pdf_file), 600)
        for i in range(len(pages)):
            pages[i].save(os.path.join(output_path, str(i + 1) + ".png"), 'PNG')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 convert_pdf_to_image.py <PDF_files_dir> <output_dir>")
        #raise ValueError("Incorrect usage")
        exit(0)
    pdf_dir = sys.argv[1]
    print (pdf_dir)
    output_dir = sys.argv[2]
    print(output_dir)
    create_images_from_pdfs(pdf_dir, output_dir)
