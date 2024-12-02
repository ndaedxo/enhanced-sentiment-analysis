import argparse
from transformers import pipeline
import csv
import json

def analyze_sentiment(text):
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(text)[0]
    
    if result['label'] == 'POSITIVE':
        sentiment = 'positive'
    elif result['label'] == 'NEGATIVE':
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    return {
        'text': text,
        'sentiment': sentiment,
        'score': round(result['score'], 4)
    }

def process_file(file_path, output_format):
    with open(file_path, 'r') as file:
        texts = [line.strip() for line in file]
    
    results = [analyze_sentiment(text) for text in texts]
    
    if output_format == 'json':
        with open('sentiment_results.json', 'w') as f:
            json.dump(results, f, indent=2)
    elif output_format == 'csv':
        with open('sentiment_results.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['text', 'sentiment', 'score'])
            writer.writeheader()
            writer.writerows(results)
    
    return results

def main():
    parser = argparse.ArgumentParser(description="Sentiment Analysis Tool")
    parser.add_argument("input", help="Input text or file path")
    parser.add_argument("--file", action="store_true", help="Treat input as a file path")
    parser.add_argument("--output", choices=['json', 'csv'], default='json', help="Output format (default: json)")
    
    args = parser.parse_args()
    
    if args.file:
        results = process_file(args.input, args.output)
        print(f"Analysis complete. Results saved to sentiment_results.{args.output}")
    else:
        result = analyze_sentiment(args.input)
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()