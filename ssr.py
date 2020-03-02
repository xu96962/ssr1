# -*- coding: UTF-8 -*-
import base64, requests, os

root_dir = os.path.dirname(os.path.abspath(__file__))
path = root_dir+'/ssr.txt'
res = root_dir+'/ssr'
group = 'lixuelu'
group = base64.urlsafe_b64encode(group.encode()).decode().strip('=')
try:
    with open(path,'r') as f:
        txt = f.read()
        txt = txt.strip().split('\n')
        yy = []
        for i in txt:
            j = i.split('ssr://')[1]
            j = j.strip()
            data = base64.urlsafe_b64decode((j + '=' * (-len(j) % 4)).encode()).decode()
            data2 = base64.urlsafe_b64encode((data.split('group=')[0]+'group='+group).encode()).decode()
            data = 'ssr://'+data2.strip('=')
            yy.append(data)
        d = '\n'.join(yy)
        d = (base64.b64encode(d.encode()).decode()).strip('=')
        print (d)
        with open(res,'w+') as ff:
            ff.writelines(d)
except Exception as e:
    print (e)