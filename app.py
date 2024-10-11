import web

urls = (
    '/(.*)', 'Index'  # Asegúrate de que 'Index' sea una cadena correcta
)

class Index:
    def GET(self):
        return 'Hello dani'


if __name__ == "__main__":
    app.run()