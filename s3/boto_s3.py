import boto
import sys,os,time
import gzip
import re
from boto.s3.key import Key

local_path = '/home/hadoop/mobodata/ad/s3/'
access_key = 'XXX'
secret_key = 'XXX'

bucket_name = 'log-ad'

conn = boto.connect_s3(access_key,secret_key)

bucket = conn.get_bucket(bucket_name)

bucket_list = bucket.list()


#fp = 'adserver-logs-backup-2014-07-01.tgz'
#fullPath = os.path.join(local_path,fp)
#fh = gzip.GzipFile(fullPath,'r')



def processGzip(fileName,ip):
	if os.path.exists(os.path.join(local_path,ip)):
		os.system('cd ' + ip)
		os.system('tar -kxf  ./' + fileName + ' static*.log -C ./' + ip + '/')
		os.system('cd ..')
	else:
		os.makedirs(os.path.join(local_path,ip))
		os.system('cd ' + ip)
		os.system('tar -kxf  ./' + fileName + ' static*.log -C ./' + ip + '/')
		os.system('cd ..')

	#os.system('tar -xzv -f  ' + fileName + ' ./static*')
        #fileIn = gzip.GzipFile(fileName,'rb')
	#s = fileIn.read()
	#fileIn.close()
	
	#outF = file
	#fname = fileName[:-4]
	#uncom_path = os.path.join(local_path,fname)
	#open(uncom_path,'w').write(fileIn.read())
	#fileIn.close()
        #while True:
        #        line = fileIn.read()
        #        if not line:
        #                break
        #        print line
        #fileIn.close()


#processGzip('adserver-logs-backup-2014-07-01.tgz')

for l in bucket_list:
	keyString = str(l.key)
	fileName = keyString[keyString.rfind('/')+1:]
	dateStr = fileName[fileName.find('2014'):fileName.find('.')]

	pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
	pattern_re = re.compile(pattern)
	ip_address = pattern_re.findall(keyString)
	ip = str(ip_address[0])

	time1 = time.strptime(dateStr,'%Y-%m-%d')
	time2 = time.strptime('2014-07-01','%Y-%m-%d')
	if time1 >= time2:
		print keyString
		print fileName
		print dateStr
		print ip
		if not os.path.exists(os.path.join(local_path,ip)):
			os.makedirs(os.path.join(local_path,ip))

		l.get_contents_to_filename(fileName)
		os.system('tar -kxzv -C ./' + ip + ' -f ' + fileName + ' stat*.log')
		os.system('rm ad*')
		#break

