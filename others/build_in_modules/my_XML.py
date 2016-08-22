# DOM vs. SAX

# DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点
# SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件
# 正常情况下，优先考虑SAX，因为DOM实在太占内存

from xml.parsers.expat import ParserCreate


# 在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，
# 准备好这3个函数，然后就可以解析xml了


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax: start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax: end_element: %s' % name)

    def char_data(self, text):
        print('sax: char_data: %s' % text)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

# 需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存
# 起来，在EndElementHandler里面再合并

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)


# 生成XML
# 99%的情况下需要生成的XML结构都是非常简单的，因此，最简单也是最有效的生成XML的
# 方法是拼接字符串


def create_xml():
    L = []
    L.append(r'<?xml version="1.0"?>')
    L.append(r'<root>')
    L.append('some & data')
    L.append(r'</root>')
    return ''.join(L)

# print(create_xml())

# 如果要生成复杂的XML呢？建议你不要用XML，改成JSON
