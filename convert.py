from textwrap import TextWrapper


def format_text(input_text, width=70, initial_indent="", subsequent_indent=" ", justify=True):
    """
    Formats text based on specified width, initial and subsequent indentations, and justification.

    Parameters:
    - input_text (str): The text to format.
    - width (int): The width of each line.
    - initial_indent (str): Indentation for the first line of each paragraph.
    - subsequent_indent (str): Indentation for subsequent lines within a paragraph.
    - justify (bool): If True, lines are justified to the specified width.

    Returns:
    - str: The formatted text.
    """
    wrapper = TextWrapper(width=width, expand_tabs=False, replace_whitespace=False)
    wrapper.initial_indent = initial_indent
    wrapper.subsequent_indent = subsequent_indent

    formatted_paragraphs = []
    paragraphs = input_text.split("\n\n")  # Split text into paragraphs by double newlines

    for paragraph in paragraphs:
        lines = wrapper.wrap(paragraph)
        if justify:
            justified_lines = [line.ljust(width) for line in lines]
        else:
            justified_lines = lines
        formatted_paragraphs.append("\n".join(justified_lines))

    return "\n\n".join(formatted_paragraphs)


def format_file(input_file_path, output_file_path, width=70, initial_indent="", subsequent_indent=" ", justify=True):
    """
    Reads a file, applies formatting, and writes the output to a new file.

    Parameters:
    - input_file_path (str): Path to the input text file.
    - output_file_path (str): Path to save the formatted text file.
    - width (int): The width of each line in characters.
    - initial_indent (str): Indentation for the first line of each paragraph.
    - subsequent_indent (str): Indentation for subsequent lines within a paragraph.
    - justify (bool): If True, justifies text lines to the specified width.
    """
    with open(input_file_path, 'r', encoding='utf-8') as file:
        original_text = file.read()

    formatted_text = format_text(
        input_text=original_text,
        width=width,
        initial_indent=initial_indent,
        subsequent_indent=subsequent_indent,
        justify=justify
    )

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_text)

    print(f"Formatted text saved to {output_file_path}")



format_file(
    input_file_path='texts/Nineteen Eighty-Four 1984zh.txt',
    output_file_path='texts/Nineteen Eighty-Four 1984zh_formatted.txt',
    width=70,
    initial_indent="",
    subsequent_indent="",
    justify=True
)
