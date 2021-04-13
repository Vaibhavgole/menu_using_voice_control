import os 
import speech_recognition as sr
import pyttsx3 as pt
import subprocess
import getpass as gp
import sys

def get_input_speech(message):
    r = sr.Recognizer()
    devnull = os.open(os.devnull, os.O_WRONLY)
    old_stderr = os.dup(2)
    sys.stderr.flush()
    os.dup2(devnull, 2)
    os.close(devnull)
    with sr.Microphone() as target:
        print(message)
        x = r.listen(target,timeout=4,phrase_time_limit=5)
    a = r.recognize_google(x,language="en-in")
    return a

def speak(text):
      engine.say(text)
      engine.runAndWait()

engine= pt.init()
voices= engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)
engine.setProperty('rate' , 150)


os.system("tput setaf 1")
print("\t\t\t\tWelcome to Automate")
pt.speak("Welcome to Automate")
os.system("tput setaf 7")
print("\t\t\t------------------------")
print("Enter the password")
pt.speak("Enter Your password Please")
userpaswd = gp.getpass()
paswd = "menu"
if userpaswd != paswd:
    print("Incorrect Password Please Try Again!!")
    pt.speak("Incorrect Password Please Try Again!!")
    exit()
pt.speak("Choose remote or local system")
loginto=get_input_speech("choose login to local/remote system : ")

print(loginto)
if loginto=="local":
    pt.speak("Logging to local system")
else:
    pt.speak("Logging to remote system")

if loginto=="remote":
    remoteip=get_input_speech("Enter the Remote system Ip: ")
    pt.speak("Please enter remote system IP Address")
os.system("clear")
def printmenu():
    pt.speak("Here's the list what you can do")
    print("""
              1: Date                           17: Configure AWS Linux    
              2: Calender                       18: Login to AWS 
              3: Configure Webserver            19: Create Key pair 
              4: Create file                    20: Create Security group
              5: Create Directory               21: Add Ingress(Inbound) Rule
              6: Add User                       22: Launch Instance
              7: Start Any Service U Want       23: Create Ebs Volume
              8: Stop Service U Want            24: Attach Ebs to Instance
              9: Start Python3                  25: Create S3 bucket
             10: Configure Docker               26: Upload object on bucket
             11: Start Docker Services          27: Create LVM Partition
             12: Stop Docker Services           28: Configure System as Hadoop NameNode
             13: Restart Docker Services        29: Configure System as Hadoop DataNode
             14: Login into Docker              30: Static Partition
             15: Pull Docker Image              31: Exit
             16: Launch Docker Container
            """)
def lvm(pvname,vgname,lvsize,lvname,filesystem,mount_lvm):
    os.system("df -h")
    os.system("fdisk -l")
    os.system("pvcreate {}".format(pvname))
    pt.speak("physical volume created successfully")
    os.system("vgcreate {} {}".format(vgname,pvname))
    os.system("vgs")
    pt.speak("volume group created successfully")
    os.system("lvcreate -L {} -n {} {}".format(lvsize,lvname,vgname))
    os.system("lvs")
    pt.speak("logical volume created successfully")
    os.system("lsblk")
    os.system("mkfs.{} /dev/{}/{}".format(filesystem,vgname,lvname))
    pt.speak("Format successfull")
    os.system("mount /dev/{}/{} {}".format(vgname,lvname,mount_lvm))
    pt.speak("Mounted successfully")
    os.system("df -h")
    os.system("lsblk")
    return
def lvmremote(pvname,vgname,lvsize,lvname,filesystem,mount_lvm):
    pt.speak("Are you doing lvm on Aws yes or no")
    keyyesno=get_input_speech("Are you doing lvm on Aws(yes/no): ")
    if keyyesno=="yes":
        pt.speak("Enter the Aws key path format of key should be .pem")
        keypath=get_input_speech("Enter the Aws key path(format of key should be .pem): ")
        pt.speak("Enter the User Name of Aws instance")
        awsuser=get_input_speech("Enter the User Name of Aws instance: ")
        os.system("chmod go= {}".format(keypath))
        os.system("ssh -i {} {}@{}  yum install fdisk --nobest -y".format(keypath,awsuser,remoteip))
        os.system("ssh -i {} {}@{}  yum install lvm --nobest -y".format(keypath,awsuser,remoteip))
        os.system("ssh -i {} {}@{}  df -h".format(keypath,awsuser,remoteip))
        os.system("ssh -i {} {}@{}  fdisk -l".format(keypath,awsuser,remoteip))
        os.system("ssh -i {} {}@{}  pvcreate {}".format(keypath,awsuser,remoteip,pvname))
        pt.speak("physical volume created successfully")
        os.system("ssh -i {} {}@{}  vgcreate {} {}".format(keypath,awsuser,remoteip,vgname,pvname))
        os.system("ssh -i {} {}@{}  vgs".format(keypath,awsuser,remoteip))
        pt.speak("volume group created successfully")
        os.system("ssh -i {} {}@{}  lvcreate -L {} -n {} {}".format(keypath,awsuser,remoteip,lvsize,lvname,vgname))
        os.system("ssh -i {} {}@{}  lvs".format(keypath,awsuser,remoteip))
        pt.speak("logical volume created successfully")
        os.system("ssh -i {} {}@{}  lsblk".format(keypath,awsuser,remoteip))
        os.system("ssh -i {} {}@{}  mkfs.{} /dev/{}/{}".format(keypath,awsuser,remoteip,filesystem,vgname,lvname))
        os.system("ssh -i {} {}@{}  mount /dev/{}/{} {}".format(keypath,awsuser,remoteip,vgname,lvname,mount_lvm))
        pt.speak("Mounted successfully")
        os.system("ssh -i {} {}@{}  df -h".format(keypath,awsuser,remoteip))
        os.system("ssh -i {} {}@{}  lsblk".format(keypath,awsuser,remoteip))
    else:
        os.system("ssh  {}  df -h".format(remoteip))
        os.system("ssh  {}  fdisk -l".format(remoteip))
        os.system("ssh  {}  pvcreate {}".format(remoteip,pvname))
        pt.speak("physical volume created successfully")
        os.system("ssh  {}  vgcreate {} {}".format(remoteip,vgname,pvname))
        os.system("ssh  {}  vgs".format(remoteip))
        pt.speak("volume group created successfully")        
        os.system("ssh  {}  lvcreate -L {} -n {} {}".format(remoteip,lvsize,lvname,vgname))
        os.system("ssh  {}  lvs".format(remoteip))
        pt.speak("logical volume created successfully")        
        os.system("ssh  {}  lsblk".format(remoteip))
        os.system("ssh  {}  mkfs.{} /dev/{}/{}".format(remoteip,filesystem,vgname,lvname))
        os.system("ssh  {}  mount /dev/{}/{} {}".format(remoteip,vgname,lvname,mount_lvm))
        os.system("ssh  {}  df -h".format(remoteip))
        pt.speak("mounted successfully")        
        os.system("ssh  {}  lsblk".format(remoteip))
    return
def checkJava():
    pt.speak("checking Java")
    r = os.system("java -version")
    if r != 0:
        pt.speak("Java is not installed in your system")
        print("Java is not installed in your system....")
        return 0
    else:
        return 1
def checkHadoop():
    pt.speak("Checking Hadoop")
    r = os.system("hadoop -v")
    if r != 0:
        pt.speak("hadoop is not installed in your system")
        print("hadoop is not installed in your system....")
        return 0
    else:
        return 1
def updateHdfsSite():
    pt.speak("Starting hdfssite file configuration")
    filename="/etc/hadoop/hdfs-site.xml"
    f = open(filename,'r')
    file_lines=list(f.readlines())
    offset = len(file_lines) - 1
    if file_lines[offset-1] == "</property>\n":
        pt.speak("hdfs-site is already configured")
        print("hdfs-site is already configured.........\n")
        pt.speak("checking core-site.xml")
        print("checking core-site.xml.........")
        return
    pt.speak("Create folder for namenode enter path")    
    folder = get_input_speech("Create folder for namenode(enter path): ")
    string = "<property>\n<name>dfs.name.dir</name>\n<value>{}</value>\n</property>\n".format(folder)
    file_lines.insert(offset, string)
    print(file_lines)
    f.close()
    f = open(filename,'w+')
    for i in range(len(file_lines)):
        f.write(file_lines[i])
    f.close()
    pt.speak("configuration success")
def updateCoreSite():
    pt.speak("starting coresite file configuration")
    filename="/etc/hadoop/core-site.xml"

    f = open(filename,'r')
    file_lines=list(f.readlines())
    offset = len(file_lines) - 1
    if file_lines[offset-1] == "</property>\n":
        pt.speak("core-site.xml is already configured")
        print("core-site.xml is already configured.........")
        return
    string = "<property>\n<name>fs.default.name</name>\n<value>hdfs://0.0.0.0:9001</value>\n</property>\n"
    file_lines.insert(offset, string)
    print(file_lines)
    f.close()
    f = open(filename,'w+')
    for i in range(len(file_lines)):
        f.write(file_lines[i])
    f.close()
    pt.speak("Configuration success")
def checkNameNodeStatus():
    pt.speak("Checking namenode status")
    sub = subprocess.Popen("jps", shell=True, stdout=subprocess.PIPE)
    output = sub.stdout.read()
    if 'NameNode' in str(output):
        return 1
    else:
        return 0
def UpdateHdfsSite():
    pt.speak("Starting update of hdfs file")
    filename="/etc/hadoop/hdfs-site.xml"
    f = open(filename,'r')
    file_lines=list(f.readlines())
    offset = len(file_lines) - 1
    if file_lines[offset-1] == "</property>\n":
        pt.speak("hdfs-site is already configured")
        print("hdfs-site is already configured.........\n")
        pt.speak("checking core-site.xml")
        print("checking core-site.xml.........")
        return
    pt.speak("Create folder for datanode enter path")
    folder = get_input_speech("Create folder for datanode(enter path): ")
    string = "<property>\n<name>dfs.data.dir</name>\n<value>{}</value>\n</property>\n".format(folder)
    file_lines.insert(offset, string)
    print(file_lines)
    f.close()

    f = open(filename,'w+')
    for i in range(len(file_lines)):
        f.write(file_lines[i])
    f.close()
    pt.speak("Update successful")
def UpdateCoreSite():
    pt.speak("starting update coresite")
    filename="/etc/hadoop/core-site.xml"

    f = open(filename,'r')
    file_lines=list(f.readlines())
    offset = len(file_lines) - 1
    if file_lines[offset-1] == "</property>\n":
        pt.speak("core-site.xml is already configured")
        print("core-site.xml is already configured.........")
        return
    pt.speak("Enter ip of namenode")
    ip = get_input_speech("Enter ip of namenode: ")
    string = "<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n".format(ip)
    file_lines.insert(offset, string)
    print(file_lines)
    f.close()

    f = open(filename,'w+')
    for i in range(len(file_lines)):
        f.write(file_lines[i])
    f.close()
    pt.speak("Update successful")
def CheckDataNodeStatus():
    pt.speak("checking datanode status")
    sub = subprocess.Popen("jps", shell=True, stdout=subprocess.PIPE)
    output = sub.stdout.read()
    if 'DataNode' in str(output):
        return 1
    else:
        return 0
while True:  
      
    if loginto=="local":
        printmenu()
        pt.speak("Enter your choice")
        ch=int(get_input_speech("Enter your Choice:  "))
        if   ch==1:
            pt.speak("watch the date output on screen")
            os.system("date")
            
        elif ch==2:
            pt.speak("watch the calendar output on screen")
            os.system("cal")
        elif ch==3:
            pt.speak("installing httpd")
            os.system("yum install httpd")
            pt.speak("starting the httpd service")
            os.system("systemctl start httpd")
            pt.speak("enabling httpd service")
            os.system("systemctl enable httpd")
            pt.speak("Watch out for httpd status")
            os.system("systemctl status httpd")
        elif ch==4:
            pt.speak("Please enter filename")
            File_name=get_input_speech("Enter File Name: ")
            os.system("touch {}".format(File_name))
            pt.speak("File created successfully")
        elif ch==5:
            pt.speak("Enter directory name")
            Dir_name=get_input_speech("Enter directory Name: ")
            os.system("mkdir {}".format(Dir_name))
            pt.speak("Directory created successfully")
        elif ch==6:
            pt.speak("Enter the user name")
            User_name=get_input_speech("Enter the username please: ")
            os.system("useradd {}".format(User_name))
            pt.speak("User added sucessfully")
        elif ch==7:
            pt.speak("Please enter which service you want to start")
            Serv_start=get_input_speech("Enter the Service which you want to start it: ")
            os.system("systemctl start {}".format(Serv_start))
            pt.speak("service started successfully")
        elif ch==8:
            pt.speak("Please enter which service you want to stop")
            Serv_stop=get_input_speech("Enter the Service which you want to Stop it: ")
            os.system("systemctl stop {}".format(Serv_stop))
            pt.speak("service stopped successfully")
        elif ch==9:
            pt.speak("Launching python console write exit() to exit the console")
            os.system("python3")
        elif ch==10:
            pt.speak("creating the docker repository")
            os.system("wget https://raw.githubusercontent.com/abhijeetdebe/DockerRepo/main/docker.repo -P /etc/yum.repos.d/")
            pt.speak("installing docker")
            os.system("yum install docker-ce --nobest -y")
            pt.speak("starting docker service")
            os.system("systemctl start docker")
        elif ch==11:
            pt.speak("starting docker service")
            os.system("systemctl start docker")   
        elif ch==12:
            pt.speak("stopping docker service")
            os.system("systemctl stop docker")   
        elif ch==13:
            pt.speak("restarting docker service")
            os.system("systemctl restart docker")
        elif ch==14:
            pt.speak("Enter your username")
            username=get_input_speech("Enter Username: ")
            pt.speak("Enter your password")
            password=get_input_speech("Enter Your Password: ")
            pt.speak("Logging to dockerhub")
            os.system("docker login --username {} --password {}".format(username,password))
        elif ch==15:
            pt.speak("Enter Image name and version to be Pulled")
            Doc_img=get_input_speech("Enter Image name and version to be Pulled(example ubuntu:14.02): ")
            pt.speak("pulling image")
            os.system("docker pull {}".format(Doc_img))
        elif ch==16:
            pt.speak("Enter the container name")
            containername=get_input_speech("Enter the Container Name: ")
            pt.speak("Please enter the docker image name to use")
            doc_img=get_input_speech("Enter the docker image name and version to launch Container: ")
            os.system("docker run -it --name {} {}".format(containername,doc_img))
        elif ch==17:
            pt.speak("downloading aws cli")
            os.system("curl ""https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip"" -o ""awscliv2.zip""")
            pt.speak("Unzipping the file")
            os.system("unzip awscliv2.zip")
            pt.speak("installing aws cli in your system")
            os.system("sudo ./aws/install")
        elif ch==18:
            pt.speak("Please Enter the Access Key, Security Key and Region Name")
            print("Please Enter the Access Key, Security Key and Region Name")
            print("Wait for Prompt to Come Up")
            os.system("aws configure")
        elif ch==19:
            pt.speak("Enter the key pair name")
            Keyname=get_input_speech("Enter the key Name: ")
            pt.speak("creating key pair")
            os.system("aws ec2 create-key-pair  --key-name {}".format(Keyname))
        elif ch==20:
            pt.speak("Enter the security group name")
            SGname=get_input_speech("Enter the Security Name: ")
            pt.speak("Enter the VPC ID")
            Vpcid=get_input_speech("Enter the VPC ID: ")
            pt.speak("Enter description in double quotes")
            desc=get_input_speech("Enter description in double quotes: ")
            pt.speak("Creating security group")
            os.system("aws ec2 create-security-group --group-name {} --description {}  --vpc-id {}".format(SGname,desc,Vpcid))
        elif ch==21:
            pt.speak("Enter Security Group ID")
            sgid=get_input_speech("Enter the Security Group ID: ")
            pt.speak("Enter the protocol name or if you want all then enter all")
            protocol=get_input_speech("Enter the protocol name or if you want all then enter all: ")
            pt.speak("Enter the CIDR")
            cidr=get_input_speech("Enter the CIDR(Example : 0.0.0.0/0): ")
            if protocol== "all" :
                os.system("aws ec2 authorize-security-group-ingress --group-id {} --protocol all --cidr {}".format(sgid,cidr))
                pt.speak("Ingress Rule added succesfully")
            else:
                pt.speak("Enter the port number")
                port=get_input_speech("Enter the port number: ")
                os.system("aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}".format(sgid,protocol,port,cidr))
                pt.speak("Ingress Rule added succesfully")
        elif ch==22:
            pt.speak("Enter the AMI ID")
            amid=get_input_speech("Enter the AMI ID: ")
            pt.speak("Enter the Instance type")
            insttype=get_input_speech("Enter the Instance type: ")
            pt.speak("Enter the number of the instance you want to launch")
            cnt=get_input_speech("Enter the number of the instance you want to launch: ")
            pt.speak("Enter the Subnet ID")
            subid=get_input_speech("Enter the Subnet ID: ")
            pt.speak("Enter the key name")
            key=get_input_speech("Enter the key name: ")
            pt.speak("Enter the security group id")
            sg=get_input_speech("Enter the security group id: ")
            os.system("aws ec2 run-instances  --image-id {} --instance-type {}  --count {} --subnet-id {} --key-name {} --security-group-ids {} ".format(amid,insttype,cnt,subid,key,sg))
            pt.speak("Instance launched successfully")
        elif ch==23:
            pt.speak("Enter the Volume type(example")
            voltype=get_input_speech("Enter the Volume type(example: gp2): ")
            pt.speak("Enter the Volume Size")
            size=get_input_speech("Enter the Volume Size: ")
            pt.speak("Enter the Availability Zone")
            zone=get_input_speech("Enter the Availability Zone(example: us-west-1c): ")
            os.system("aws ec2 create-volume --volume-type {} --size {} --availability-zone {}".format(voltype,size,zone))
            pt.speak("Volume created successfully")
        elif ch==24:
            pt.speak("Enter the Volume ID")
            volid=get_input_speech("Enter the Volume ID: ")
            pt.speak("Enter the Instance ID")
            instid=get_input_speech("Enter the Instance ID: ")
            pt.speak("Enter the device name")
            dev=get_input_speech("Enter the device name(example: /dev/sdf): ")
            os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device {}".format(volid,instid,dev))
            pt.speak("Volume attached to the instance successfully")
        elif ch==25:
            pt.speak("Enter the Bucket Name")
            buckname=get_input_speech("Enter the Bucket Name: ")
            pt.speak("Enter the Region ID")
            region=get_input_speech("Enter the Region ID(example: us-west-1): ")
            os.system("aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={} ".format(buckname,region,region))
            pt.speak("Bucket created successfully")
        elif ch==26:
            pt.speak("Enter the Object local path")  
            source=get_input_speech("Enter the Object local path: ")
            pt.speak("Enter the bucket path")
            dest=get_input_speech("Enter the bucket path(example s3://bucketname): ")
            os.system("aws s3 cp {} {}".format(source,dest))
            pt.speak("Object added successfully")
        elif ch==27:
            pt.speak("Enter the Physical Volume Device Name")
            pvname=get_input_speech("Enter the Physical Volume Device Name(example: /dev/sdb): ")
            pt.speak("Enter the Volume Group Name")
            vgname=get_input_speech("Enter the Volume Group Name: ")
            pt.speak("Enter the Size of LV")
            lvsize=get_input_speech("Enter the Size of LV(example: 5G): ")
            pt.speak("Enter the Logical Volume Name")
            lvname=get_input_speech("Enter the Logical Volume Name: ")
            pt.speak("Enter the File system")
            filesystem=get_input_speech("Enter the File system(example: xfs,ext4): ")
            pt.speak("Enter the path of Existing directory to mount to LVM")
            mount_lvm=get_input_speech("Enter the path of Existing directory to mount to LVM: ")
            lvm(pvname,vgname,lvsize,lvname,filesystem,mount_lvm)
            pt.speak("LVM successfully created")
        elif ch==28:
            if checkJava:
                if checkHadoop: 
                    updateHdfsSite()
                    updateCoreSite()
                    if not checkNameNodeStatus():
                        pt.speak("Starting namenode")
                        print("Starting NameNode..............")
                        os.system("hadoop namenode -format -force")
                        os.system("hadoop-daemon.sh start namenode")
                        pt.speak("Namenode started")
                    else:
                        pt.speak("Service already running")
                        print("Service running already.....")
        elif ch==29:
            if checkJava :
                if checkHadoop :
                    UpdateHdfsSite()
                    UpdateCoreSite()
                    if not CheckDataNodeStatus():
                        pt.speak("Starting datanode")
                        print("Starting DataNode..............")
                        os.system("hadoop-daemon.sh start datanode")
                        pt.speak("Datanode started")
                    else:
                        pt.speak("Service already running")
                        print("Service running already.....")
        elif ch==30:
            pt.speak("To create partition Press 1 or remove partition Press 2")
            c=int(get_input_speech("Do you want to create(Press 1) or remove(Press 2) partition"))
            os.system("fdisk -l")
            if int(c)==1 :
                pt.speak("Enter the Device Name")
                diskname=get_input_speech("Enter the Device Name")
                os.system("fdisk -s /dev/{}".format(diskname))
                pt.speak("enter the partition size")
                partsize=get_input_speech("enter the partition size")
                pt.speak("Give the file name where you want to mount the harddisk")
                f_name=get_input_speech("Give the file name where you want to mount the harddisk")
                os.system("fdisk /dev/{}".format(diskname))
                os.system("echo n | fdisk /dev/{}".format(diskname))
                os.system("echo p | fdisk /dev/{}".format(diskname))
                os.system("echo \n | fdisk /dev/{}".format(diskname))
                os.system("echo +{}G | fdisk /dev/{}".format(partsize,diskname))
                os.system("echo w | fdisk /dev/{}".format(diskname))
                os.system("echo q | fdisk /dev/{}".format(diskname))
                os.system("mkfs.ext4 /dev/{}".format(diskname))
                os.system("mkdir /{}".format(f_name))
                os.system("mount /dev/{}  /{}".format(diskname,f_name))
                pt.speak("Successfully created and mounted the partition")
            elif int(c)==2 :
                os.system("fdisk /dev/{}".format(diskname))
                os.system("echo d | fdisk /dev/{}".format(diskname))
                os.system("echo w | fdisk /dev/{}".format(diskname))
                os.system("echo q | fdisk /dev/{}".format(diskname))
                pt.speak("partition Removed successfully")
        elif ch==31:
            print("Have a Nice Day")
            pt.speak("Have a Nice Day")
            exit()
        else:
            pt.speak("Enter the Right Choice")
            print("Enter the Rigth Choice")
        pt.speak("Press Enter to Continue")
        get_input_speech("Press Enter to continue")
        os.system("clear")
    elif loginto=="remote":
        printmenu()
        ch=int(get_input_speech("Enter your Choice:  "))
        if   ch==1:
            os.system("ssh {} date".format(remoteip))
        if ch==2:
            os.system("ssh {} cal".format(remoteip))
        if ch==3:
            os.system("ssh {} yum install httpd".format(remoteip))
            os.system("ssh {} systemctl start httpd".format(remoteip))
            os.system("ssh {} systemctl enable httpd".format(remoteip))
            os.system("ssh {} systemctl status httpd".format(remoteip))
        if ch==4:
            File_name=get_input_speech("Enter File Name: ")
            os.system("ssh {} touch {}".format(remoteip,File_name))
        if ch==5:
            Dir_name=get_input_speech("Enter directory Name: ")
            os.system("ssh {} mkdir {}".format(remoteip,Dir_name))
        if ch==6:
            User_name=get_input_speech("Enter the username please: ")
            os.system("ssh {} useradd {}".format(remoteip,User_name))
        if ch==7:
            Serv_start=get_input_speech("Enter the Service which you want to start it: ")
            os.system("ssh {} systemctl start {}".format(remoteip,Serv_start))
        if ch==8:
            Serv_stop=get_input_speech("Enter the Service which you want to Stop it: ")
            os.system("ssh {} systemctl stop {}".format(remoteip,Serv_stop))
        elif ch==9:
            os.system("python3")
        if ch==10:
            os.system("sudo cd /etc/yum.repos.d/ && wget https://raw.githubusercontent.com/abhijeetdebe/DockerRepo/main/docker.repo")
            os.system("ssh {} yum install docker --nobest -y".format(remoteip))
            os.system("ssh {} systemctl start docker".format(remoteip))
        if ch==11:
            os.system("ssh {} systemctl start docker".format(remoteip))   
        if ch==12:
            os.system("ssh {} systemctl stop docker".format(remoteip))   
        if ch==13:
            os.system("ssh {} systemctl restart docker".format(remoteip))
        if ch==14:
            username=get_input_speech("Enter Username: ")
            useremail=get_input_speech("Enter Email Address: ")
            os.system("ssh {} docker login --username={} --email={}".format(remoteip,username,useremail))
        if ch==15:
            Doc_img=get_input_speech("Enter Image name and version to be Pulled(example ubuntu:14.02): ")
            os.system("ssh {} docker pull {}".format(remoteip,Doc_img))
        if ch==16:
            containername=get_input_speech("Enter the Container Name: ")
            doc_img=get_input_speech("Enter the docker image name and version to launch Container: ")
            os.system("ssh {} docker run -it --name {} {}".format(remoteip,containername,doc_img))
        if ch==17:
            os.system("ssh {} curl ""https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip"" -o ""awscliv2.zip""".format(remoteip))
            os.system("ssh {} unzip awscliv2.zip".format(remoteip))
            os.system("ssh {} sudo ./aws/install".format(remoteip))
        if ch==18:
            print("Please Enter the Access Key, Security Key and Region Name")
            print("Wait for Prompt to Come Up")
            os.system("ssh {} aws configure".format(remoteip))
        if ch==19:
            Keyname=get_input_speech("Enter the key Name: ")
            os.system("ssh {} aws ec2 create-key-pair  --key-name {}".format(remoteip,Keyname))
        if ch==20:
            SGname=get_input_speech("Enter the Security Name: ")
            Vpcid=get_input_speech("Enter the VPC ID: ")
            desc=get_input_speech("Enter description in double quotes: ")
            os.system("ssh {} aws ec2 create-security-group --group-name {} --description {}  --vpc-id {}".format(remoteip,SGname,desc,Vpcid))
        if ch==21:
            sgid=get_input_speech("Enter the Security Group ID: ")
            protocol=get_input_speech("Enter the protocol name or if you want all then enter all: ")
            cidr=get_input_speech("Enter the CIDR(Example : 0.0.0.0/0): ")
            if protocol== "all" :
                os.system("ssh {} aws ec2 authorize-security-group-ingress --group-id {} --protocol all --cidr {}".format(remoteip,sgid,cidr))
            else:
                port=get_input_speech("Enter the port number: ")
                os.system("ssh {} aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}".format(remoteip,sgid,protocol,port,cidr))
        if ch==22:
            amid=get_input_speech("Enter the AMI ID: ")
            insttype=get_input_speech("Enter th Instance type: ")
            cnt=get_input_speech("Enter the number of the instance you want to launch: ")
            subid=get_input_speech("Enter the Subnet ID: ")
            key=get_input_speech("Enter the key name: ")
            sg=get_input_speech("Enter the security group id: ")
            os.system("ssh {} aws ec2 run-instances  --image-id {} --instance-type {}  --count {} --subnet-id {} --key-name {} --security-group-ids {} ".format(remoteip,amid,insttype,cnt,subid,key,sg))
        if ch==23:
            voltype=get_input_speech("Enter the Volume type(example: gp2): ")
            size=get_input_speech("Enter the Volume Size: ")
            zone=get_input_speech("Enter the Availability Zone(example: us-west-1c): ")
            os.system("ssh {} aws ec2 create-volume --volume-type {} --size {} --availability-zone {}".format(remoteip,voltype,size,zone))
        if ch==24:
            volid=get_input_speech("Enter the Volume ID: ")
            instid=get_input_speech("Enter the Instance ID: ")
            dev=get_input_speech("Enter the device name(example: /dev/sdf): ")
            os.system("ssh {} aws ec2 attach-volume --volume-id {} --instance-id {} --device {}".format(remoteip,volid,instid,dev))
        if ch==25:
            buckname=get_input_speech("Enter the Bucket Name: ")
            region=get_input_speech("Enter the Region ID(example: us-west-1): ")
            os.system("ssh {} aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}".format(remoteip,buckname,region,region))
        if ch==26:
            source=get_input_speech("Enter the Object local path: ")
            dest=get_input_speech("Enter the bucket path(example s3://bucketname): ")
            os.system("ssh {} aws s3 cp {} {}".format(remoteip,source,dest))
        if ch==27:
            pvname=get_input_speech("Enter the Physical Volume Device Name(example: /dev/sdb): ")
            vgname=get_input_speech("Enter the Volume Group Name: ")
            lvsize=get_input_speech("Enter the Size of LV(example: 5G): ")
            lvname=get_input_speech("Enter the Logical Volume Name: ")
            filesystem=get_input_speech("Enter the File system(example: xfs,ext4): ")
            mount_lvm=get_input_speech("Enter the path of Existing directory to mount to LVM: ")
            lvmremote(pvname,vgname,lvsize,lvname,filesystem,mount_lvm)
        if ch==28:
            print("Working on Hadoop NameNode Remote")
        if ch==29:
            print("Working on Hadoop Datanode Remote")
        if ch==30:
            c=int(get_input_speech("Do you want to create(Press 1) or remove(Press 2) partition"))
            os.system("fdisk -l")
            if int(c)==1 :
                diskname=get_input_speech("Enter the Device Name")
                os.system("ssh {} fdisk -s /dev/{}".format(remoteip,diskname))
                partsize=get_input_speech("enter the partition size")
                f_name=get_input_speech("Give the file name where you want to mount the harddisk")
                os.system("ssh {} fdisk /dev/{}".format(remoteip,diskname))
                os.system("ssh {} echo n | fdisk /dev/{}".format(remoteip,diskname))
                os.system("ssh {} echo p | fdisk /dev/{}".format(remoteip,diskname))
                os.system("ssh {} echo \n | fdisk /dev/{}".format(remoteip,diskname))
                os.system("ssh {} echo +{}G | fdisk /dev/{}".format(remoteip,partsize,diskname))
                os.system("ssh {} echo w | fdisk /dev/{}".format(remoteip,diskname))
                os.system("ssh {} echo q | fdisk /dev/{}".format(remoteip,diskname))
                os.system("ssh {} mkfs.ext4 /dev/{}".format(remoteip,diskname))
                os.system("ssh {} mkdir /{}".format(remoteip,f_name))
                os.system("ssh {} mount /dev/{}  /{}".format(remoteip,diskname,f_name))
            elif int(c)==2 :
                os.system("ssh {} fdisk /dev/{}".format(remoteip,diskname))
                os.system("ssh {} echo d | fdisk /dev/{}".format(remoteip,diskname))
                os.system("ssh {} echo w | fdisk /dev/{}".format(remoteip,diskname))
                os.system("ssh {} echo q | fdisk /dev/{}".format(remoteip,diskname))
        if ch==31:
            exit()
        else:
            print("Option not supported enter local or remote")
        get_input_speech("Enter to continue")
        os.system("clear")
    else:
        print("Enter the Right Location")
