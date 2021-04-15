import glob
from collections import Counter

z = 0
q = 0
attack_list = []
dac = dict()
dec = dict()


def count(num,old):  # Check if previous port number and current number matches
  if old == num:
    return True
  else:
    return False



def no(value):     # check if it is a number
  try:
    if int(value):
      return True
  except:
    return False

log_list = open('report.txt', 'w')  

for folder_files in glob.glob('*.log'):   #read all the log files
  log_list.write(folder_files  + '-->' + '\n\n')

  a_list = []
  dac = dict()
  dec = dict()
  dictionary = {}
  with open(folder_files , 'r') as file:
    for line in file:

      word = line.split(' ')

      try:
        ip_vic = word[4]
        ip_atk = word[2]
        
        victim_port = ip_vic.split('.')[-1][:]
        victim_add = ip_vic.split('.')[0:4]

        attack_port = ip_atk.split('.')[-1][:]

        dec[victim_port] = dec.get(victim_port , 0 ) + 1

        ip_add = ".".join(word[2].split('.')[0:-1])  #remove the port number from ip address
        
        time = word[0]
        temp = []
        # Create a dictionary of all the variables
        
        temp.append(victim_port) 
        temp.append(attack_port)  #port number
        temp.append(time)
        temp.append(ip_add)


        dictionary[z] = temp
        z = z + 1

      except:
        continue



    for m,n in dictionary.items():  

      dac[n[0]] = dac.get(n[0],0)  + 1
      w = n[3]
      if len(dac) == 1000 and n[3] not in a_list :
        
        a_list.append(n[3])

        log_list.write('\t\t\t' + 'Scanned from ' + ' ' + n[3] + ' ' + 'at' + ' ' +  n[2] + '\n\n')

      if len(dac) == 100:

        d = n[3]
        f = n[2]

    if  99 <  len(dec) < 120 and d not in attack_list:


      a_list.append(d)
      log_list.write('\t\t\t' + 'Scanned from ' + ' ' + d + ' ' + 'at' + ' ' +  f + '\n\n')

    if len(dec) > 1030:

      dac.clear()

  dac.clear()

  
log_list.close()
