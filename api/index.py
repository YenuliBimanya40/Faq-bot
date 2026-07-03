import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)

from app import app

app.template_folder = os.path.join(ROOT_DIR, 'templates')
app.static_folder = os.path.join(ROOT_DIR, 'static')

if __name__ == '__main__':
    app.run()
