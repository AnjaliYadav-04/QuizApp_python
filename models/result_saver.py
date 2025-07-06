import csv
import os

class ResultSaver:
    @staticmethod
    def save_to_csv(username,score,total,filename="data/result.csv"):
        file_exists=os.path.isfile(filename)
        with open(filename,mode='a',newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Username", "Score", "Total"])
            writer.writerow([username, score, total]) 