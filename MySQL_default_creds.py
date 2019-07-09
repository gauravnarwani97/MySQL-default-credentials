import sys
import subprocess
import MySQLdb
import threading
import time

def def_cred():
   """

   A function to get default credentials for db access.
   
   """
   fp = open("default_db_credentials1.txt", "r")
   def_db_val = fp.read()
   fp.close()
   return def_db_val.splitlines()
   
def connect_mysql_ip_port(ip, port, user="", passwd=""):
  """

  A function to connect ip for that port.

  """
  try:
      MySQLdb.connect(host=ip,
                      user=user,
                      passwd=passwd,
                      port=port,
                      connect_timeout=10)
      print (ip, user, passwd)
  except:
      pass

def connect_db(ip, port, db):
   """

   Function to connect MySQL db with default cred

   """
   for row in def_cred():
       user, passwd = row.split(':')
       try:
           t1 = threading.Thread \
                      (target=db,
                       args=(ip, port, \
                             user, \
                             passwd))
           t1.start()
       except:
           print "Failed %s :%s" % (ip, port)
		   
def main(ip, port):
    """

    Start of Script.
    
    """
    success = []
    if port == 3306:
        connect_db(ip, port, connect_mysql_ip_port)

if __name__ == "__main__":
    if len(sys.argv) != 3:
      sys.exit("Usage: python MySQL_default_creds.py ip port")
    main(sys.argv[1], int(sys.argv[2]))
