import os
import json
import cv2
import Levenshtein
import sys 
from paddleocr import PaddleOCR


os.environ['FLAGS_use_onednn'] = '0'
ocr = PaddleOCR(lang='ar', use_gpu=False, show_log=False)

def check_writing(image_path, target):
    img = cv2.imread(image_path)
    if img is None: return json.dumps({"error": "Image not found"})

    result = ocr.ocr(img, cls=True)
    raw = "".join([line[1][0] for line in result[0]]).replace(" ", "").strip() if result[0] else ""
    predicted = raw[::-1]

    dist = Levenshtein.distance(predicted, target)
    max_l = max(len(target), 1)
    accuracy = round(((max_l - dist) / max_l) * 100, 2)

    dysgraphia_alarm = False
    
    if accuracy < 80:
        flipped_img = cv2.flip(img, 1)
        res_flip = ocr.ocr(flipped_img, cls=True)
        raw_flip = "".join([line[1][0] for line in res_flip[0]]).replace(" ", "").strip() if res_flip[0] else ""
        predicted_flip = raw_flip[::-1]

        dist_flip = Levenshtein.distance(predicted_flip, target)
        accuracy_flip = round(((max_l - dist_flip) / max_l) * 100, 2)

        if accuracy_flip > accuracy:
            predicted = predicted_flip
            accuracy = accuracy_flip
            dysgraphia_alarm = True

    if not dysgraphia_alarm and predicted == target[::-1] and predicted != target:
        dysgraphia_alarm = True

    return json.dumps({
        "predicted_text": predicted, 
        "true_text": target,          
        "accuracy": accuracy,   
        "dysgraphia_alarm": dysgraphia_alarm       
    }, ensure_ascii=False)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        img_p = sys.argv[1]
        target_w = sys.argv[2]
        
        output_json = check_writing(img_p, target_w)
        
        sys.stdout.write(output_json + '\n')
        sys.stdout.flush()


{
 "true_text": "ماما", 
 "predicted_text": "ماما", 
 "accuracy": 100.0, 
 "dysgraphia_alarm": True
 }     

