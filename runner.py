import os

if __name__ == '__main__':
    os.environ['email'] = 'm.fredi@codermine.com'
    os.environ['psw'] = 'codermineTW$02'
    os.environ['url'] = 'https://codermine.eu.teamwork.com/'

    os.popen('python3 -m main')
