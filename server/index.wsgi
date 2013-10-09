import sae
from hashlib import md5
from bottle import Bottle,request,debug

import urllib2 as urilib
import sae.kvdb

SECRET = "fc967we161f7d898ad257d62407373"
users = {
    "yubao1":"123456",
    "xiaoqing4":"123456",
    "liulei12":"123456"}
messages ={
    "0" : "success",
    "1" : "User Not Exist",
    "2" : "Error Password",
    "3" : "Uploads Not Found"
}

app = Bottle()
debug(True)

def check():
    uid = request.forms.uid
    pwd = request.forms.pwd
    try:
        real_pwd = users[uid]
    except:
        return messages["1"];

    real_encry_pwd = md5(md5(SECRET+real_pwd).hexdigest() + SECRET).hexdigest()
    if(pwd != real_encry_pwd):
        return messages["2"]

    return messages["0"]


@app.route("/dict/pull",method="POST")
def pull():
    uid = request.forms.uid
    upload = request.files.upload
    ret = check()
    if(ret != messages["0"]):
        return ret

    kv = sae.kvdb.KVClient()
    k = "dict_" + uid
    data =kv.get(str(k))

    return data


@app.route("/dict/push",method="POST")
def push():
    uid = request.forms.uid
    upload = request.files.upload
    ret = check()
    if(ret != messages["0"]):
        return ret

    if  upload and upload.file:
        raw = upload.file.read()
        filename = upload.filename
    else:
        return messages["3"]

    kv = sae.kvdb.KVClient()
    k = "dict_" + uid
    kv.set(str(k),raw)

    return messages["0"]

application = sae.create_wsgi_app(app)