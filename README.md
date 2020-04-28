
# Welcome to Full-like InstaBot

This bot fully like all your friend post.

```python
for link in valid_links: # walk through valid links, all of the users post and find like button, then push it
    chrome.get(link)
    like = chrome.find_element_by_xpath('//*[name()="svg"][@aria-label="Like"]')
    time.sleep(1)
    like.click()
```

![shot](shot.gif)




<span style="color:red">Happy Codding 🍓</span>

> Peyman Majidi 
