# Text Compression Program

This Python program compresses text files using various lossless compression algorithms, including Zlib, LZMA, Brotli, Gzip, Snappy, and LZ4. It supports directory input, progress bars for each algorithm, and logs the results (compression time, input/output file sizes, and compression ratio). The program can be run from the command line or as an executable and interactively asks whether to save the results.

## Features

- **Multiple Compression Algorithms**: Zlib, LZMA, Brotli, Gzip, Snappy, and LZ4.
- **Terminal-Based Interaction**: Prompts for directory input and optionally logs results to a text file.
- **Progress Bars**: Shows the progress of each compression algorithm using the `tqdm` library.
- **Compression Metrics**: Logs compression time, input and output sizes, and compression ratio.
- **Supports Directory Search**: Compresses all `.txt` files in the given directory or current directory.

## Installation

### Requirements

- Python 3.x
- Dependencies:
  - `tqdm`
  - `lz4`
  - `brotli`
  - `snappy`
  
### Installing Dependencies

To install the required Python dependencies, run:

```bash
pip install tqdm lz4 brotli python-snappy
```

### Running the Script

1. Clone the repository or download the script.
2. Run the Python script from the terminal.

```bash
python compressor.py
```

3. When prompted, provide the directory containing text files for compression. If you don't provide any input, the program will use the current directory.

```plaintext
Please enter the directory path (leave blank for current directory): 
```

4. The program will display progress bars for each compression algorithm and output results in the terminal.
5. At the end of the process, the program will ask if you'd like to save the results to a file (`compression_results.txt`).

```plaintext
Do you want to save the results to a file? (yes/no): 
```

## Creating an Executable

To convert the Python script into a standalone executable, you can use `PyInstaller`.

### Install PyInstaller

```bash
pip install pyinstaller
```

### Generate the Executable

Run the following command to create a single-file executable:

```bash
pyinstaller --onefile --console compressor.py
```

The executable will be generated in the `dist` folder.

## Usage

### Running the Executable

You can run the generated executable by double-clicking it or running it from the command line. The program will prompt for a directory path and process the text files inside.

### Example

```bash
compressor.exe
```

If you leave the directory prompt blank, it will use the current working directory.

### Sample Output

```plaintext
Processing file: /path/to/textfile.txt
Zlib Compression: 100%|██████████| 1.2M/1.2M [00:01<00:00, 1.5MB/s]
Results for Zlib:
Input Size: 1253456 bytes
Output Size: 456789 bytes
Compression Time: 1.234567 seconds
Compression Ratio: 0.36
...
Do you want to save the results to a file? (yes/no): yes
Results saved to compression_results.txt.
```

## Logs

When the user opts to save the results, the program generates a `compression_results.txt` file in the specified directory with the following format:

```plaintext
Compression Results Log
========================================
Language: example_file
Algorithm: Zlib
Input Size: 123456 bytes
Output Size: 56789 bytes
Compression Time: 1.234567 seconds
Compression Ratio: 0.46
========================================
...
```
