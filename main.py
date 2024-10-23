import argparse
import pytesseract
import cv2

parser = argparse.ArgumentParser(
    description="EasyOCR image reader. It gets text from image "
			    "to text file."
)
parser.add_argument("input_image", type=str, help="Path to image to read")
parser.add_argument('output_file', type=str, help='Path to result file')
arguments = parser.parse_args()


def main():
    image = cv2.imread(arguments.input_image)
    string = pytesseract.image_to_string(image)
    with open(arguments.output_file, 'w') as res:
        res.write(string)

    print(f'Содержимое изображения {arguments.input_image} '
          f'записано в текстовый файл {arguments.output_file}.')

	
if __name__ == "__main__":
	main()

