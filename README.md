# check-safetensors-file

A command-line tool to analyze safetensors files and list dtypes found within.

Marks bf16 with ⚠️ and fp8 variants with 🚫

## Installation

```bash
pip install .
```

Or from PyPI (when available):

```bash
pip install check-safetensors-file
```

## Usage

```bash
# As a Python module
python -m check_safetensors_file <safetensors_file>

# As a CLI command
check-safetensors-file <safetensors_file>
```

## Example

```bash
check-safetensors-file model.safetensors
```

## License

MIT License