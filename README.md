# Pàgina web de La Crida Premià de Dalt

[http://cridapremiadedalt.github.io/](http://cridapremiadedalt.github.io/)

## Estructura de la pàgina

* Pàgines
* Posts

## Pàgines

### Dinàmiques

* Inici
* Tags
* Categories
* Arxiu
* Autors
* Category

### Estàtiques

* Contacte
* Programa
* Codi Ètic

## Reconeixements

* Per a realitzar aquest blog, s'ha utilitzat de base la plantilla [pelican-hss](https://github.com/laughk/pelican-hss) realitzada per Kei Iwasaki.

## How to execute the site

El primer cop que s'executa s'ha de crear el entorn virtual i instalar-hi les dependències.

```bash
virtualenv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

La resta de vegades que s'executi es pot fer activant el entorn prèviament creat i executant pelican.

```bash
source venv/Scripts/activate
pelican -lr
```

## Reference links

https://shahayush.com/2020/03/web-pelican-pt1-setup/
https://docs.getpelican.com/en/stable/settings.html#template-pages
https://docs.getpelican.com/en/stable/content.html#writing-content
