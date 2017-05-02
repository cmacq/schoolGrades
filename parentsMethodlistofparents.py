import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent



ua = UserAgent()
header = {'user-agent':ua.chrome}
#google_page = requests.get('https://www.google.com',headers=header)
#google_page = requests.get('https://sites.google.com/a/lexington.k12.il.us/ljhs-homework-help/7th-grade/assignments',headers=header)
#google_page = requests.get('https://www.google.com/calendar/embed?src=lexington.k12.il.us_trqdg10lkf759nbhfijho33i2g@group.calendar.google.com&amp;color=%23668CD9&amp;mode=AGENDA&amp;showTitle=1&amp;showNav=1&amp;showDate=1&amp;showTabs=1&amp;showCalendars=0&amp;hl=en',headers=header)
google_page = requests.get('https://calendar.google.com/calendar/htmlembed?src=lexington.k12.il.us_trqdg10lkf759nbhfijho33i2g@group.calendar.google.com&amp;amp;color=%23668CD9&amp;amp;mode=AGENDA&amp;amp;showTitle=1&amp;amp;showNav=1&amp;amp;showDate=1&amp;amp;showTabs=1&amp;amp;showCalendars=0&amp;amp;hl=en&mode=AGENDA&dates=20170101/20170201',headers=header)
#https://www.google.com/calendar/embed?src=lexington.k12.il.us_trqdg10lkf759nbhfijho33i2g@group.calendar.google.com&amp;color=%23668CD9&amp;mode=AGENDA&amp;showTitle=1&amp;showNav=1&amp;showDate=1&amp;showTabs=1&amp;showCalendars=0&amp;hl=en" title="LJHS 7th Grade Assignments
soup = BeautifulSoup(google_page.content,'lxml') # html.parser
print(soup.prettify)
link = soup.a
#print(link)   
#
#print(link.parents)   
#print(link.parent)

#for parent in link.parents:
#    print(parent.name)
                    
meta = soup.meta
#print(meta)
#get method can be used to get the value of any meta attribute
#print(meta.get('charset'))

#can also treat the attribute like a dictionary
#print(meta['charset'])
# this isn't working for me - but it worked for him in the demo


#body = soup.body

#print(soup.prettify)

#print(body['style'])
# there can be more than one attribute

# Navigable strings - getting the string inside a tag
#title = soup.title
#print(title.string)
#print(title)

#title.string.replace_with("title has been changed")
#print(title)
#p = soup.p

#print(p)





#(soup.prettify())


#identify some tags

#tag.contents = returns a list of children
"""
head = soup.head
print(head.contents)

for child in head.contents:
    print(child if child is not None else '')
"""    

#body = soup.body
#for child in body.contents:
#    print(child if child is not None else '',end='\n\n\n\n')
#    
#for child in body.children:
#    print(child if child is not None else '',end='\n\n\n\n')

#descendants

#head = soup.head
#for child in soup.head:
#    print(child)
    
    
    # .contents only returns direct children
    # 
    
#body = soup.body
#
#children = [child for child in body.contents if child != '\n']
#print(len(children))
#
#for index,child in enumerate(soup.head.descendants):
#    print(index)
#    print(child if child != '\n' else '\\n')
#
#div = soup.div
#print(div)

#parent = div.parent
#print(parent.name)
#
#child = div.child
#print(child.name)

p = (soup.body.p)
divset = (soup.div)

# .next_siblings

#for sibling in p.next_siblings:
#    #print(sibling.name if sibling != '\n' else '')
#    pass

for sibling in divset.next_siblings:
    print(sibling)

# .previous_siblings

#==============================================================================
# for sibling in p.previous_siblings:
#     print(sibling if sibling  != '\n' else '')
#==============================================================================




    
    