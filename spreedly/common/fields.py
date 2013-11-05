from datetime import datetime
from lxml import etree
import inspect


class Fields(object):
    def __init__(self, xml_doc=None):
        if not xml_doc:
            return

        class_hier = inspect.getmro(self.__class__)

        for cls in class_hier:
            for field_name, field in cls.__dict__.iteritems():
                if field_name not in self.__dict__ and isinstance(field, Field):
                    value = field.value(xml_doc, field_name)
                    setattr(self, field_name, value)
                if field_name not in self.__dict__ and isinstance(field, Fields):
                    value = field.__class__(xml_doc.xpath('.//%s' % field_name)[0])
                    setattr(self, field_name, value)


class Field(object):
    def __init__(self, xpath=None, optional=False):
        self._xpath = xpath
        self._optional = optional

    def xpath(self, field_name):
        if self._xpath:
            return self._xpath
        else:
            return './/%s' % field_name

    def value(self, xml_doc, field_name):
        xml_values = xml_doc.xpath(self.xpath(field_name))

        if xml_values:
            return xml_values[0].text
        elif not self._optional:
            raise RuntimeError('Non-optional field "%s" missing from XML fragment:\n%s' %
                               (field_name, etree.tostring(xml_doc, pretty_print=True)))


class IntegerField(Field):
    def value(self, xml_doc, field_name):
        value = super(IntegerField, self).value(xml_doc, field_name)

        if value:
            return int(value)


class DateTimeField(Field):
    def value(self, xml_doc, field_name):
        value = super(DateTimeField, self).value(xml_doc, field_name)

        if value:
            return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")


class BooleanField(Field):
    def value(self, xml_doc, field_name):
        value = super(BooleanField, self).value(xml_doc, field_name).lower()

        if value == 'true':
            return True
        elif value == 'false':
            return False
        elif value is not None:
            raise RuntimeError('Value "%s" is not a boolean value.' % value)
