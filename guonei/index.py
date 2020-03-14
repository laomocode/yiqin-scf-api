from requests import get
from bs4 import BeautifulSoup
from json import loads
def main_handler(event, context):
    content=get("https://3g.dxy.cn/newh5/view/pneumonia")
    content.encoding='utf-8'
    data=content.text
    bs = BeautifulSoup(data,'html.parser')
    a=bs.find(id="getAreaStat").prettify()
    b=a.replace('<script id="getAreaStat">','')
    a=b.replace('</script>','')
    b=a.replace('}catch(e){}','')
    a=b.replace(' try { window.getAreaStat = ','')
    return loads(a)