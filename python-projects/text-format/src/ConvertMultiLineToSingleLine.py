def format_text_to_single_line(input_file_path, outpot_file_path):

    with open(input_file_path, 'r') as input_file:
        text_content = input_file.read()

    # Split the text into lines
    lines = text_content.splitlines()

    # Join the lines into a single string
    formatted_text = ''.join(line.strip() for line in lines)

    with open(outpot_file_path, 'w') as output_file:
        output_file.write(formatted_text)

# Example text content with multiple lines

input_file_path = "/Users/e177305/my-projects/PkCodeVault/python-projects/text-format/resources/input/sample-input.xml"
outpot_file_path = "/Users/e177305/my-projects/PkCodeVault/python-projects/text-format/resources/output/result.txt"

# Format text into single line
format_text_to_single_line(input_file_path, outpot_file_path)

#print(formatted_text)
