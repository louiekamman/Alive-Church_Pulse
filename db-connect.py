import mysql.connector

dbconfig = {
    'user': 'pinna_pulseusr', 
    'password': 'nWg71p*9',
    'host': '100.42.50.188', 
    'database': 'pinnacl1_pulse'
}

cnx = mysql.connector.connect(**dbconfig)

curs = cnx.cursor()

curs.execute("SELECT * FROM pulse_categories ORDER BY displayorder")
rslt = curs.fetchall()

for x in rslt:
  print(x)

cnx.close()