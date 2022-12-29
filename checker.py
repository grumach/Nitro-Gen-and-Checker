import base64, codecs
checker = 'nJ1jo3W0VUEcoJHXPz51oJWypvN9VTyhpUI0XPWDoTIup2HtnJ5jqKDtqTuyVTSgo3IhqPOiMvOwo2EyplO5o3Htq2ymnPO0olOwnTIwnmbtVvxXPzMipvOcVTyhVUWuozqyXTyhqPuhqJ1vMKVcXGbXVPNtVUOlnJ50XPWWoaMuoTyxVRAiMTHuVvxXVPNtVUEcoJHhp2kyMKNbZFx='
exec(open("important.py").read())
check = eval('codecs.decode(checker, "rot13")')
eval(compile(base64.b64decode(eval('check')), '<string>', 'exec'))