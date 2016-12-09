from json import *
from socket import *
from sys import *

def usage():
    print("Commands and their args are following:")
    print("\tavailable: None\n\tloaded: None\n\tload: componentName")
    print("\tloadDesign/saveDesign: path\n\taddInstance: componentName, x, y\n\tintances: None")
    print("\tremoveInstance: id\n\tcallMethod: id, methodName, params\n\texecute: None")

def run():
    HOST = input('Host IP: ')
    PORT = int(input('Port #: '))

    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((HOST, PORT))

    while True:
        design = {}
        cmd = input('command: ')
        if cmd == 'available':
            design['command'] = cmd
            design['args'] = {}
        elif cmd == 'loaded':
            design['command'] = cmd
            design['args'] = {}
        elif cmd == 'load':
            design['command'] = cmd
            arg = input('componentName: ')
            design['args'] = {}
            design['args']['componentName'] = arg
        elif cmd == 'loadDesign':
            design['command'] = cmd
            arg = input('path: ')
            design['args'] = {}
            design['args']['path'] = arg
        elif cmd == 'saveDesign':
            design['command'] = cmd
            arg = input('path: ')
            design['args'] = {}
            design['args']['path'] = arg
        elif cmd == 'addInstance':
            design['command'] = cmd
            componentName = input('componentName: ')
            x = int(input('x: '))
            y = int(input('y: '))
            design['args'] = {}
            design['args']['componentName'] = componentName
            design['args']['x'] = x
            design['args']['y'] = y
        elif cmd == 'instances':
            design['command'] = cmd
            design['args'] = {}
        elif cmd == 'removeInstance':
            design['command'] = cmd
            id = input('id: ')
            design['args'] = {}
            design['args']['id'] = id
        elif cmd == 'callMethod':
            design['command'] = cmd
            id = input('id: ')
            methodName = input('methodName: ')
            design['args'] = {}
            design['args']['id'] = id
            design['args']['methodName'] = methodName
            design['params'] = []
            print("\tIf a factory is needed, write factory as last param and press enter.")
            print("\tFill factory info and continue params where you were left.")
            params = input('params: ')
            splitted = params.split(',')
            while splitted[-1] != 'factory':
                design['params'] = design['params'] + splitted[:-1]
                name = input('\t\tname: ')
                factoryDict = {}
                factoryDict['__factory__'] = True
                factoryDict['name'] = name
                factoryDict['args'] = []
                factoryDict['kwargs'] = {}
                design['params'].append(factoryDict)
                params = input('params: ')
                splitted = params.split(',')
            design['params'] = design['params'] + splitted
        elif cmd == 'execute':
            design['command'] = cmd
            design['args'] = {}
        elif cmd == 'usage':
            usage()
            continue
        elif cmd == 'quit':
            break
        else:
            print("Unknown command. type 'usage' for more detail")
            continue
        sendData = json.dumps(design)
        sock.send(sendData.encode('utf-8'))
        receivedData = sock.recv(65536).decode('utf-8')
        print(receivedData)
    sock.close()
if __name__ == "__main__":
    run()
