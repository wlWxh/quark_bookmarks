import os
from selenium import webdriver
from selenium.webdriver.common.by import By

url = input('请输入链接：\n')
os.system('cls')

while True:
    i = int(input('''请选择浏览器：
1）Chrome
2）Edge
3）Firefox
4）PhantomJS
5）Safari
'''))
    if i==1:
        driver = webdriver.Chrome()
        break
    elif i==2:
        driver = webdriver.Edge()
        break
    elif i==3:
        driver = webdriver.Firefox()
        break
    elif i==4:
        driver = webdriver.PhantomJS()
        break
    elif i==5:
        driver = webdriver.Safari()
        break
    else:
        print('请输入正确的数字')
        os.system("pause")
        os.system('cls')
        
try:
    driver.get(url)
    driver.implicitly_wait(3)
except Exception as e:
    print('连接失败，请检查链接')
    os.system("pause")
    exit()

i=driver.find_elements(By.CLASS_NAME,"left")

n=1
for j in i:
    print(str(n)+')'+j.text)
    n+=1

if n==1:
    print('登录状态异常，请检查链接')
    os.system("pause")
    exit()

while True:
    x=0
    x=int(input('\n请选择要同步的版本：\n'))
    if x>0 and x<=n:
        print(i[x-1].text)
        i[x-1].click()
        break
    else:
        print('请输入正确的数字')
        os.system("pause")
        os.system('cls')

windows = driver.window_handles  
driver.switch_to.window(windows[-1])

i=driver.find_elements(By.CLASS_NAME,"ant-tree-treenode-switcher-close")

for j in i:
    j.click()

i=driver.find_element(By.CLASS_NAME,"ant-tree-list").text

driver.quit()

i = i.split('\n')

html=[]
for n in range(len(i)):
    if i[n].find('https://') >= 0:
        t='<DT><A HREF="'+i[n]+'">'+i[n-1]+'</A>\n'
        html.append(t)
    if i[n].find('http://') >= 0:
        t='<DT><A HREF="'+i[n]+'">'+i[n-1]+'</A>\n'
        html.append(t)

with open('bookmarks.html','w',encoding='utf-8') as f:
    f.writelines(html)

print('书签已导出至bookmarks.html文件，请在'+os.getcwd()+'中查看')
