import sqlite3
import csv

db_filename = "depression_survey.db"
conn = sqlite3.connect(db_filename)
c = conn.cursor()

query = "SELECT * FROM survey_results"

c.execute(query)
data = c.fetchall()

column_names = [desc[0] for desc in c.description]

csv_filename = "checklist_data.csv"

with open(csv_filename, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(column_names)
    csv_writer.writerows(data)

print(f"Data exported to {csv_filename}")
conn.close()
