import os
import shutil
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# -----------------------------
# Configuration
# -----------------------------
APP_DIR = "/var/www/berwa_app"  # Example application directory
DB_NAME = "berwa_school"
DB_USER = "root"
DB_PASSWORD = "your_db_password"
BACKUP_DIR = os.path.join(os.path.expanduser("~"), "berwa_backups")

EMAIL_NOTIFICATIONS = True
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_email_password"
NOTIFY_TO = "admin@berwa.rw"

# Ensure backup directory exists
os.makedirs(BACKUP_DIR, exist_ok=True)


# -----------------------------
# Functions
# -----------------------------

def configure_server():
    """
    Simulate server configuration.
    Real tasks can include setting permissions, restarting services, environment variables, etc.
    """
    try:
        print("Configuring server...")
        # Example: change permissions
        os.chmod(APP_DIR, 0o755)
        print(f"Server directory permissions set for {APP_DIR}")
        # Example: restart web server (requires sudo privileges)
        # os.system("sudo systemctl restart apache2")
        print("Server configuration complete.\n")
    except Exception as e:
        print(f"Error configuring server: {e}")


def backup_database():
    """
    Backup MySQL database using mysqldump
    """
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(BACKUP_DIR, f"{DB_NAME}_backup_{timestamp}.sql")
        print(f"Backing up database to {backup_file} ...")
        os.system(f"mysqldump -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} > {backup_file}")
        print("Database backup completed.\n")
    except Exception as e:
        print(f"Error backing up database: {e}")


def send_notification(subject, message):
    """
    Send notification email
    """
    if not EMAIL_NOTIFICATIONS:
        print("Email notifications disabled.")
        return

    try:
        print("Sending notification email...")
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = NOTIFY_TO
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Notification email sent.\n")
    except Exception as e:
        print(f"Error sending notification: {e}")


# -----------------------------
# Main Deployment Script
# -----------------------------
if __name__ == "__main__":
    print("=== BERWA School Deployment Automation ===\n")

    configure_server()
    backup_database()

    notification_subject = "Deployment Completed for BERWA School App"
    notification_message = f"Deployment completed successfully for BERWA School application.\nDate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\nBackup location: {BACKUP_DIR}"

    send_notification(notification_subject, notification_message)

    print("All automated deployment tasks completed successfully.")
