import os
import sys
import csv
import logging

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teacher_query_system.settings")

import django

django.setup()

from teachers_app.models import Teacher

logging.basicConfig(level=logging.INFO)

def load_data(csv_file_path):
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                name, department, title, image_url = row

                teacher, created = Teacher.objects.get_or_create(
                    name=name,
                    department=department,
                    title=title,
                    image_url=image_url
                )

                if created:
                    logging.info(f"Added new teacher: {name}, {department}, {title}, {image_url}")
                else:
                    logging.info(f"Skipped duplicate teacher: {name}")

        logging.info(f"Data from {csv_file_path} has been loaded into the database successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == '__main__':
    current_directory = os.path.dirname(os.path.abspath(__file__))
    csv_files = [
        os.path.join(current_directory, 'professors_information.csv'),
        os.path.join(current_directory, 'associate professor_information.csv'),
        os.path.join(current_directory, 'lecturer_information.csv')
    ]

    for csv_file in csv_files:
        load_data(csv_file)