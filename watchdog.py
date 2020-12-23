#!/usr/bin/python3
import docker
import datetime
import dateutil.parser
import syslog
saveselenoid = "aerokube"
timeout = 1
syslog.syslog('Cheking for dead containers')
client = docker.from_env()
for container in client.containers.list():
   print (container.attrs["Config"]["Image"])
   if datetime.datetime.now(datetime.timezone.utc) - dateutil.parser.parse(container.attrs["Created"]) > datetime.timedelta(minutes=timeout):
      if saveselenoid in container.attrs["Config"]["Image"]:
   	   continue
      else:
           container.kill()
           syslog.syslog('Zombie was killed ' + container.attrs["Config"]["Image"])
