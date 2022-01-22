from app import create_app
from app import is_in_development

app = create_app()

if __name__ == "__main__":
    app.run()