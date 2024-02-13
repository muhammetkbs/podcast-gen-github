import yaml 
import xml.etree.ElementTree as ET

with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)
    rss_element = ET.Element('rss', {'version':'2.0', 
        'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd', 
        'xmlns:content':'http://purl.org/rss/1.0/modules/content/'})

channel_element = ET.SubElement(rss_element, 'channel')

link_prefix = yaml_data['link']


ET.SubElement(channel_element, 'title').text = yaml_data['title']
ET.SubElement(channel_element, 'format').text = yaml_data['format']
ET.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle']
ET.SubElement(channel_element, 'itunes:author').text = yaml_data['author']
ET.SubElement(channel_element, 'description').text = yaml_data['description']
ET.SubElement(channel_element, 'itunes:image', {'href': link_prefix + yaml_data['image']})
ET.SubElement(channel_element, 'language').text = yaml_data['language']
ET.SubElement(channel_element, 'link').text = link_prefix

ET.SubElement(channel_element, 'itunes:category', {'text': yaml_data['category']})

for item in yaml_data['item']:
    item_element = ET.SubElement(channel_element, 'item')
    ET.SubElement(item_element, 'title').text = item['title']
    ET.SubElement(item_element, 'itunes:author').text = yaml_data['author']
    ET.SubElement(item_element, 'description').text = item['description']
    ET.SubElement(item_element, 'itunes:duration').text = item['duration']
    ET.SubElement(item_element, 'pubDate').text = item['published']

    enclosure = ET.SubElement(item_element, 'enclosure', {
        'url': link_prefix + item['file'],
        'type': 'audio/mpeg',
        'lenght': item['length']
    })

output_tree = ET.ElementTree(rss_element)

output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)