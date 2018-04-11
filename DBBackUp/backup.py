import os
import sys
import time
import shutil


backup_dir = r'\\testvm\DBBakupForSIT'
local_dir = r"D:\BACK"

today = time.strftime("%Y%m%d", time.localtime())
_today = time.strftime("%Y_%m_%d_", time.localtime())

back_num_max = 30
code = -100


def check_status(filename):
    with open(filename,  encoding='utf-8') as f:
        if '状态: 成功' in f.read():
            return True
        else:
            return False


def backup():
    for (path, dirs, files) in os.walk(local_dir):
        for filename in files:
            # 存在当日的日志文件
            if 'SonarQube_backup_' + _today in filename:
                shutil.copy(filename, backup_dir)
                print('备份成功')


def clear(directory, keywords):
    for (path, dirs, files) in os.walk(directory):
        files = [f for f in files if keywords in f]
        num = len(files)
        if num > back_num_max:
            files.sort()
            for f in files[:num-back_num_max]:
                f_dir = os.path.join(backup_dir,f)
                print("删除备份时间超过%s天的数据库文件: %s" %(back_num_max, f_dir))
                os.remove(f_dir)


def send_email(message):
    print(message)


def main():
    log_flag = False
    for (path, dirs, files) in os.walk(local_dir):
        for filename in files:
            # 存在当日的日志文件
            if 'Full_Backup_Sonar_Subplan_1_' + today in filename:
                log_flag = True
                if check_status(filename):
                    backup()
                    code = 0
                    clear(backup_dir, 'SonarQube')
                    clear(local_dir, 'SonarQube')
                else:
                    send_email("本地备份失败")
                    code = -2

    # 如果没有日志文件，发送邮件提醒
    if not log_flag:
        send_email("未找到今日备份日志，可能发生备份异常！")
        code = -1

    sys.exit(code)

if __name__ == '__main__':
    main()
