from requests import get
from bs4 import BeautifulSoup
from json import loads
def main_handler(event, context):
    content=get("https://ncov.dxy.cn/ncovh5/view/pneumonia")
    content.encoding='utf-8'
    data=content.text
    bs = BeautifulSoup(data,'html.parser')
    a=bs.find(id="getListByCountryTypeService2").prettify()
    b=a.replace('<script id="getListByCountryTypeService2">','')
    a=b.replace('</script>','')
    b=a.replace('}catch(e){}','')
    a=b.replace(' try { window.getListByCountryTypeService2 = ','')
    return loads(a)