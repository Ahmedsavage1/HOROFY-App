# Handwriting Recognition and Dysgraphia Detection

This module provides an AI-based solution for processing Arabic handwriting, extracting text, and identifying potential mirror writing (Dysgraphia) patterns.

## Features
- **Arabic OCR:** High-accuracy Arabic text extraction using PaddleOCR.
- **Orientation Correction:** Automatic handling of RTL (Right-to-Left) reading order.
- **Mirroring Detection:** Intelligent image-flipping logic to distinguish between system errors and Dysgraphia.
- **Accuracy Metrics:** Sequence-based scoring using Levenshtein Distance.

## Tech Stack
- **Language:** Python 3.12
- **Core Libraries:** PaddleOCR, OpenCV, python-Levenshtein.

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

# How to use as as a node.js

```bash

#Example
const { spawn } = require('child_process');
const path = require('path');

const pythonProcess = spawn('python', [
    path.join(__dirname, 'paddle/main.py'), 
    'D:/Graduation Project/pdfs/dmamatest.jpeg', 
    'ماما'
]);

let resultData = "";

pythonProcess.stdout.on('data', (data) => {
    resultData += data.toString();
});

pythonProcess.on('close', (code) => {
    try {
        const lines = resultData.trim().split('\n');
        const finalJson = JSON.parse(lines[lines.length - 1]);
        console.log("OCR Result:", finalJson);
    } catch (e) {
        console.error("OCR Error:", resultData);
    }
});

```