from lxml import etree
import sys
xsd = etree.XMLSchema(etree.parse("esquema.xsd"))
for f in sys.argv[1:]:
    doc = etree.parse(f)
    ok = xsd.validate(doc)
    print(f, "-> VÁLIDO" if ok else "-> NO VÁLIDO")
    for e in xsd.error_log: print("  línea", e.line, e.message)
