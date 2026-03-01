# check-safetensors-file

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Support](https://img.shields.io/pypi/pyversions/check-safetensors-file.svg)](https://pypi.org/project/check-safetensors-file/)

A command-line tool to analyze [safetensors](https://github.com/huggingface/safetensors) files and identify potentially problematic dtypes.

Marks problematic types with visual indicators:
- **⚠️ bf16** - Brain float 16 (proceed with caution)
- **🚫 fp8 variants** - FP8 formats (consider conversion or alternative models)

## Features

- 🔍 Parse safetensors file headers
- 📊 Display all dtypes found in the model
- ⚠️ Visual warnings for problematic dtypes
- 🚫 Clear identification of FP8 formats

## Installation

### From PyPI

```bash
pip install check-safetensors-file
```

### From Source

```bash
git clone https://github.com/chazzofalf/model_type_identifier.git
cd model_type_identifier
pip install .
```

## Usage

### As a Python module

```bash
python -m check_safetensors_file <safetensors_file>
```

### As a CLI command

```bash
check-safetensors-file <safetensors_file>
```

## Examples

### Basic usage

```bash
check-safetensors-file model.safetensors
```

### Output example

```
float16
float32

⚠️ Warning: Brain float (bf16) types detected. YMMV - proceed with caution.
```

### FP8 detection

```
F8_E4M3
F8_E5M2

🚫 Note: FP8 dtypes detected. Consider conversion or seeking out alternative models.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments

- Built for working with [Hugging Face](https://huggingface.co/) models
- Safetensors format by [Hugging Face](https://github.com/huggingface/safetensors)