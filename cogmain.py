from selenium.webdriver import Chrome

browser = Chrome()
browser.get('https://lookup.coghq.org/report/minister/login.php')
browser.find_element_by_name('usr').send_keys('MikeB')
browser.find_element_by_name('psw').send_keys('Pasteur123')
browser.find_element_by_name('submit').click()

# report link
browser.get('https://lookup.coghq.org/report/minister/report.php')

# [0] is spanish button is top-right corner
# [1] starts report button
# handle for possibility of more than 1 report button
# browser.find_elements_by_tag_name('input')[1].click()
browser.find_elements_by_xpath("//input[@type='button']")[1].click()

# reporting to New Jersey
browser.find_element_by_name('ans').click()
browser.find_element_by_name('ans').is_selected() # True if selected

# continue
browser.find_elements_by_tag_name('input')[-1].click()

# no to 'Has marital status changed since last report?'
# [0] is yes
browser.find_elements_by_name('marital_status_change')[1].click()

# no to 'Do you have a supplemental vocation to your ministry?'
# [0] is yes
browser.find_elements_by_name('supplemental_vocation')[1].click()

browser.find_element_by_name('revivals').send_keys(5)
browser.find_element_by_name('past_visit').send_keys(3)
browser.find_element_by_name('spec_serv').send_keys(1)
browser.find_element_by_name('sermons').send_keys(4)
browser.find_element_by_name('personal_evangelism_mtgs').send_keys(5)
browser.find_element_by_name('lectures').send_keys(5)
browser.find_element_by_name('worker_classes').send_keys(5)
browser.find_element_by_name('counseling').send_keys(5)
browser.find_element_by_name('choir_training_mtgs').send_keys(5)
browser.find_element_by_name('tithes').click()
browser.find_element_by_name('tithes_where').send_keys('East Orange Church of God')

# submit edit
# browser.find_element_by_xpath('/html/body/center[3]/input')

browser.quit()