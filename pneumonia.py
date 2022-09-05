from lxml import etree
import csv
html = etree.parse('./data.html',etree.HTMLParser())
location = {'地区':html.xpath('//tr[@class="VirusTable_1-85-1_2AH4U9"]/td/a/div/text()')}
newly_increased = {'新增':html.xpath('//tr[@class="VirusTable_1-85-1_2AH4U9"]//td[2]/text()')}
accumulative_total = {'累计':html.xpath('//tr[@class="VirusTable_1-85-1_2AH4U9"]//td[3]/text()')}
cure = {'治愈':html.xpath('//tr[@class="VirusTable_1-85-1_2AH4U9"]//td[4]/text()')}
die = {'死亡':html.xpath('//tr[@class="VirusTable_1-85-1_2AH4U9"]//td[5]/text()')}
existing = {'累计':html.xpath('//tr[@class="VirusTable_1-85-1_2AH4U9"]//td[4]/text()')}
# 按照疫情地区、新增、现有、累计、治愈、死亡的顺序，保存成csv文件，
print(location)
print(newly_increased)
print(accumulative_total)
print(cure)
print(die)
with open('data.csv','w') as csvfile:
    fieldnames = ['地区','新增','累计','治愈','死亡']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(location)
    writer.writerow(newly_increased)
    writer.writerow(accumulative_total)
    writer.writerow(cure)
    writer.writerow(die)