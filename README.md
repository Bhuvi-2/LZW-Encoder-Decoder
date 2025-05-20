# LZW File Compression and Decompression Tool

A Python implementation of the LZW algorithm for text file compression and decompression.

---

## Program Design
- **Encoder (`LZW-Encoder.py`):**  
  - Compresses ASCII text files using LZW.  
  - Builds a dynamic dictionary starting with 256 ASCII entries.  
  - Outputs compressed codes as 2-byte binary data in a .lzw file.  

- **Decoder (`LZW-Decoder.py`):**  
  - Reconstructs the original text from .lzw files.  
  - Rebuilds the dictionary identically to the encoder during decompression.  

### Data Structures
- **Dictionary:**  
  - Encoder: `{"string": code}` (e.g., `{"AB": 256}`).  
  - Decoder: `{code: "string"}` (e.g., `{256: "AB"}`).  
- **Bit Length:** User-defined (e.g., 12 bits = 4096 max entries).  

---

## File Breakdown
1. **`LZW-Encoder.py`**  
   - Using in terminal: `python LZW-Encoder.py <input_file> <bit_length>`  
   - Input: ASCII text file (e.g., 'text.txt').  
   - Output: Compressed '.lzw' file (e.g., 'text.lzw').  

2. **`LZW-Decoder.py`**  
   - Using in terminal: `python LZW-Decoder.py <encoded_file> <bit_length>`  
   - Input: `.lzw` file (e.g., `text.lzw`).  
   - Output: Decompressed `_decoded.txt` file (e.g., `text_decoded.txt`).  

---

## What Works
- Handles standard ASCII text files.  
- Correctly compresses/decompresses repetitive patterns (e.g., "ABABABA").  
- Syncs encoder/decoder dictionaries for accurate reconstruction.  
- Validates input file format by making sure it uses an ASCII-only format for the encoder.

## Limitations
- **Non-ASCII Characters:** Encoder crashes on Unicode text (e.g., emojis, accents).  
- **Bit Length Mismatch:** Decoder requires the same `bit_length` used during encoding.  
- **Large Files:** May fail if the dictionary exceeds `2^bit_length` entries.

---

## Requirements
- **Language:** Python 3.x (Tested on Python 3.11.5).  
- **Dependencies:** None (Uses built-in `sys` and `struct` libraries).  

---

## How to Run
1. **Encode a File**  
   ```bash
   python LZW-Encoder.py input.txt 12
2. **Decode a File**  
   ```bash
   python LZW-Decoder.py input.lzw 12