from openpyxl import Workbook
import sys
import json
import glob
import cv2
import os
import calculate

if __name__ == "__main__":
    data = json.loads(sys.argv[1])
    nasPath = data["nasPath"]
    inputDir = data["inputDir"]
    outputDir = data["outputDir"]

    os.makedirs(nasPath + outputDir, exist_ok=True)

    wb = Workbook()
    ws = wb.active
    ws.append(["너비", "높이", "더하기", "빼기"])

    img_arr = glob.glob(nasPath + inputDir + "/*.png")
    for i in img_arr:
        file_name = os.path.basename(i)

        img = cv2.imread(i)
        w, h = img.shape[:2]
        ws.append([w, h, calculate.add(w,h), calculate.sub(w,h)])

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(nasPath + outputDir + "/proc_" + file_name, gray)
    
    wb.save(nasPath + outputDir + "/report.csv")