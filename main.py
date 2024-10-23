import argparse
import easyocr


parser = argparse.ArgumentParser(
    description="EasyOCR image reader. It gets text from image "
			    "to text file."
)
parser.add_argument("input_image", type=str, help="Path to image to read")
parser.add_argument('output_file', type=str, help='Path to result file')
parser.add_argument('--use-gpu', action=argparse.BooleanOptionalAction, default=True, help='Option, would it use GPU or not. Default is "--use-gpu"')
arguments = parser.parse_args()


def main():
	reader = easyocr.Reader(['ru',], gpu=arguments.use_gpu)
	content = reader.readtext(arguments.input_image, detail=0, paragraph=True)
	with open(arguments.output_file, 'w') as res:
		res.write(''.join(content))
	print(f'Содержимое изображения {arguments.input_image} '
		  f'записано в текстовый файл {arguments.output_file}.')

	
if __name__ == "__main__":
	main()

