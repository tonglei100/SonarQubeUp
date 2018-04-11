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
    {'name': 'aries', 'key': 'com.bosera.iof:aries-maven',
        'to': ['huangcx@bosera.com', 'chenhl@bosera.com'], 'cc':['moch@bosera.com']},
    {'name': 'bosera-web', 'key': 'com.bosera.iof.website:bosera-web',
        'to': ['zhouyunhong@bosera.com'], 'cc':['moch@bosera.com']},
    {'name': 'boseraEmp', 'key': 'boseraEmp:boseraEmp', 'to': [
        'zhouyunhong@bosera.com'], 'cc':['moch@bosera.com']},
    {'name': 'capital-web', 'key': 'capital-web:capital-web',
        'to': ['zhouyunhong@bosera.com'], 'cc':['moch@bosera.com']},
    {'name': 'DSMS', 'key': 'DSMS', 'to': [
        'dongyw@bosera.com'], 'cc':['yangxl@bosera.com']},
    {'name': 'PTMS', 'key': 'PTMS', 'to': [
        'dongyw@bosera.com'], 'cc':['yangxl@bosera.com']},
    {'name': 'emos-service', 'key': 'com.bosera:emos-service',
        'to': ['wangpan@bosera.com'], 'cc':['zhum@bosera.com']},
    {'name': 'emos-spcm', 'key': 'com.bosera:emos-spcm',
        'to': ['wangpan@bosera.com'], 'cc':['zhum@bosera.com']},
    {'name': 'emos-web', 'key': 'com.bosera:emos-web',
        'to': ['wangpan@bosera.com'], 'cc':['zhum@bosera.com']},
    {'name': 'portal-service', 'key': 'com.bosera:portal-service',
        'to': ['wangpan@bosera.com'], 'cc':['zhum@bosera.com']},
    {'name': 'ETF', 'key': 'ETF', 'to': [
        'zhangxb@bosera.com'], 'cc':['linhs@bosera.com']},
    {'name': 'NewTA', 'key': 'NewTA', 'to': [
        'zhangxb@bosera.com'], 'cc':['linhs@bosera.com']},
    {'name': 'ZDMS', 'key': 'ZDMS', 'to': [
        'zhangxb@bosera.com'], 'cc':['linhs@bosera.com']},
    {'name': 'iof-base-services', 'key': 'com.bosera.iof.trade:iof-base-services',
        'to': ['gongt@bosera.com'], 'cc':['moch@bosera.com']},
    {'name': 'iof-commons', 'key': 'com.bosera.iof.trade:iof-commons',
        'to': ['gongt@bosera.com'], 'cc':['moch@bosera.com']},
    {'name': 'wechat-gold-web', 'key': 'com.bosera.iof.trade:wechat-gold-web',
        'to': ['gongt@bosera.com'], 'cc':['moch@bosera.com']},
    {'name': 'mobile-web', 'key': 'com.bosera.iof.trade:mobile-web',
        'to': ['yangxl@bosera.com'], 'cc':['moch@bosera.com']},
    {'name': 'app-web', 'key': 'com.bosera.iof.trade:app-web',
        'to': ['yangxl@bosera.com'], 'cc':['moch@bosera.com']},
    {'name': 'kims', 'key': 'kims', 'to': [
        'qixd@bosera.com'], 'cc':['chenmb@bosera.com']},
    {'name': 'koss', 'key': 'koss', 'to': [
        'qinyx@bosera.com', 'JZ37@bosera.com'], 'cc':['chenmb@bosera.com']},
    {'name': 'kvs', 'key': 'kvs', 'to': [
        'zhaoyi1@bosera.com', 'JZ123@bosera.com'], 'cc':['chenmb@bosera.com']},
    {'name': 'klcs', 'key': 'klcs', 'to': [
        'luoyr@bosera.com'], 'cc':['chenmb@bosera.com']},
    {'name': 'sweetest', 'key': 'sweetest', 'to': [
        'tongl@bosera.com'], 'cc':['shenhf@bosera.com']}
]
