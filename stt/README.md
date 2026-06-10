# Json output example
result = evaluate_speech(r"D:\project\recordings\New Recording 73.m4a", "أحبُّ المدرسةَ")
print(result)

Output:
{'success': True, 'predicted_text': 'أحب المدرسة', 'expected_text': 'أحبُّ المدرسةَ', 'similarity': 100.0, 'status': 'PASS'}

# Installation

```bash
pip install -r requirements.txt
```
# How to use as a node.js

```bash
const { spawn } = require('child_process');
const path = require('path');

const pythonProcess = spawn('python', [
    path.join(__dirname, 'speech_eval.py'), // اسم الملف بتاعك
    'path/to/audio_record.wav',            // مسار ملف الصوت اللي جاي من Flutter
    'الكلمة المتوقعة'                        // النص اللي المفروض الطفل ينطقه
]);

example
py main.py "D:/Graduation Project/project/recordings/New Recording 73.m4a" "احب المدرسة"

let resultData = "";
pythonProcess.stdout.on('data', (data) => {
    resultData += data.toString();
});

pythonProcess.on('close', (code) => {
    try {
        const finalJson = JSON.parse(resultData.trim());
        console.log("Speech Result:", finalJson);
    } catch (e) {
        console.error("Error parsing Python output");
    }
});
```
