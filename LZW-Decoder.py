# By Bhuvi Alluri

import sys
import struct

def main():
    # Validate command line arguments
    if len(sys.argv) != 3:
        print("Usage: python LZW-Decoder.py <encoded_file> <bit_length>")
        sys.exit(1)

    encoded_filename = sys.argv[1]
    bit_length = int(sys.argv[2])
    max_table_size = 2 ** bit_length

    # Read the encoded file
    try:
        with open(encoded_filename, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Error: File '{encoded_filename}' not found.")
        sys.exit(1)

    # Convert bytes to list of codes
    codes = []
    for i in range(0, len(data), 2):
        chunk = data[i:i+2]
        if len(chunk) != 2:
            print("Error: Encoded file has incomplete bytes.")
            sys.exit(1)
        code = struct.unpack('>H', chunk)[0]
        codes.append(code)

    # Initialize dictionary with ASCII characters
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256

    # Decode the codes
    decoded_data = []
    if not codes:
        decoded_str = ""
    else:
        # Process the first code
        current_code = codes[0]
        if current_code not in dictionary:
            print(f"Error: Invalid code {current_code} in encoded file.")
            sys.exit(1)
        current_str = dictionary[current_code]
        decoded_data.append(current_str)

        # Process remaining codes
        for code in codes[1:]:
            if code in dictionary:
                new_str = dictionary[code]
            else:
                # Handle case where code is not in the dictionary
                new_str = current_str + current_str[0]

            decoded_data.append(new_str)

            # Add new entry to the dictionary if space allows
            if len(dictionary) < max_table_size:
                dictionary[next_code] = current_str + new_str[0]
                next_code += 1

            current_str = new_str

        decoded_str = ''.join(decoded_data)

    # Print the decoded output
    print("\nDecoded output:")
    print(decoded_str)

    # Generate output filename
    base_name = encoded_filename.rsplit(".lzw", 1)[0]
    output_filename = f"{base_name}_decoded.txt"

    # Write the decoded data to the output file
    try:
        with open(output_filename, 'w', encoding='ascii') as f:
            f.write(decoded_str)
    except UnicodeEncodeError:
        print("Error: Decoded data contains non-ASCII characters.")
        sys.exit(1)

if __name__ == "__main__":
    main()