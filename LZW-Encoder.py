# By Bhuvi Alluri

import sys  # For handling command line arguments
import struct   # For converting integers to bytes

def main():
    # Validate command line arguments
    if len(sys.argv) != 3:
        print("Usage: python LZW-Encoder.py <input_file> <bit length>")
        sys.exit(1)

    # Read command line arguments
    input_filename = sys.argv[1]
    bit_length = int(sys.argv[2])
    max_table_size = 2 ** bit_length

    # Initalize dictionary with ASCII characters (0-255)
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256 # Next available code after initial ASCII set

    try:
        # Read input file as ASCII text
        with open(input_filename, "r", encoding='ascii') as input_file:
            input_data = input_file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: File '{input_filename}' is not ASCII text.")
        sys.exit(1)
    
    current_string = "" # Current string to be encoded
    output_codes = [] # List to store compressed output codes

    # Main compression algorithm
    for symbol in input_data:
        combined_string = current_string + symbol

        # Check if combined string already exists in dictionary
        if combined_string in dictionary:
            current_string = combined_string # Extend current string
        else:
            # Output code for current string
            output_codes.append(dictionary[current_string])

            # Add new string to dictionary if space is available
            if len(dictionary) < max_table_size:
                dictionary[combined_string] = next_code
                next_code += 1

            #Start new string with current symbol
            current_string = symbol

    # Handle remaining string in input data
    if current_string:
        output_codes.append(dictionary[current_string])

    # Print the encoded integers
    print("\nEncoded output (as integers):")
    print(output_codes)
    
    # Generate output filename (remove extension if there is one)
    base_name = input_filename.rsplit(".", 1)[0]
    output_filename = f"{base_name}.lzw"

    # Write compressed codes to output file
    with open(output_filename, 'wb') as file:
        for code in output_codes:
            # Convert code to 2-byte big-endian format
            file.write(struct.pack(">H", code))

if __name__ == "__main__":
    main()