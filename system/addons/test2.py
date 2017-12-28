from pdfgen import *
from printFormat import *

dataNS = {
	#folio
	"folio": "3267788",
	#linea 1
	"RazonSocial":"Albin Trotter E.",
	"cod_operador":"EXCENTA",
	#linea 2
	"direccionns":"Camino el Alba 9437",
	"comuna":"Las Condes",
	"ciudad":"Santiago",
	"codlegal":"15644464-2",
	#linea 3
	"fonocliente":"965881118",
	"movil":"978862666",
	"giro":"PARTICULAR",
	#linea 4
	"email":"albin.trotter@gmail.com",
	"contacto":"Teresa Cruz F.",
	#linea 5
	"artefacto":"Calefon ATDV 13 L GL",
	"modelo":"Merlin",
	"combustible":"GN",
	#linea 6
	"serie":"999888222",
	"fecha_compra":"08-09-2016",
	"factura":"99887766",
	"distribuidor":"Sodimac",
	#linea 7
	"tipo":"GAS",
	"concesionario":"Testo de la Test",
	"NUMERO_guia": "1065324534",
	#linea 8
	"certificado":"00-00-11-00-11123",
	"cod_tecnico":"Antonio Golzio",
	#observaciones
	"obs":"Favor llamar dos horas antes de asistir al domicilio, para poder partir antes de la oficina. Ademas para coordinar con los maestros de pintura y los ceramistas. Los tecnicos debe ir preparados para lidiar con aranas y ratas, puede que algun reptil clase 3 los cuales pueden ser perjudiciales a la salud."
}

for k,d in dataNS.iteritems():
	print k
	print repr(formatNS[k])

test = pdfGenerator("/usr/local/sacservices/test.pdf")

test.genFormat(dataNS, formatNS)
test.save()