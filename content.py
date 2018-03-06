#!/usr/bin/python3

import webapp

contents = {
	'/lunes': 'lluvia',
	'/martes': 'algo mejor'
}

formulario = """
 <form action="" method="POST">
  El tiempo:<br>
  <input type="text" name="tiempo" value="sol"><br> 
  <input type="submit" value="Enviar">
</form> 
"""

class contentApp(webapp.webApp):

	def parse(self,request):
		return (request.split()[0], request.split()[1], request)  
#cojo metodo[0], recurso[1] y cuerpo [donde encontremos doble linea en blanco por primera vez[0=cabeceras,1=cuerpo]]

	def process(self, parsedRequest):
		metodo, recurso, peticion = parsedRequest
		if metodo == "POST":
			cuerpo = peticion.split('\r\n\r\n',1)[1]
			contents[recurso] = cuerpo.split('=')[1]
			return("200 OK","<html>" + contents[recurso] + "</html>")
		else: #si hago metodo=="GET"
			try: 
				print(contents)
				print(recurso)
				return("200 OK","<html>" + contents[recurso] + "</html>")
			except KeyError:
				return("404 Not Found","<html>Not Found!" + formulario + "</html>")

if __name__=="__main__":
	testWebApp = contentApp("localhost", 1234)
