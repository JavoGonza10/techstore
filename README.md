# TechStore – Landing Page y Catálogo XML

Proyecto final: catálogo de productos validado con XML/XSD y landing page Mobile-First, accesible y optimizada para SEO.

## Estructura
```
techstore/
├── index.html          Landing page
├── css/styles.css      Estilos (Mobile-First, Flexbox + Grid)
├── img/                Imágenes SVG
├── xml/catalogo.xml    Catálogo (6 productos)
├── xml/esquema.xsd     Esquema de validación
└── validar.py          Script de validación (lxml)
```

## Validar el XML
Con VSCode: instala la extensión *XML* (Red Hat) y abre `xml/catalogo.xml`; el esquema se enlaza con `xsi:noNamespaceSchemaLocation`.
O por terminal: `cd xml && python ../validar.py catalogo.xml`
