# Advanced Python Programming Problems for Year 8
## Data Processing and Analysis Through Real-World Applications

### Introduction
These problems are designed to introduce advanced programming concepts through practical applications. Each problem builds upon previous knowledge while introducing new concepts. We'll work with real data, create interactive applications, and learn modern programming practices.

### Problem 1: Weather Data Analyzer
**Concept Focus:** File handling, Data Structures, and Basic Statistics

#### Learning Objectives:
- Reading data from CSV files
- Working with dictionaries and lists
- Implementing statistical calculations
- Error handling and data validation

```python
"""
Create a weather data analyzer that reads temperature data from a CSV file
and provides statistical analysis.

CSV Format Example:
date,temperature,humidity
2024-01-01,12.5,65
2024-01-02,13.2,70
2024-01-03,11.8,68
"""

import csv
from datetime import datetime
from typing import Dict, List, Tuple

class WeatherAnalyzer:
    def __init__(self, filename: str):
        self.filename = filename
        self.temperatures: List[float] = []
        self.humidity_data: List[float] = []
        self.date_temp_map: Dict[datetime, float] = {}
        
    def load_data(self) -> None:
        """
        Loads and validates weather data from CSV file.
        Implements error handling for missing or invalid data.
        """
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        date = datetime.strptime(row['date'], '%Y-%m-%d')
                        temp = float(row['temperature'])
                        humidity = float(row['humidity'])
                        
                        # Store data in our structures
                        self.temperatures.append(temp)
                        self.humidity_data.append(humidity)
                        self.date_temp_map[date] = temp
                    except ValueError as e:
                        print(f"Invalid data in row: {row}. Error: {e}")
                        continue
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find file: {self.filename}")
    
    def get_statistics(self) -> Dict[str, float]:
        """
        Calculates basic statistics for temperature data.
        Returns dictionary with min, max, average, and range.
        """
        if not self.temperatures:
            return {}
            
        return {
            'minimum': min(self.temperatures),
            'maximum': max(self.temperatures),
            'average': sum(self.temperatures) / len(self.temperatures),
            'range': max(self.temperatures) - min(self.temperatures)
        }
    
    def find_temperature_trends(self) -> List[Tuple[datetime, str]]:
        """
        Analyzes temperature trends by comparing consecutive days.
        Returns list of dates and trend indicators.
        """
        trends = []
        dates = sorted(self.date_temp_map.keys())
        
        for i in range(1, len(dates)):
            prev_temp = self.date_temp_map[dates[i-1]]
            curr_temp = self.date_temp_map[dates[i]]
            
            if curr_temp > prev_temp:
                trend = "increasing"
            elif curr_temp < prev_temp:
                trend = "decreasing"
            else:
                trend = "stable"
                
            trends.append((dates[i], trend))
            
        return trends

# Example usage
def main():
    analyzer = WeatherAnalyzer('weather_data.csv')
    try:
        analyzer.load_data()
        stats = analyzer.get_statistics()
        trends = analyzer.find_temperature_trends()
        
        print("Weather Statistics:")
        for key, value in stats.items():
            print(f"{key.capitalize()}: {value:.2f}")
            
        print("\nTemperature Trends:")
        for date, trend in trends:
            print(f"{date.strftime('%Y-%m-%d')}: {trend}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

#### Advanced Concepts and Best Practices:
1. **Type Hints**
   - Using Python's type hinting system
   - Improves code readability and maintainability
   - Enables better IDE support

2. **Class Structure**
   - Organizing data and methods in a class
   - Encapsulation of related functionality
   - Clear separation of concerns

3. **Error Handling**
   - Try-except blocks for file operations
   - Validation of input data
   - Graceful error reporting

4. **Data Structures**
   - Using appropriate data structures (lists, dictionaries)
   - Efficient data organization
   - Easy access patterns

### Problem 2: Text Analysis Engine
**Concept Focus:** Natural Language Processing Basics

This problem introduces basic text analysis concepts including:
- Word frequency analysis
- Sentence structure analysis
- Basic text statistics
- Pattern matching

```python
import re
from collections import Counter
from typing import Dict, List, Set

class TextAnalyzer:
    def __init__(self, text: str):
        self.text = text
        self.words: List[str] = []
        self.sentences: List[str] = []
        self.word_frequencies: Dict[str, int] = {}
        self.prepare_text()
        
    def prepare_text(self) -> None:
        """
        Preprocesses text by:
        1. Splitting into sentences
        2. Extracting words
        3. Removing punctuation
        4. Converting to lowercase
        """
        # Split into sentences (basic implementation)
        self.sentences = [s.strip() for s in re.split(r'[.!?]+', self.text) if s.strip()]
        
        # Extract words and clean them
        self.words = [
            word.lower() for sentence in self.sentences
            for word in re.findall(r'\w+', sentence)
        ]
        
        # Calculate word frequencies
        self.word_frequencies = Counter(self.words)
    
    def get_word_stats(self) -> Dict[str, float]:
        """
        Calculates various text statistics.
        """
        if not self.words:
            return {}
            
        return {
            'average_word_length': sum(len(word) for word in self.words) / len(self.words),
            'unique_words': len(set(self.words)),
            'total_words': len(self.words),
            'sentence_count': len(self.sentences)
        }
    
    def find_common_words(self, n: int = 5) -> List[Tuple[str, int]]:
        """
        Returns the n most common words and their frequencies.
        """
        return self.word_frequencies.most_common(n)
    
    def get_sentence_complexity(self) -> Dict[str, float]:
        """
        Analyzes sentence complexity based on:
        - Words per sentence
        - Average word length per sentence
        - Unique words per sentence
        """
        if not self.sentences:
            return {}
            
        complexities = []
        for sentence in self.sentences:
            words = re.findall(r'\w+', sentence.lower())
            if words:
                complexity = {
                    'word_count': len(words),
                    'avg_word_length': sum(len(word) for word in words) / len(words),
                    'unique_ratio': len(set(words)) / len(words)
                }
                complexities.append(complexity)
        
        # Calculate averages across all sentences
        return {
            'avg_words_per_sentence': sum(c['word_count'] for c in complexities) / len(complexities),
            'avg_complexity_score': sum(c['avg_word_length'] * c['unique_ratio'] 
                                     for c in complexities) / len(complexities)
        }

# Example usage
def main():
    sample_text = """
    Python is a versatile programming language. It's used in web development, 
    data analysis, artificial intelligence, and scientific computing! The syntax 
    is clear and readable, making it great for beginners.
    """
    
    analyzer = TextAnalyzer(sample_text)
    
    print("Text Statistics:")
    stats = analyzer.get_word_stats()
    for key, value in stats.items():
        print(f"{key.replace('_', ' ').title()}: {value:.2f}")
    
    print("\nMost Common Words:")
    common_words = analyzer.find_common_words()
    for word, count in common_words:
        print(f"{word}: {count}")
    
    print("\nSentence Complexity:")
    complexity = analyzer.get_sentence_complexity()
    for key, value in complexity.items():
        print(f"{key.replace('_', ' ').title()}: {value:.2f}")

if __name__ == "__main__":
    main()
```

#### Key Learning Points:
1. **Regular Expressions**
   - Pattern matching for text analysis
   - Text cleaning and preprocessing
   - Extracting specific patterns

2. **Collections Module**
   - Using Counter for frequency analysis
   - Efficient data structures for counting
   - Built-in helper methods

3. **Text Processing Techniques**
   - Sentence splitting
   - Word tokenization
   - Basic text statistics

4. **Object-Oriented Design**
   - Modular code structure
   - Reusable components
   - Clear method responsibilities

[Continued in next problems...]
