# Highlighter

When you only want to highlight words in a stream (and not grep or filter anything), this tool is for you.

## Prerequisites

Made with Pyhton 2.7.5, not sure if it works with Python 3+.

The shell needs to support ANSI escape sequences. All major shells supports it.

## Installation

Run ```pip install https://github.com/mattissf/highlighter/archive/master.zip``` from a shell and it will install an executable script called ```hl```.

## Usage

For example run ```echo "a long sentence with some words that should be highlighted" | hl sentence words``` and the words 
```sentence``` and ```words``` will be highlighted.
