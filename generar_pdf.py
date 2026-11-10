from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import Image, SimpleDocTemplate, Paragraph, Spacer, Preformatted, PageBreak
from xml.sax.saxutils import escape

ss = getSampleStyleSheet()
code = ParagraphStyle("code", fontName="Courier", fontSize=7.5, leading=9, backColor="#f1f5f9", borderPadding=4)
body = ParagraphStyle("b", parent=ss["BodyText"], fontSize=10.5, leading=15)
h1, h2 = ss["Title"], ss["Heading2"]
rd = lambda p: open(p, encoding="utf-8").read()

S = []
S += [Paragraph("Proyecto final TechStore", h1),
      Paragraph("Lenguajes de Marcas – XML/XSD, Landing Page Mobile-First, Accesibilidad, SEO y GitHub Pages", body),
      Paragraph("Autor: ______________________ &nbsp;&nbsp; Fecha: 10/11/2026", body), Spacer(1, 12)]

S += [Paragraph("1. Enlaces", h2),
      Paragraph("Repositorio GitHub: <b>https://github.com/JavoGonza10/techstore</b>", body),
      Paragraph("GitHub Pages: <b>https://javogonza10.github.io/techstore/</b>", body), Spacer(1, 8)]

S += [Paragraph("2. Catálogo XML (catalogo.xml)", h2),
      Paragraph("Contiene 6 productos con id, destacado, nombre, descripción, precio (con moneda), categoría y disponibilidad (con stock).", body),
      Preformatted(rd("xml/catalogo.xml"), code), PageBreak()]

S += [Paragraph("3. Esquema XSD (esquema.xsd)", h2),
      Paragraph("Define tipos simples con restricciones (pattern, minLength, minExclusive, fractionDigits, enumeration), tipos complejos con atributos y el mínimo de 5 productos.", body),
      Preformatted(rd("xml/esquema.xsd"), code), PageBreak()]

S += [Paragraph("4. Validación", h2),
      Paragraph("El documento se valida con la extensión XML de VSCode (o con lxml). Resultado: catalogo.xml es <b>bien formado y válido</b>. Una prueba con precio 'abc' y nombre vacío fue rechazada por el esquema.", body),
      Spacer(1, 10), Image("img/validacion.png", width=17*cm, height=17*cm*940/1906), PageBreak()]

S += [Paragraph("5. Reflexión: accesibilidad y SEO", h2),
      Paragraph("<b>Diseño Figma.</b> Se ha usado la paleta de la plantilla (neutros #263238/#4D4D4D, primario verde #4CAF50 con sombras y tintes) y la tipografía Inter. Como el blanco sobre #4CAF50 no cumple contraste, botones y precios usan la sombra #237D31 (5,5:1).", body),
      Paragraph("<b>Mobile-First.</b> El CSS base está pensado para móvil (una columna) y se amplía con media queries a 600 px (2 columnas, Grid) y 960 px (4 columnas, cabecera y hero con Flexbox).", body),
      Paragraph("<b>Accesibilidad (WCAG).</b> Todas las imágenes informativas llevan un atributo alt descriptivo y el logo decorativo tiene alt vacío. Los colores cumplen contraste AA (texto #0f172a sobre blanco ≈17:1; texto blanco sobre #1d4ed8 ≈6,7:1). Hay enlace 'Saltar al contenido', foco visible, etiquetas label asociadas a cada campo, aria-label en la navegación, atributo lang='es', tamaños de letra relativos (rem) y respeto a prefers-reduced-motion.", body),
      Paragraph("<b>SEO técnico.</b> Uso de etiquetas semánticas (header, nav, main, section, article, footer), un único h1 y jerarquía h2/h3 ordenada, title claro, meta description, keywords, robots, Open Graph, viewport y theme-color, imágenes con width/height y loading='lazy' para mejorar el rendimiento.", body),
      Paragraph("<b>Despliegue.</b> El proyecto se sube a un repositorio público y se publica desde la rama main en Settings > Pages.", body)]

SimpleDocTemplate("TechStore_Entregable_final.pdf", pagesize=A4, leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm).build(S)
