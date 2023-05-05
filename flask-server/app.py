from flask import Flask, request, jsonify
from flask_cors import CORS
from database import create_image_table, insert_image, get_image, get_detections
import datetime
from datetime import datetime
import csv
import os
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    df = pd.read_csv(file)
    for i, row in df.iterrows():
        image_name = row[0]
        objects_detected = row[1]
        timestamp = row[2]
        insert_image(image_name,objects_detected,timestamp)
    
    return 'File uploaded successfully!'

@app.route('/images', methods=['GET'])
def get_images_handler():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    images = get_image(start_date, end_date)

    image_list = []
    for image in images:
        data = {
            'image_name': image[0],
            'detections': image[1],
            'image_path': f'static/{image[0]}'
        }
        image_list.append(data)

    report_filename = 'report.csv'
    if os.path.exists(report_filename):
        os.remove(report_filename)

    all_detections=get_detections(start_date,end_date)
    object_counts = {}
    for detection_list in all_detections:
        detections = detection_list.split(',')
        for detection in detections:
            detection = detection.strip()
            if detection in object_counts:
                object_counts[detection] += 1
            else:
                object_counts[detection] = 1

    with open(report_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['threat', 'occurence'])
        for obj, count in object_counts.items():
            writer.writerow([obj, count])

    return jsonify({'images': image_list})

@app.route('/')
def index():
    return "working"

@app.route('/createtable')
def create_table():
    create_image_table()
    return "Database created"

if __name__ == '__main__':
    app.run(debug=True)