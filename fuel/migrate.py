import pymysql
import sqlite3
from pydantic import ValidationError

from schemas import (
    Course, AssignmentEmail, AssignmentPreference, ExamDay, ExamHour, 
    ExamPeriod, GlobalSetting, ProfessorCourse, Professor, Upload, User, 
    WelcomePost, Email, EmailUrl, Doctoral, DoctoralSupervisor, ExamCourse, ExamSupervision
)

MYSQL_CONFIG = {
    'host': '127.0.0.1',
    'port': 3307,          # phpMyAdmin port
    'user': 'root',        
    'password': '',        
    'database': 'scheduler_old',
    'cursorclass': pymysql.cursors.DictCursor 
}

# Path to the new SQLite database
SQLITE_DB_PATH = r"C:\xampp\htdocs\scheduler\fuel\app\scheduler_new.sqlite"


def migrate_table(mysql_conn, sqlite_conn, table_name, model_class):
    print(f"Starting migration for table: {table_name}...")

    with mysql_conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        
    if not rows:
        print(f"   Table {table_name} is empty. Skipping.\n")
        return

    sqlite_cursor = sqlite_conn.cursor()
    success_count = 0

    for row in rows:
        try:
            validated_item = model_class(**row)
            
            clean_data = validated_item.model_dump()
            
            columns = ', '.join([f'"{k}"' for k in clean_data.keys()])
            placeholders = ', '.join(['?'] * len(clean_data))
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

            sqlite_cursor.execute(sql, tuple(clean_data.values()))
            success_count += 1
            
        except ValidationError as e:
            print(f"Validation error in {table_name} (ID: {row.get('id')}):\n{e}")
        except sqlite3.IntegrityError as e:
            print(f"Insert error in {table_name} (ID: {row.get('id')}): {e}")
            pass 

    sqlite_conn.commit()
    print(f"Success: {success_count} / {len(rows)}\n")


def main():
    mysql_conn = pymysql.connect(**MYSQL_CONFIG)
    sqlite_conn = sqlite3.connect(SQLITE_DB_PATH)

    tables_to_migrate = {
        'courses': Course,
        'assignments_emails': AssignmentEmail,
        'assignments_preferences': AssignmentPreference,
        'examdays': ExamDay,
        'examhours': ExamHour,
        'examperiods': ExamPeriod,
        'globalsettings': GlobalSetting,
        'professorcourses': ProfessorCourse,
        'professors': Professor,
        'uploads': Upload,
        'users': User,
        'welcomeposts': WelcomePost,
        'emails': Email,
        'emailurls': EmailUrl,
        'doctorals': Doctoral,
        'doctoralsupervisors': DoctoralSupervisor,
        'examcourses': ExamCourse
    }

    try:
        for table_name, model in tables_to_migrate.items():
            migrate_table(mysql_conn, sqlite_conn, table_name, model)
            
        print(" MIGRATION FULLY COMPLETED!")
    finally:
        mysql_conn.close()
        sqlite_conn.close()

if __name__ == "__main__":
    main()