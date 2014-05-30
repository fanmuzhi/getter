#!/usr/bin/env python
# encoding: utf-8

from xml.dom.minidom import Document, parseString, Node
from pprint import pprint as pp


def dumps(diction):
    '''convert diction to xml
    '''
    if(type(diction) == dict):
        xml = dict2xml(diction).dump()
        return xml


def loads(xml):
    '''convert xml to diction
    '''
    diction = xml2dict(xml).load()
    return diction


class xml2dict(object):

    def __init__(self, xml):
        self.Dict = {}
        self.doc = parseString(xml)
        self.remove_blanks(self.doc)
        self.doc.normalize()
        self.root = self.doc.documentElement
        self.parse(self.root)

    def remove_blanks(self, node):
        for x in node.childNodes:
            if x.nodeType == Node.TEXT_NODE:
                if x.nodeValue:
                    x.nodeValue = x.nodeValue.strip()
            elif x.nodeType == Node.ELEMENT_NODE:
                self.remove_blanks(x)

    def to_list(self, father):
        myList = []
        for node in father.childNodes:
            if(len(node.childNodes) > 1):
                myList.append(self.parse(node))
            else:
                myList.append(node.childNodes[0].nodeValue)
        return myList

    def parse(self, father):
        myDict = {}
        if(father.hasAttributes()):
            for attr in father.attributes.items():
                myDict.update({attr[0]: attr[1]})
        if(father.hasChildNodes()):
            if(len(father.childNodes) > 1):
                if(father.firstChild.nodeName == father.lastChild.nodeName):
                    # parse a list
                    listname = father.nodeName
                    tag = father.firstChild.nodeName
                    myDict.update({listname: {tag: self.to_list(father)}})
                else:
                    # parse a recurse dict
                    for node in father.childNodes:
                        self.parse(node)
            else:
                # parse a value
                node = father.childNodes[0]
                if(node.nodeType == Node.TEXT_NODE):
                    myDict.update({father.nodeName: node.nodeValue})
        self.Dict.update(myDict)
        return myDict

    def load(self):
        return self.Dict


class dict2xml(object):
    
    def __init__(self, diction, **kvargs):
        
        #if len(structure) == 1:
        #rootName = str(structure.keys()[0])
        self.doc = Document()
        rootName = kvargs.get("rootName", "xml")
        self.root = self.doc.createElement(rootName)

        self.doc.appendChild(self.root)
        self.build(self.root, diction)

    def build(self, father, structure):
        if type(structure) == dict:
            for k in structure:
                tag = self.doc.createElement(k)
                father.appendChild(tag)
                self.build(tag, structure[k])

        elif type(structure) == list:
            grandFather = father.parentNode
            tagName = father.tagName
            grandFather.removeChild(father)
            for l in structure:
                tag = self.doc.createElement(tagName)
                self.build(tag, l)
                grandFather.appendChild(tag)
        else:
            data = str(structure)
            tag = self.doc.createTextNode(data)
            father.appendChild(tag)

    def dump(self):
        return self.doc.toprettyxml(indent="    ")
        #return self.doc.toxml("utf-8")


if __name__ == '__main__':
    example = {
        "sn": 2103839,
        "item": "SNR",
        "date": "2009-11-25",
        "errorcode": 7,
        "errormsg": u"Noise Too High",
        "signal": {"data": [1, 2, 3]},
        "noise": {"data": [5, 6, 7]}
    }

    print("original:")
    pp(example)
    print("dict to xml:")
    myxml = dumps(example)
    print(myxml)

    print("xml to dict:")
    mydict = loads(myxml)
    pp(mydict)
