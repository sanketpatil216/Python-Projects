from datetime import datetime
from collections import OrderedDict



convert_time  = 0
report_list = list()
count = 0
dictionary = OrderedDict()
report_dict = OrderedDict()
count_list = list()

i = 0
a = 0
with open ('dnslog.txt' , 'r') as text:
  for lines in text:
    line = lines.split()
    
    try: 
      time = datetime.strptime(line[0]+line[1] ,"%Y-%m-%d%H:%M:%S.%f")
      convert_time = ((time.hour * 3600000000 + time.minute * 60000000 + time.second * 1000000  +   time.microsecond )) / 1000
      temp = []
      temp.append(line[7])
      temp.append(convert_time)
      temp.append(time)
      dictionary[a] = temp
      a = a + 1
    except:
      quit


  for l in range (len(dictionary)):
    try:
      web = dictionary.get(i)[0]
      time = dictionary.get(i)[2] 
      report_dict[web] = { "Time" : time , "Blank" : [] , "Count" : 1 }
      header = web
      report_list.append(web)
      prev_time = dictionary.get(i)[1]
      i = i +  1
      new_time = dictionary.get(i)[1]

      while new_time - prev_time < 8000:

        if dictionary.get(i)[0] not in report_list:
          report_dict[header]['Blank'].append(dictionary.get(i)[0])
          report_list.append(dictionary.get(i)[0])

        i = i + 1
        prev_time = new_time
        new_time = dictionary.get(i)[1]

        report_dict[header]['Count'] = len(report_list)
      del report_list[:]

    except:

      continue

file = open('report.txt', 'w')
for l in report_dict:
  count1 = 0
  website = report_dict[l]
  file.write( l + ':' + str(website['Count']) + ' Time: ' + str(website['Time']) + '\n')
  for m in website['Blank']:
    count1 = count1 + 1
    file.write( str(count1) + '.' + m + '\n')
  file.write('\n')
file.close()
