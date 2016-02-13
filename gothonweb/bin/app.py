import web

urls = (
	'/','index'
)

app = web.application(urls, gobals())

class index:
	def GET(self):
		greeting = "Hello World"
		return greeting
		

if __name__ == "__main__":
	app.run()