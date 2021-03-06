from lxml import etree
import inspect

def decallmethods(decorator, prefix='test_'):
    """
    decorates all methods in class which begin with prefix test_ to prevent
    accidental external HTTP requests.
    """
    def dectheclass(cls):
        for name, m in inspect.getmembers(cls, inspect.ismethod):
            if name.startswith(prefix):
                setattr(cls, name, decorator(m))

        return cls
    return dectheclass


def _validate(xmlparser, xmlfilename):
    """
        Raises an exception if the XML file doesn't validate.
    """
    with open(xmlfilename, 'r') as f:
        etree.fromstring(f.read(), xmlparser)

def xml_validate(xml_file, xsd_file):
    with open(xsd_file, 'r') as f:
        schema_root = etree.XML(f.read())

    schema = etree.XMLSchema(schema_root)
    xmlparser = etree.XMLParser(schema=schema)

    return _validate(xmlparser, xml_file)

class MockBuffer():

    string = ""

    def write(self, data):
        self.string += data

    def flush(self):
        pass

    def __repr__(self):
        return self.string

    def get(self):
        return self.string

