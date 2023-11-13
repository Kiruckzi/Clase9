from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
import sys



class Ventana1(QMainWindow):

    def __init__(self, parent=None):
        super(Ventana1,self).__init__(parent)

        # Poner el título:
        self.setWindowTitle("Formulario de registro")

        #poner icono
        self.setWindowIcon(QtGui.QIcon('imagenes/img_1.png'))

        self.ancho = 800
        self.alto = 600

        self.resize(self.ancho, self.alto)

        # hacer que la ventana quede en el centro
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())


        # para que la pantalla no se pueda cambiar de tamaño
        self.setFixedHeight(self.alto)
        self.setFixedWidth(self.ancho)

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap('imagenes/img_2.png')

        self.fondo.setPixmap(self.imagenFondo)

        self.fondo.setScaledContents(True)

        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setCentralWidget(self.fondo)

        self.horizontal = QHBoxLayout()

        self.horizontal.setContentsMargins(30,30,30,30)

        self.ladoIzquierdo = QFormLayout()

        self.letrero1 =QLabel()

        self.letrero1.setText("Informacion del cliente")

        self.letrero1.setFont(QFont("arial",20))

        self.letrero1.setStyleSheet("color: #000890")

        self.ladoIzquierdo.addRow(self.letrero1)

        self.horizontal.addLayout(self.ladoIzquierdo)


        self.letrero2 = QLabel()

        self.letrero2.setFixedWidth(340)

        self.letrero2.setText("por favor ingrese la información del cliente"
                              "\nen el formulario de abajo los campos marcados"
                              "\ncon asterico son obligarios.")


        self.letrero2.setFont(QFont("arial",10))

        self.letrero2.setStyleSheet ("color: #000080; margin: 40px "
                                    "margin-top:20px;"
                                     "padding-bottom: 10px;"
                                     "border: 2px solid #000080"
                                     "border-left: none;"
                                     "border-right:none;"
                                     "border-top: none;")

        self.ladoIzquierdo.addRow(self.letrero2)

        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Nombre completo*", self.nombreCompleto)

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("password*", self.password)

        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("password*", self.password2)

        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Documento*", self.documento)


        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)
        self.ladoIzquierdo.addRow("correo*", self.correo)

        self.botonRegistrar = QPushButton("Registrar")

        self.botonRegistrar.setFixedWidth(90)

        self.botonRegistrar.setStyleSheet("background-color: #000845;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        self.botonLimpiar = QPushButton("limpiar")

        self.botonLimpiar.setFixedWidth(90)

        self.botonLimpiar.setStyleSheet("background-color: #000342;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        self.horizontal.addLayout(self.ladoIzquierdo)


        self.ladoDerecho = QFormLayout()

        self.ladoDerecho.setContentsMargins(100,0,0,0)

        self.letrero3 = QLabel()

        self.letrero3.setText("Recuperar contraseña")

        self.letrero3.setFont(QFont("arial",20))

        self.letrero3.setStyleSheet("color:000080")

        self.ladoDerecho.addRow(self.letrero3)

        self.letrero4 = QLabel()

        self.letrero4.setFixedWidth(400)

        self.letrero4.setText("por favor ingrese la información para recuperar"
                              "\nla contraseña.los campos marcados"
                              "\ncon asterico son obligarios.")

        self.letrero4.setFont(QFont("arial",10))


        self.letrero4.setStyleSheet ("color: #000080; margin: 40px "
                                    "margin-top:20px;"
                                     "padding-bottom: 10px;"
                                     "border: 2px solid #000080"
                                     "border-left: none;"
                                     "border-right:none;"
                                     "border-top: none;")

        self.ladoDerecho.addRow(self.letrero4)

        self.labelPregunta1 = QLabel("Pregunta de verificacion 1*")


        self.ladoDerecho.addRow(self.labelPregunta1)

        self.pregunta1 = QLineEdit()

        self.pregunta1.setFixedWidth(320)


        self.ladoDerecho.addRow(self.pregunta1)


        self.labelRespuesta1 = QLabel("Respuesta de verificacion 1*")

        self.ladoDerecho.addRow(self.labelRespuesta1)

        self.respuesta1 = QLineEdit()

        self.respuesta1.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta1)

       #pregunta 2
        self.labelPregunta2 = QLabel("Pregunta de verificacion 2*")

        self.ladoDerecho.addRow(self.labelPregunta2)

        self.pregunta2 = QLineEdit()

        self.pregunta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta2)

        self.labelRespuesta2 = QLabel("Respuesta de verificacion 2*")

        self.ladoDerecho.addRow(self.labelRespuesta2)

        self.respuesta2 = QLineEdit()

        self.respuesta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta2)

        #PREGUNTA 3

        self.labelPregunta3 = QLabel("Pregunta de verificacion 3*")

        self.ladoDerecho.addRow(self.labelPregunta3)

        self.pregunta3 = QLineEdit()

        self.pregunta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta3)

        self.labelRespuesta3 = QLabel("Respuesta de verificacion 3*")

        self.ladoDerecho.addRow(self.labelRespuesta3)

        self.respuesta3 = QLineEdit()

        self.respuesta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta3)

        self.botonBuscar = QPushButton("Buscar")

        self.botonBuscar.setFixedWidth(90)

        self.botonBuscar.setStyleSheet("color: #000080; margin: 40px "
                                       "margin-top:20px;"
                                        "padding: 10px;"
                                       "background-color: #000845;")

        self.botonRecuperar = QPushButton("Recuperar")

        self.botonRecuperar.setFixedWidth(90)

        self.botonRecuperar.setStyleSheet("color: #000080; margin: 40px "
                                       "margin-top:20px;"
                                        "padding: 10px;"
                                       "background-color: #000845;")

        self.ladoDerecho.addRow(self.botonBuscar, self.botonRecuperar)




        self.horizontal.addLayout(self.ladoDerecho)




        #PONER AL FINAL

        self.fondo.setLayout(self.horizontal)

    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.password.setText('')
        self.password2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')





    def accion_botonRegistrar(self):
        self.ventanaDialogo = QDialog(None,QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        self.ventanaDialogo.resize(300,150)

        #Boton para aceptar
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accepted)

        self.ventanaDialogo.setWindowTitle("Formulario de registro")

        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        self.vertical = QVBoxLayout()

        self.mensaje = QLabel("")

        self.mensaje.setStyleSheet("background-color: #000845; color:#FFFFFF; padding: 10px;")

        self.vertical.addWidget(self.mensaje)

        self.vertical.addWidget(self.opciones)

        self.ventanaDialogo.setLayout(self.vertical)

        self.datosCorrectos = True


        if(

             self.password.text() != self.password2.text()
        ):

            self.datosCorrectos = False
            self.mensaje.setText("Los passwords no son iguales")
            self.ventanaDialogo.exec_()


        if(
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.password2.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Debe ingresar todos los campos")

            self.ventanaDialogo.exec_()

        if self.datosCorrectos:

                self.file = open('datos/clientes.txt', 'ab')
                # Trae el texto de los qline edits
                self.file.write(bytes(
                    self.nombreCompleto.text() + ";"
                    + self.usuario.text() + ";"
                    + self.password.text() + ";"
                    + self.password2.text() + ";"
                    + self.documento.text() + ";"
                    + self.correo.text() + ";"
                    + self.pregunta1.text() + ";"
                    + self.respuesta1.text() + ";"
                    + self.pregunta2.text() + ";"
                    + self.respuesta2.text() + ";"
                    + self.pregunta3.text() + ";"
                    + self.respuesta3.text() + "\n"
                    , encoding='UTF-8'))

                self.file.close()

                self.file = open('datos/clientes.txt', 'rb')
                while self.file:
                    linea = self.file.readline().decode('UTF-8')
                    print(linea)
                    if linea == '':
                        break
                self.file.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana1 =  Ventana1 ()
    ventana1.show()
    sys.exit(app.exec_())

