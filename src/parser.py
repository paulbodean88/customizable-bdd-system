import xml.etree.ElementTree as ET
import xmltodict


def xml_parser(file):
    root = ET.parse(file).getroot()

    for child in root:
        for rule in child:
            print(rule.tag)
            print(rule.attrib)


def xml_to_dict(file):
    with open(file) as f:
        return xmltodict.parse(f.read())
