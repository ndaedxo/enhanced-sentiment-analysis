# Enhanced Sentiment Analysis Tool

This project provides a powerful and flexible sentiment analysis tool using Python and the Hugging Face Transformers library. It can analyze individual text inputs or process entire files, outputting results in JSON or CSV format.

## Features

- Analyze sentiment of single text inputs
- Process entire files for batch sentiment analysis
- Output results in JSON or CSV format
- Easy-to-use command-line interface

## Prerequisites

- Python 3.7+
- pip package manager

## Installation

1. Clone the repository:
```bash
git https://github.com/ndaedxo/enhanced-sentiment-analysis.git
cd enhanced-sentiment-analysis
```

2. Install the required dependencies:
```bash
pip install transformers torch
```

## Usage

### Analyzing a Single Text Input

To analyze the sentiment of a single piece of text:

```bash
python sentiment_analyzer.py "Your text here"
```

### Analyzing Texts from a File

1. Create a text file with one text per line.
2. Run the script with the `--file` flag:

```bash
python sentiment_analyzer.py path/to/your/file.txt --file
```

### Output Formats

Choose between JSON (default) and CSV output formats:

```bash
# JSON output (default)
python sentiment_analyzer.py path/to/your/file.txt --file

# CSV output
python sentiment_analyzer.py path/to/your/file.txt --file --output csv
```

## Output Details

Each sentiment analysis result includes:
- The original text
- Sentiment classification (positive, negative, or neutral)
- Confidence score (ranging from 0 to 1)

### Example Output (JSON)
```json
{
  "text": "I love this product!",
  "sentiment": "positive",
  "score": 0.9876
}
```

## Command-Line Arguments

- `input`: Text or file path to analyze (required)
- `--file`: Treat input as a file path (optional)
- `--output`: Specify output format ('json' or 'csv', default is 'json')

## Examples

1. Analyze a single positive text:
```bash
python sentiment_analyzer.py "I love this product! It's amazing!"
```

2. Analyze texts from a file and save as CSV:
```bash
python sentiment_analyzer.py reviews.txt --file --output csv
```

## Performance Considerations

- The tool uses a pre-trained DistilBERT model for sentiment analysis
- Processing large files may take some time depending on your hardware
- Ensure you have sufficient memory when analyzing large datasets

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Troubleshooting

- Ensure all dependencies are correctly installed
- Check that your input text or file is properly formatted
- For large files, monitor system resources during processing

## 👤 Author

Ndaedzo Austin Mukhuba
- GitHub: [@ndaedzo](https://github.com/ndaedxo)
- LinkedIn: [Ndaedzo Austin Mukhuba](https://linkedin.com/in/ndaedzo-mukhuba-71759033b)
- Email: [ndaemukhuba](ndaemukhuba@gmail.com)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Hugging Face Transformers](https://github.com/huggingface/transformers) library
- Sentiment analysis powered by pre-trained DistilBERT model

## Contact

For questions, issues, or suggestions, please open an issue on the GitHub repository.
