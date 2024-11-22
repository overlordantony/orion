import os

def open_application(app_name):
    os.system(f"start {app_name}")

def shutdown():
    os.system("shutdown /s /t 1")
