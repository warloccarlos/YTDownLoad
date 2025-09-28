from ui import create_app
from ui.network import get_ip

app  = create_app()

if __name__ == '__main__':
    app.run(host=get_ip(), debug=False)