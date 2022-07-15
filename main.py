from website import create_app
import sys
sys.path.append(".")

app = create_app()

if __name__ == '__main__':
    app.secret_key = 'xxxxyyyyyzzzzz'


    app.run(debug=True)
