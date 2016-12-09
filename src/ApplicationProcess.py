from multiprocessing import *
from ceng445 import *
import json

STATUS_OK = 'OK'
STATUS_FAIL = 'FAIL'

class ApplicationProcess(Process):
    def __init__(self, connectionInfo):
        super(ApplicationProcess, self).__init__()
        self._conn = connectionInfo[0]
        self._addr = connectionInfo[1]
        self._app = Application()

    def run(self):
        try:
            while self._conn:
                receivedData = self._conn.recv(65536).decode('utf-8')
                command = json.loads(receivedData)
                result = json.dumps(self.handle(command), indent='\t')
                self._conn.send(result.encode('utf-8'))
        except:
            self._conn.close()

    def handle(self, cmd):
        result = {}
        command = cmd.get('command', None)

        if command == 'available':
            try:
                result['result'] = self._app.available()
                result['status'] = STATUS_OK
            except:
                result['status'] = STATUS_FAIL
        elif command == 'loaded':
            try:
                result['result'] = self._app.loaded()
                result['status'] = STATUS_OK
            except:
                result['status'] = STATUS_FAIL
        elif command == 'load':
            try:
                result['result'] = self._app.load(cmd['args']['name'])
                result['status'] = STATUS_OK
            except:
                result['status'] = STATUS_FAIL
        elif command == 'instances':
            try:
                result['result'] = self._app.instances()
                result['status'] = STATUS_OK
            except:
                result['status'] = STATUS_FAIL
        elif command == 'addInstance':
            try:
                result['result'] = self._app.addInstance(cmd['args']['componentName'], cmd['args']['x'], cmd['args']['y'])
                result['status'] = STATUS_OK
            except:
                result['status'] = STATUS_FAIL
        elif command == 'removeInstance':
            try:
                result['result'] = self._app.removeInstance(cmd['args']['id'])
                result['status'] = STATUS_OK
            except:
                result['status'] = STATUS_FAIL
        elif command == 'callMethod':
            try:
                params = tuple(cmd['args']['params'])
                params = None if params == () else self._getParams(params)
                result['result'] = self._app.callMethod(cmd['args']['id'], cmd['args']['methodName'], params)
                result['status'] = STATUS_OK
            except:
                result['status'] = STATUS_FAIL
        elif command == 'saveDesign':
            try:
                result['result'] = self._app.saveDesign(cmd['args']['path'])
                result['status'] = STATUS_OK
            except:
                result['status'] = STATUS_FAIL
        elif command == 'loadDesign':
            try:
                result['result'] = self._app.loadDesign(cmd['args']['path'])
                result['status'] = STATUS_OK
            except:
                result['status'] = STATUS_FAIL
        elif command == 'execute':
            try:
                result['result'] = self._app.execute()
                result['status'] = STATUS_OK
            except:
                result['status'] = STATUS_FAIL
        else:
            result['result'] = 'Available Commands: '
            result['status'] = STATUS_OK
        return result

    def _getParams(self, params):
        #TODO: Does not cover all possible cases. Improve it later
        retVal = []
        for i in params:
            if type(i) == type({}) and '__factory__' in i and i['__factory__'] == True:
                retVal.append(Factory().createInstance(i['name']))
            else:
                retVal.append(i)
        return tuple(retVal)
