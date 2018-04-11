url = 'http://vwt-sonar/'
api = {
    'login': url + 'api/authentication/login',
    'logout': url + 'api/authentication/logout',
    'validate': url + 'api/authentication/validate',
    'project_status': url + 'api/qualitygates/project_status?projectKey='
}

status2cn = {
    'OK': '正常',
    'WARN': '警告',
    'ERROR': '错误'
}
metric2cn = {
    'reliability_rating': '可靠性',
    'new_reliability_rating': '新可靠性',
    'security_rating': '安全性',
    'new_security_rating': '新增安全性',
    'duplicated_lines_density': '重复行',
    'vulnerabilities': '漏洞',
    'new_vulnerabilities': '新增漏洞',
    'bugs': 'bug',
    'new_bugs': '新增bug',
}


projects = [
    {'name': 'sweetest', 'key': 'sweetest', 'to': [
        'tongl@xxxx.com'], 'cc':['shenhf@xxx.com']}
]
