def scrape():   

    import pandas as pd
    from splinter import Browser
    from bs4 import BeautifulSoup as bs
    import requests

    executable_path = {'executable_path': 'C:/Users/gamew/Anaconda3/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)
    soup = bs(response.text, 'lxml')

    # News title from website
    news_title = soup.find('div', class_ = 'content_title').a.text.strip()
    print(news_title)

    # News paragraph from website
    news_p = soup.find('div', class_ = 'image_and_description_container').div.text.strip()
    print(news_p)

    # Image collection
    executable_path = {'executable_path': 'C:/Users/gamew/Anaconda3/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.click_link_by_partial_text("FULL IMAGE")
    browser.is_element_not_present_by_text('more info', wait_time=1)
    browser.click_link_by_partial_text('more info')
    html = browser.html
    soup =bs(html, 'html.parser')
    img_link = soup.find('figure', class_ = 'lede').a['href']
    feat_img_url = 'https://www.jpl.nasa.gov'+img_link
    browser.quit()
    print(feat_img_url)

    # Mars weather from twitter
    url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(url)
    soup = bs(response.text, 'lxml')
    mars_weather = soup.find('p', class_= 'TweetTextSize').text
    print(mars_weather)

    # Table of data
    url = 'https://space-facts.com/mars/'
    facts = pd.read_html(url)
    facts_df = facts[1]
    facts_df.columns = ['description', 'value']
    facts_table = facts_df.to_html()
    facts_table

    # Hemisphere image collection
    executable_path = {'executable_path': 'C:/Users/gamew/Anaconda3/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    response = requests.get(url)
    soup = bs(response.text, 'lxml')
    image_items = soup.find_all('div', class_ = 'item')
    image_items
    image_items = soup.find_all('div', class_ = 'item')
    hemisphere_image_urls = []
    for item in image_items:
        img_title =item.h3.text
        img_link = 'https://astrogeology.usgs.gov'+item.a['href']
        browser.visit(img_link)
        img_url = browser.find_link_by_text('Sample')['href']
        hemisphere_image_urls.append({'title':img_title,'img_url':img_url})
    browser.quit()

    # Scraped data
    scraped_data = {'news_title':news_title, 'news_p':news_p, 'feat_img_url':feat_img_url,'mars_weather':mars_weather,'facts_table':facts_table,'hemisphere_image_urls':hemisphere_image_urls}
    scraped_data

    return scraped_data