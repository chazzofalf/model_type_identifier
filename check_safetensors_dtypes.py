#!/Volumes/projs/projs/model_type_identifier/.venv/bin/python3.12
"""
Script to analyze safetensors files and list dtypes found within.
Marks bf16 with ⚠️ and fp8 variants with 🚫
"""

import sys
import struct
import json


def get_dtype_display(dtype_str):
    """Return a display string for the dtype with appropriate markers."""
    dtype_lower = dtype_str.lower()
    
    # Check for fp8 variants first (takes precedence)
    # FP8 variants in safetensors: F8_E4M3, F8_E5M2, etc.
    if 'f8' in dtype_lower or 'fp8' in dtype_lower:
        return f"{dtype_str} 🚫"
    
    # Check for brain float 16
    if 'bf16' in dtype_lower or 'bfloat16' in dtype_lower:
        return f"{dtype_str} ⚠️"
    
    return dtype_str


def parse_safetensors_header(file_path):
    """Parse the safetensors file header and return tensor information."""
    with open(file_path, 'rb') as f:
        # Read first 8 bytes to get header size
        header_size_bytes = f.read(8)
        if len(header_size_bytes) < 8:
            raise ValueError("Invalid safetensors file: unable to read header size")
        
        header_size = struct.unpack('<Q', header_size_bytes)[0]
        
        if header_size == 0:
            raise ValueError("Invalid safetensors file: header size is 0")
        
        # Read header JSON
        header_bytes = f.read(header_size)
        header = json.loads(header_bytes.decode('utf-8'))
        
        return header


def main():
    if len(sys.argv) != 2:
        print("Usage: python check_safetensors_dtypes.py <safetensors_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    try:
        header = parse_safetensors_header(file_path)
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading safetensors file: {e}")
        sys.exit(1)
    
    # Collect dtypes from the header
    dtypes = {}
    has_fp8 = False
    has_bf16 = False
    
    for tensor_name, tensor_info in header.items():
        # Skip metadata key
        if tensor_name == '__metadata__':
            continue
        
        dtype = tensor_info.get('dtype', 'unknown')
        dtypes[dtype] = True
        
        # Check for fp8 or bf16
        dtype_lower = dtype.lower()
        # FP8 variants in safetensors: F8_E4M3, F8_E5M2, etc.
        if 'f8' in dtype_lower or 'fp8' in dtype_lower:
            has_fp8 = True
        if 'bf16' in dtype_lower or 'bfloat16' in dtype_lower:
            has_bf16 = True
    
    # Display dtypes
    for dtype in sorted(dtypes.keys()):
        print(get_dtype_display(dtype))
    
    # Display appropriate notice
    if has_fp8:
        print()
        print("🚫 Note: FP8 dtypes detected. Consider conversion or seeking out alternative models.")
    elif has_bf16:
        print()
        print("⚠️ Warning: Brain float (bf16) types detected. YMMV - proceed with caution.")
    else:
        print()
        print("✅ All checks out, not conversion or consideration needed")


if __name__ == '__main__':
    main()