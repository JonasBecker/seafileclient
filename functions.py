import subprocess

def write_config(p_file,username, token):
  with open('seafileclient/base_config.conf') as f:
    content = f.read()

  content = content.replace("###USERNAME###",username)
  content = content.replace("###TOKEN###",token)

  with open(p_file,'w') as f:
    f.write(content)

def start_client(conf_file):
  subprocess.Popen('seadrive -c {} -f -d seafile -o nonempty -l seafilelog.log /root'.format(conf_file),shell=True)