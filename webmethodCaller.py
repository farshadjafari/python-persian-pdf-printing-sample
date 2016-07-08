import httplib
from xml.dom import minidom
http = httplib.HTTPSConnection("sep.shaparak.ir")
xml = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenc="http://www.w3.org/2003/05/soap-encoding" xmlns:tns="urn:Foo" xmlns:types="urn:Foo/encodedTypes" xmlns:rpc="http://www.w3.org/2003/05/soap-rpc" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
<soap12:Body soap12:encodingStyle="http://www.w3.org/2003/05/soap-encoding">
<tns:verifyTransaction>
  <String_1 xsi:type="xsd:string">""" +RefNum+ """</String_1>
  <String_2 xsi:type="xsd:string">-----------YOUR-ID-should-be-here--------</String_2>
</tns:verifyTransaction>
</soap12:Body>
</soap12:Envelope>"""
http.request("POST", "/payments/referencepayment.asmx", body=xml, headers = {
    # "Host": "sep.shaparak.ir",
    "Content-Type": "application/soap+xml; charset=utf-8",
    "Content-Length": str(len(xml)),
    # "SOAPAction": "verifyTransaction"
})
r1 = http.getresponse()
data = r1.read()