import sqlite3

def create_connection():
    conn = sqlite3.connect('database.db')
    return conn

def close_connection(conn):
    conn.close()

def create_image_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS image_data
                 (image_name TEXT PRIMARY KEY, detections TEXT, timestamp TEXT)''')
    conn.commit()
    close_connection(conn)

def insert_image(image_name, detections, timestamp):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO image_data VALUES (?, ?, ?)", (image_name, detections, timestamp))
    conn.commit()
    close_connection(conn)

def get_image(start_date, end_date):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM image_data WHERE timestamp BETWEEN ? AND ?", (start_date, end_date))
    images = c.fetchall()
    close_connection(conn)
    return images

def get_detections(start_date, end_date):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT detections FROM image_data WHERE timestamp BETWEEN ? AND ?", (start_date, end_date))
    all_detections = [d[0] for d in c.fetchall()]
    conn.close()
    return all_detections
