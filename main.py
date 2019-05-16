import os


class NodeJS:
    def __init__(self):
        self.install_path = os.getcwd()
        self.install_file = 'node-v10.15.3-x64.msi'
        self.conf_resource_url = 'https://registry.npm.taobao.org'

    def install(self):
        os.system('\\'.join([self.install_path, self.install_file]))

    def configure(self):
        os.system('npm config set registry %s' % self.conf_resource_url)

    def check(self):
        os.system('npm config get registry')


if __name__ == '__main__':
    node_inst = NodeJS()
    node_inst.install()
    node_inst.configure()
    node_inst.check()
