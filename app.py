import web

urls = (
    '/(.*)', 'Index'
)
app = web.application(urls)

class Index:
    def GET(self):
        return 'Hello dani'

if __name__ == "__main__":
    app.run()