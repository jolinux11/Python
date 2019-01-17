import docker

c = docker.DockerClient(base_url='unix://var/run/docker.sock',version='1.13',timeout=10)
ctr = c.create_container('fedora:latest')
c.start(ctr)
