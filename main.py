import os
import time
import zlib
import lzma
import brotli
import gzip
import snappy
import lz4.frame
import argparse
import csv
from tqdm import tqdm  # For progress bars


def load_text_file(file_path):
    """Load the contents of a text file in binary mode."""
    with open(file_path, 'rb') as file:
        return file.read()


def compress_with_zlib(data):
    return zlib.compress(data)


def compress_with_lzma(data):
    return lzma.compress(data)


def compress_with_brotli(data):
    return brotli.compress(data)


def compress_with_gzip(data):
    return gzip.compress(data)


def compress_with_snappy(data):
    return snappy.compress(data)


def compress_with_lz4(data):
    return lz4.frame.compress(data)


def save_compressed_file(file_path, compressed_data):
    """Save compressed data to a file."""
    with open(file_path, 'wb') as file:
        file.write(compressed_data)


def log_compression_results(language_abbreviation, algorithm, input_size, output_size, compression_time):
    """Return compression results to be logged later."""
    return {
        'Language': language_abbreviation,
        'Algorithm': algorithm,
        'Input Size (bytes)': input_size,
        'Output Size (bytes)': output_size,
        'Compression Time (s)': compression_time,
        'Compression Ratio': output_size / input_size
    }


def compress_text_files(input_directory):
    """Compress all text files in the specified directory."""
    results = []

    # Get a list of text files in the directory
    for file_name in os.listdir(input_directory):
        if file_name.endswith('.txt') and file_name != "compression_results.txt":
            input_file_path = os.path.join(input_directory, file_name)
            print(f"\nProcessing file: {input_file_path}")

            text_data = load_text_file(input_file_path)
            input_size = len(text_data)

            algorithms = {
                'Zlib': compress_with_zlib,
                'LZMA': compress_with_lzma,
                'Brotli': compress_with_brotli,
                'Gzip': compress_with_gzip,
                'Snappy': compress_with_snappy,
                'LZ4': compress_with_lz4,
            }

            # Loop through each algorithm
            for algorithm_name, compress_function in algorithms.items():
                print(f"Starting compression using {algorithm_name}...")
                start_time = time.time()  # Start timing

                # Initialize progress bar
                with tqdm(total=input_size, desc=f'{algorithm_name} Compression', unit='B', unit_scale=True) as pbar:
                    compressed_data = compress_function(text_data)
                    pbar.update(input_size)  # Update the progress bar to complete

                compression_time = time.time() - start_time  # Calculate time taken
                output_size = len(compressed_data)

                # Save the compressed file
                output_file_path = os.path.join(input_directory,
                                                f"{file_name[:-4]}_compressed_{algorithm_name.lower()}.bin")
                save_compressed_file(output_file_path, compressed_data)

                # Log the results
                result = log_compression_results(file_name[:-4], algorithm_name, input_size, output_size,
                                                 compression_time)
                results.append(result)

                # Display results in terminal
                print(f"\nResults for {algorithm_name}:")
                print(f"Input Size: {input_size} bytes")
                print(f"Output Size: {output_size} bytes")
                print(f"Compression Time: {compression_time:.6f} seconds")
                print(f"Compression Ratio: {result['Compression Ratio']:.2f}")

    return results


def save_results_to_csv(results, directory):
    """Save compression results to a CSV file."""
    results_file_path = os.path.join(directory, "compression_results.csv")

    with open(results_file_path, mode='w', newline='') as csv_file:
        fieldnames = [
            'Language', 'Algorithm', 'Input Size (bytes)',
            'Output Size (bytes)', 'Compression Time (s)', 'Compression Ratio'
        ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for result in results:
            writer.writerow(result)

    print(f"Results saved to {results_file_path}.")

def main():
    # Ask user for the directory in the terminal
    directory = input("Please enter the directory path (leave blank for current directory): ").strip()

    if not directory:  # If no input, use the current directory
        directory = os.getcwd()

    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    # Compress text files in the specified directory
    results = compress_text_files(directory)

    # Ask the user if they want to save the results to a CSV file
    save_to_file = input("\nDo you want to save the results to a CSV file? (yes/no): ").strip().lower()
    if save_to_file == 'yes':
        save_results_to_csv(results, directory)

if __name__ == "__main__":
    main()
