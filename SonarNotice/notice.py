import requests
from mail import Mail
from config import *


class Sonar:

    def __init__(self):
        self.login_status = False
        self.s = requests.Session()

    def login(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'login': 'admin', 'password': '******'}
        r = self.s.post(api['login'], headers=headers, data=payload)
        self.validate()

    def logout(self):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        r = self.s.post(api['logout'], headers=headers)
        self.validate()

    def validate(self):
        r = self.s.get(api['validate'])
        if r.status_code == 200 and r.json()['valid']:
            self.login_status = True
        else:
            self.login_status = False

    def project_status(self, project_key):
        r = self.s.get(api['project_status'] + project_key)
        if r.status_code == 200:
            projectStatus = r.json()['projectStatus']
            status = projectStatus['status']
            conditions = projectStatus['conditions']
            periods = projectStatus['periods']

            report = {'status': status2cn.get(status), 'metrics': []}
            if status != 'OK':
                for condition in conditions:
                    if condition['status'] != 'OK':
                        condition['status'] = status2cn.get(
                            condition['status'])
                        condition['metricKey'] = metric2cn.get(
                            condition['metricKey'])
                        report['metrics'].append(condition)
            return report

    def notice(self, project):
        '''
        # 当状态为 正常 时
        {'status': '正常'}

        # 当状态为 警告/错误 时
        {'status': '警告', 'metrics': [{'status': 'WARN',
        'metricKey': 'reliability_rating', 'comparator': 'GT',
        'warningThreshold': '2', 'errorThreshold': '3', 'actualValue': '3'}]}
        '''
        if not self.login_status:
            self.login()
        if not self.login_status:
            print('*** Login failure ***')
            exit(1)

        status = self.project_status(project['key'])
        if status['status'] != '正常':
            text = '\n'.join([metric['metricKey'] + ': ' + metric['status']
                              for metric in status['metrics']])
            project_url = url + 'dashboard?id=' + project['key']
            body = '项目: %s\n状态: %s\n\n<异常指标>\n' % (
                project['name'], status['status']) + text + '\n\n项目地址: ' + project_url
            status['body'] = body
            print(body)
        return status


if __name__ == '__main__':
    sonar = Sonar()
    mail = Mail()
    for project in projects:
        notice = sonar.notice(project)
        print(project['name'] + ': ' + notice['status'])
        if notice['status'] != '正常':
            mail.send(project['name'], project['to'], project['cc'], notice)
