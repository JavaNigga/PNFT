
import subprocess
import socket

class conexiones():

    def empezarServer(self, ruta):
        print("""        ****************************************************************************
        Entre a: """ + socket.gethostbyname(socket.gethostname()) + ":3000" + 
        """ Para poder acceder a los archivos de este pc...
        Para detener el servidor oprima: CTR+Z
        **************************************************************************** """)
        try:
            subprocess.call("node ./serverSide/server.js", shell=True)
        except:
            print("............")
        input("BYE!")