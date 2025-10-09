import subprocess as sp


def prompt_install_tabulate():
	ans=input("Install LSPORT additional features [Y/n]")
	if ans.lower()!='n':
		print('Installation begins...')
		resp = sp.run(['pip3', 'install','tabulate'])
		if resp.returncode==0:
			print('Installation Successfull')
			return True
			
		else:
			print('Installation Unsuccessful. Continueing without enhancment')
			return False
	else:
		print('Continueing without enhancment')
		return False
		

try:
	from tabulate import tabulate
	table=True
except:
	if prompt_install_tabulate():
		from tabulate import tabulate
		table=True
	else:
		table=False

pipe = sp.Popen("ls -l /dev/serial/by-id/ | awk '{print $9 \" \" $11}'",shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
res = pipe.communicate()


ports=res[0].decode(encoding='utf-8').strip()

data= []

if ports=="":
	ports=[]
else:
	ports=ports.split("\n")

if not table:
	print("Device Name \t Port")
	print("----------- \t ---------")

for port in ports:
	port=port.split()
	if not table:
		print(port[0],"\t ->  ",port[1].replace("../..","/dev"))
	data.append([port[0],port[1].replace("../..","/dev")])

print()
if table:
	print (tabulate(data, headers=["Device Name", "Port"]))
print()
print(f"{len(ports)} Devices Found\n")

print("If you don't see your device here, Then run lsusb -t to find the driver is install or not.")


