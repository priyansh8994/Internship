#!/usr/bin/env python
# coding: utf-8

# In[184]:


get_ipython().system('pip install selenium')


# In[187]:


from selenium.webdriver import Chrome


# In[188]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[189]:


driver=webdriver.Chrome(r"C:\Users\hp\Desktop\chromedriver_win32")


# In[ ]:





# In[88]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[89]:


driver.get("https://www.naukri.com/")


# In[90]:


designation=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input")
designation.send_keys('Data Analyst')


# In[91]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Bangalore')


# In[92]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[6]")
search.click()


# In[93]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[96]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]') 
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)

company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]') 
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)
    


# In[97]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[98]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'location':job_location,'company_name':company_name,'Experience':experience_required})
df


# In[99]:


# Answer number 2
driver=webdriver.Chrome(r"C:\Users\hp\Desktop\chromedriver_win32")


# In[ ]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[100]:


driver.get("https://www.naukri.com/")


# In[101]:


designation=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input")
designation.send_keys('Data Scientist')


# In[102]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Bangalore')


# In[103]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[6]")
search.click()


# In[104]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[105]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]') 
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)

company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]') 
for i in experience_tags[0:10]:
     exp=i.tex
    experience_required.append(exp)


# In[106]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[107]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'location':job_location,'company_name':company_name,'Experience':experience_required})
df


# In[123]:


#Answer number 3
driver=webdriver.Chrome(r"C:\Users\hp\Desktop\chromedriver_win32")


# In[124]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[125]:


driver.get("https://www.naukri.com/")


# In[126]:


designation=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input")
designation.send_keys('Data Scientist')


# In[127]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Delhi/NCR')


# In[128]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[6]")
search.click()


# In[129]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[133]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]') 
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)

company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
experience_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]') 
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)


# In[134]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[135]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'location':job_location,'company_name':company_name,'Experience':experience_required})
df


# In[140]:


# Answer 4
driver=webdriver.Chrome(r"C:\Users\hp\Desktop\chromedriver_win32")


# In[165]:


url="https://www.flipkart.com/"
driver.get(url)


# In[143]:


search_g= driver.find_element(By.XPATH,'//input[@class="_3704LK"]')
search_g


# In[144]:


search_g.send_keys('sunglasses')


# In[145]:


search_btn=driver.find_element(By.XPATH,'//button[@class="L0Z3Pu"]')
search_btn


# In[146]:


search_btn=driver.find_element(By.CLASS_NAME,'L0Z3Pu')
search_btn.click()


# In[147]:


B_name=[]
Price=[]
P_desc=[]
Discount=[]


# In[157]:


for i in range(3):
    b_name=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    p_desc=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    price =driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    discount=driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')
    
    for j  in b_name:
        B_name.append(j.text)
    B_name[:100]    
    
    
    
    for k in p_desc:
        P_desc.append(k.text)
    P_desc[:100] 
    
    
    for l in price:
        Price.append(l.text)
    Price[:100] 
    
    
    for t in discount:
        Discount.append(t.text)
    Discount[:100]


# In[160]:


B_name[:100]


# In[159]:


print(len(B_name[:100])),print(len(Price[:100])),print(len(P_desc[:100])),print(len(Discount[:100]))


# In[162]:


sun_gl=pd.DataFrame({})
sun_gl['Brand_name']=B_name[:100]
sun_gl['P_price']=Price[:100]
sun_gl['Pr_desc']=P_desc[:100]
sun_gl['P_discount']=Discount[:100]


# In[163]:


sun_gl


# In[166]:


#Answer5
driver=webdriver.Chrome(r"C:\Users\hp\Desktop\chromedriver_win32")


# In[167]:


url="https://www.flipkart.com/"
driver.get(url)


# In[168]:


search_g= driver.find_element(By.XPATH,'//input[@class="_3704LK"]')
search_g


# In[169]:


search_g.send_keys('sneakers')


# In[170]:


search_btn=driver.find_element(By.XPATH,'//button[@class="L0Z3Pu"]')
search_btn


# In[171]:


search_btn=driver.find_element(By.CLASS_NAME,'L0Z3Pu')
search_btn.click()


# In[172]:


B_name=[]
Price=[]
P_desc=[]
Discount=[]


# In[178]:


for i in range(3):
    b_name=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    p_desc=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    price =driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    discount=driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')
    
    for j  in b_name:
        B_name.append(j.text)
    B_name[:100]    
    
    
    
    for k in p_desc:
        P_desc.append(k.text)
    P_desc[:100] 
    
    
    for l in price:
        Price.append(l.text)
    Price[:100] 
    
    
    for t in discount:
        Discount.append(t.text)
    Discount[:100]


# In[180]:


print(len(B_name[:100])),print(len(Price[:100])),print(len(P_desc[:100])),print(len(Discount[:100]))


# In[182]:


sneak=pd.DataFrame({})
sneak['Brand_name']=B_name[:100]
sneak['P_price']=Price[:100]
sneak['Pr_desc']=P_desc[:100]
sneak['P_discount']=Discount[:100]


# In[183]:


sneak


# In[198]:


#answer 7
driver=webdriver.Chrome(r"C:\Users\hp\Desktop\chromedriver_win32")


# In[199]:


url="https://www.amazon.in/"
driver.get(url)


# In[202]:


search_g= driver.find_element(By.XPATH,'//input[@class="nav-input nav-progressive-attribute"]')
search_g


# In[203]:


search_g.send_keys('Laptop')


# In[204]:


search_btn=driver.find_element(By.XPATH,'//div[@class="nav-search-submit nav-sprite"]')
search_btn


# In[205]:


search_btn=driver.find_element(By.XPATH,'//div[@class="nav-search-submit nav-sprite"]')
search_btn.click()


# In[206]:


Title=[]
Price=[]
Rating=[]


# In[220]:


for i in range(3):
    b_name=driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
    p_desc=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
    price =driver.find_elements(By.XPATH,'//i[@class="a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom"]')
    
    
    for j  in b_name:
        Title.append(j.text)
    Title[:10]    
    
    
    
    for k in p_desc:
        P_desc.append(k.text)
    P_desc[:10] 
    
    
    for l in price:
        Price.append(l.text)
    Price[:10] 
    


# In[221]:


print(len(b_name[:10])),print(len(Price[:10])),print(len(P_desc[:10]))


# In[222]:


lap=pd.DataFrame({})
lap['Brand_name']=B_name[:10]
lap['P_price']=Price[:10]
lap['Pr_desc']=P_desc[:10]


# In[215]:


lap


# In[231]:


#Answer8
driver=webdriver.Chrome(r"C:\Users\hp\Desktop\chromedriver_win32")


# In[232]:


url="https://www.azquotes.com/"
driver.get(url)


# In[233]:


search_btn=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a')
search_btn.click()


# In[240]:


from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()


driver.get('https://www.azquotes.com/')


top_quotes_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a')
top_quotes_button.click()


driver.implicitly_wait(10)


quotes = []
authors = []
types = []

quote_tags = driver.find_elements(By.XPATH,'//div[@class="title"]')
for tag in quote_tags[:10]:
    quote = tag.text.strip()
    quotes.append(quote)
    
author_tags = driver.find_elements(By.XPATH,'//div[@class="author"]' ) 
for tag in author_tags[:10]:
    author = tag.text.strip()
    authors.append(author)

type_tags = driver.find_elements(By.XPATH,'//div[@class="tags"]' )
for tag in type_tags[:10]:
    quote_type = tag.text.strip()
    types.append(quote_type)


for i in range(10):
    print(f'{i+1}.  Quote: {quotes[i]}')
    print(f'   Author: {authors[i]}')
    print(f'   Type: {types[i]}')
    print()


driver.quit()


# In[248]:





# In[245]:





# In[ ]:





# In[ ]:




