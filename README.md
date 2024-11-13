 Dandelion Salon Application

A web application for managing salon appointments and services.

## Features

- Make appointments 
- Create user accounts with email
- View hair styles and services
- Online payment processing
- Admin dashboard for salon management

## Live Demo

Visit the live application at: https://madeleinecoiffure.herokuapp.com/

## Tech Stack

- Django 3.2.5
- Python 3.9
- PostgreSQL (via Heroku)
- HTML/CSS/JavaScript
- Heroku for deployment

## Setup

1. Clone the repository
```bash
git clone [repository-url]
```

2. Create and activate virtual environment
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your configurations
```

# Project Structure

```
dandelionCoiffure/
├── .git/
├── deployment/
│   ├── admin/
│   │   ├── css/
│   │   │   ├── vendor/
│   │   │   │   └── select2/
│   │   │   │   │   ├── LICENSE-SELECT2.md
│   │   │   │   │   ├── select2.css
│   │   │   │   │   └── select2.min.css
│   │   │   ├── autocomplete.css
│   │   │   ├── base.css
│   │   │   ├── changelists.css
│   │   │   ├── dashboard.css
│   │   │   ├── fonts.css
│   │   │   ├── forms.css
│   │   │   ├── login.css
│   │   │   ├── nav_sidebar.css
│   │   │   ├── responsive_rtl.css
│   │   │   ├── responsive.css
│   │   │   ├── rtl.css
│   │   │   └── widgets.css
│   │   ├── fonts/
│   │   │   ├── LICENSE.txt
│   │   │   ├── README.txt
│   │   │   ├── Roboto-Bold-webfont.woff
│   │   │   ├── Roboto-Light-webfont.woff
│   │   │   └── Roboto-Regular-webfont.woff
│   │   ├── img/
│   │   │   ├── gis/
│   │   │   │   ├── move_vertex_off.svg
│   │   │   │   └── move_vertex_on.svg
│   │   │   ├── calendar-icons.svg
│   │   │   ├── icon-addlink.svg
│   │   │   ├── icon-alert.svg
│   │   │   ├── icon-calendar.svg
│   │   │   ├── icon-changelink.svg
│   │   │   ├── icon-clock.svg
│   │   │   ├── icon-deletelink.svg
│   │   │   ├── icon-no.svg
│   │   │   ├── icon-unknown-alt.svg
│   │   │   ├── icon-unknown.svg
│   │   │   ├── icon-viewlink.svg
│   │   │   ├── icon-yes.svg
│   │   │   ├── inline-delete.svg
│   │   │   ├── LICENSE
│   │   │   ├── README.txt
│   │   │   ├── search.svg
│   │   │   ├── selector-icons.svg
│   │   │   ├── sorting-icons.svg
│   │   │   ├── tooltag-add.svg
│   │   │   └── tooltag-arrowright.svg
│   │   ├── js/
│   │   │   ├── admin/
│   │   │   │   ├── DateTimeShortcuts.js
│   │   │   │   └── RelatedObjectLookups.js
│   │   │   ├── vendor/
│   │   │   │   ├── jquery/
│   │   │   │   │   ├── jquery.js
│   │   │   │   │   ├── jquery.min.js
│   │   │   │   │   └── LICENSE.txt
│   │   │   │   ├── select2/
│   │   │   │   │   ├── i18n/
│   │   │   │   │   │   ├── af.js
│   │   │   │   │   │   ├── ar.js
│   │   │   │   │   │   ├── az.js
│   │   │   │   │   │   ├── bg.js
│   │   │   │   │   │   ├── bn.js
│   │   │   │   │   │   ├── bs.js
│   │   │   │   │   │   ├── ca.js
│   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   ├── dsb.js
│   │   │   │   │   │   ├── el.js
│   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   ├── es.js
│   │   │   │   │   │   ├── et.js
│   │   │   │   │   │   ├── eu.js
│   │   │   │   │   │   ├── fa.js
│   │   │   │   │   │   ├── fi.js
│   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   ├── he.js
│   │   │   │   │   │   ├── hi.js
│   │   │   │   │   │   ├── hr.js
│   │   │   │   │   │   ├── hsb.js
│   │   │   │   │   │   ├── hu.js
│   │   │   │   │   │   ├── hy.js
│   │   │   │   │   │   ├── id.js
│   │   │   │   │   │   ├── is.js
│   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   ├── ja.js
│   │   │   │   │   │   ├── ka.js
│   │   │   │   │   │   ├── km.js
│   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   ├── lt.js
│   │   │   │   │   │   ├── lv.js
│   │   │   │   │   │   ├── mk.js
│   │   │   │   │   │   ├── ms.js
│   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   ├── ne.js
│   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   ├── ps.js
│   │   │   │   │   │   ├── pt-BR.js
│   │   │   │   │   │   ├── pt.js
│   │   │   │   │   │   ├── ro.js
│   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   ├── sk.js
│   │   │   │   │   │   ├── sl.js
│   │   │   │   │   │   ├── sq.js
│   │   │   │   │   │   ├── sr-Cyrl.js
│   │   │   │   │   │   ├── sr.js
│   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   ├── th.js
│   │   │   │   │   │   ├── tk.js
│   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   ├── uk.js
│   │   │   │   │   │   ├── vi.js
│   │   │   │   │   │   ├── zh-CN.js
│   │   │   │   │   │   └── zh-TW.js
│   │   │   │   │   ├── LICENSE.md
│   │   │   │   │   ├── select2.full.js
│   │   │   │   │   └── select2.full.min.js
│   │   │   │   └── xregexp/
│   │   │   │   │   ├── LICENSE.txt
│   │   │   │   │   ├── xregexp.js
│   │   │   │   │   └── xregexp.min.js
│   │   │   ├── actions.js
│   │   │   ├── autocomplete.js
│   │   │   ├── calendar.js
│   │   │   ├── cancel.js
│   │   │   ├── change_form.js
│   │   │   ├── collapse.js
│   │   │   ├── core.js
│   │   │   ├── inlines.js
│   │   │   ├── jquery.init.js
│   │   │   ├── nav_sidebar.js
│   │   │   ├── popup_response.js
│   │   │   ├── prepopulate_init.js
│   │   │   ├── prepopulate.js
│   │   │   ├── SelectBox.js
│   │   │   ├── SelectFilter2.js
│   │   │   └── urlify.js
│   │   └── .DS_Store
│   └── .DS_Store
├── salonapp/
│   ├── __pycache__/
│   │   ├── __init__.cpython-39.pyc
│   │   ├── admin.cpython-39.pyc
│   │   ├── apps.cpython-39.pyc
│   │   ├── models.cpython-39.pyc
│   │   ├── urls.cpython-39.pyc
│   │   └── views.cpython-39.pyc
│   ├── migrations/
│   │   ├── __pycache__/
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   └── 0001_initial.cpython-39.pyc
│   │   ├── __init__.py
│   │   ├── .DS_Store
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20210801_0023.py
│   │   └── 0003_payment.py
│   ├── static/
│   │   ├── admin/
│   │   │   ├── css/
│   │   │   │   ├── vendor/
│   │   │   │   │   └── select2/
│   │   │   │   │   │   ├── LICENSE-SELECT2.md
│   │   │   │   │   │   ├── select2.css
│   │   │   │   │   │   └── select2.min.css
│   │   │   │   ├── autocomplete.css
│   │   │   │   ├── base.css
│   │   │   │   ├── changelists.css
│   │   │   │   ├── dashboard.css
│   │   │   │   ├── fonts.css
│   │   │   │   ├── forms.css
│   │   │   │   ├── login.css
│   │   │   │   ├── nav_sidebar.css
│   │   │   │   ├── responsive_rtl.css
│   │   │   │   ├── responsive.css
│   │   │   │   ├── rtl.css
│   │   │   │   └── widgets.css
│   │   │   ├── fonts/
│   │   │   │   ├── LICENSE.txt
│   │   │   │   ├── README.txt
│   │   │   │   ├── Roboto-Bold-webfont.woff
│   │   │   │   ├── Roboto-Light-webfont.woff
│   │   │   │   └── Roboto-Regular-webfont.woff
│   │   │   ├── img/
│   │   │   │   ├── gis/
│   │   │   │   │   ├── move_vertex_off.svg
│   │   │   │   │   └── move_vertex_on.svg
│   │   │   │   ├── calendar-icons.svg
│   │   │   │   ├── icon-addlink.svg
│   │   │   │   ├── icon-alert.svg
│   │   │   │   ├── icon-calendar.svg
│   │   │   │   ├── icon-changelink.svg
│   │   │   │   ├── icon-clock.svg
│   │   │   │   ├── icon-deletelink.svg
│   │   │   │   ├── icon-no.svg
│   │   │   │   ├── icon-unknown-alt.svg
│   │   │   │   ├── icon-unknown.svg
│   │   │   │   ├── icon-viewlink.svg
│   │   │   │   ├── icon-yes.svg
│   │   │   │   ├── inline-delete.svg
│   │   │   │   ├── LICENSE
│   │   │   │   ├── README.txt
│   │   │   │   ├── search.svg
│   │   │   │   ├── selector-icons.svg
│   │   │   │   ├── sorting-icons.svg
│   │   │   │   ├── tooltag-add.svg
│   │   │   │   └── tooltag-arrowright.svg
│   │   │   ├── js/
│   │   │   │   ├── admin/
│   │   │   │   │   ├── DateTimeShortcuts.js
│   │   │   │   │   └── RelatedObjectLookups.js
│   │   │   │   ├── vendor/
│   │   │   │   │   ├── jquery/
│   │   │   │   │   │   ├── jquery.js
│   │   │   │   │   │   ├── jquery.min.js
│   │   │   │   │   │   └── LICENSE.txt
│   │   │   │   │   ├── select2/
│   │   │   │   │   │   ├── i18n/
│   │   │   │   │   │   │   ├── af.js
│   │   │   │   │   │   │   ├── ar.js
│   │   │   │   │   │   │   ├── az.js
│   │   │   │   │   │   │   ├── bg.js
│   │   │   │   │   │   │   ├── bn.js
│   │   │   │   │   │   │   ├── bs.js
│   │   │   │   │   │   │   ├── ca.js
│   │   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   │   ├── dsb.js
│   │   │   │   │   │   │   ├── el.js
│   │   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   │   ├── es.js
│   │   │   │   │   │   │   ├── et.js
│   │   │   │   │   │   │   ├── eu.js
│   │   │   │   │   │   │   ├── fa.js
│   │   │   │   │   │   │   ├── fi.js
│   │   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   │   ├── he.js
│   │   │   │   │   │   │   ├── hi.js
│   │   │   │   │   │   │   ├── hr.js
│   │   │   │   │   │   │   ├── hsb.js
│   │   │   │   │   │   │   ├── hu.js
│   │   │   │   │   │   │   ├── hy.js
│   │   │   │   │   │   │   ├── id.js
│   │   │   │   │   │   │   ├── is.js
│   │   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   │   ├── ja.js
│   │   │   │   │   │   │   ├── ka.js
│   │   │   │   │   │   │   ├── km.js
│   │   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   │   ├── lt.js
│   │   │   │   │   │   │   ├── lv.js
│   │   │   │   │   │   │   ├── mk.js
│   │   │   │   │   │   │   ├── ms.js
│   │   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   │   ├── ne.js
│   │   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   │   ├── ps.js
│   │   │   │   │   │   │   ├── pt-BR.js
│   │   │   │   │   │   │   ├── pt.js
│   │   │   │   │   │   │   ├── ro.js
│   │   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   │   ├── sk.js
│   │   │   │   │   │   │   ├── sl.js
│   │   │   │   │   │   │   ├── sq.js
│   │   │   │   │   │   │   ├── sr-Cyrl.js
│   │   │   │   │   │   │   ├── sr.js
│   │   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   │   ├── th.js
│   │   │   │   │   │   │   ├── tk.js
│   │   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   │   ├── uk.js
│   │   │   │   │   │   │   ├── vi.js
│   │   │   │   │   │   │   ├── zh-CN.js
│   │   │   │   │   │   │   └── zh-TW.js
│   │   │   │   │   │   ├── LICENSE.md
│   │   │   │   │   │   ├── select2.full.js
│   │   │   │   │   │   └── select2.full.min.js
│   │   │   │   │   └── xregexp/
│   │   │   │   │   │   ├── LICENSE.txt
│   │   │   │   │   │   ├── xregexp.js
│   │   │   │   │   │   └── xregexp.min.js
│   │   │   │   ├── actions.js
│   │   │   │   ├── autocomplete.js
│   │   │   │   ├── calendar.js
│   │   │   │   ├── cancel.js
│   │   │   │   ├── change_form.js
│   │   │   │   ├── collapse.js
│   │   │   │   ├── core.js
│   │   │   │   ├── inlines.js
│   │   │   │   ├── jquery.init.js
│   │   │   │   ├── nav_sidebar.js
│   │   │   │   ├── popup_response.js
│   │   │   │   ├── prepopulate_init.js
│   │   │   │   ├── prepopulate.js
│   │   │   │   ├── SelectBox.js
│   │   │   │   ├── SelectFilter2.js
│   │   │   │   └── urlify.js
│   │   │   └── .DS_Store
│   │   ├── assets/
│   │   │   └── .DS_Store
│   │   └── .DS_Store
│   ├── __init__.py
│   ├── .DS_Store
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── salonproject/
│   ├── __pycache__/
│   │   ├── __init__.cpython-39.pyc
│   │   ├── settings.cpython-39.pyc
│   │   ├── urls.cpython-39.pyc
│   │   └── wsgi.cpython-39.pyc
│   ├── __init__.py
│   ├── .DS_Store
│   ├── asgi.py
│   ├── settings.py
│   ├── temp.py
│   ├── urls.py
│   └── wsgi.py
├── staticfiles/
│   ├── admin/
│   │   ├── css/
│   │   │   ├── vendor/
│   │   │   │   └── select2/
│   │   │   │   │   ├── LICENSE-SELECT2.md
│   │   │   │   │   ├── select2.css
│   │   │   │   │   └── select2.min.css
│   │   │   ├── autocomplete.css
│   │   │   ├── base.css
│   │   │   ├── changelists.css
│   │   │   ├── dashboard.css
│   │   │   ├── fonts.css
│   │   │   ├── forms.css
│   │   │   ├── login.css
│   │   │   ├── nav_sidebar.css
│   │   │   ├── responsive_rtl.css
│   │   │   ├── responsive.css
│   │   │   ├── rtl.css
│   │   │   └── widgets.css
│   │   ├── fonts/
│   │   │   ├── LICENSE.txt
│   │   │   ├── README.txt
│   │   │   ├── Roboto-Bold-webfont.woff
│   │   │   ├── Roboto-Light-webfont.woff
│   │   │   └── Roboto-Regular-webfont.woff
│   │   ├── img/
│   │   │   ├── gis/
│   │   │   │   ├── move_vertex_off.svg
│   │   │   │   └── move_vertex_on.svg
│   │   │   ├── calendar-icons.svg
│   │   │   ├── icon-addlink.svg
│   │   │   ├── icon-alert.svg
│   │   │   ├── icon-calendar.svg
│   │   │   ├── icon-changelink.svg
│   │   │   ├── icon-clock.svg
│   │   │   ├── icon-deletelink.svg
│   │   │   ├── icon-no.svg
│   │   │   ├── icon-unknown-alt.svg
│   │   │   ├── icon-unknown.svg
│   │   │   ├── icon-viewlink.svg
│   │   │   ├── icon-yes.svg
│   │   │   ├── inline-delete.svg
│   │   │   ├── LICENSE
│   │   │   ├── README.txt
│   │   │   ├── search.svg
│   │   │   ├── selector-icons.svg
│   │   │   ├── sorting-icons.svg
│   │   │   ├── tooltag-add.svg
│   │   │   └── tooltag-arrowright.svg
│   │   ├── js/
│   │   │   ├── admin/
│   │   │   │   ├── DateTimeShortcuts.js
│   │   │   │   └── RelatedObjectLookups.js
│   │   │   ├── vendor/
│   │   │   │   ├── jquery/
│   │   │   │   │   ├── jquery.js
│   │   │   │   │   ├── jquery.min.js
│   │   │   │   │   └── LICENSE.txt
│   │   │   │   ├── select2/
│   │   │   │   │   ├── i18n/
│   │   │   │   │   │   ├── af.js
│   │   │   │   │   │   ├── ar.js
│   │   │   │   │   │   ├── az.js
│   │   │   │   │   │   ├── bg.js
│   │   │   │   │   │   ├── bn.js
│   │   │   │   │   │   ├── bs.js
│   │   │   │   │   │   ├── ca.js
│   │   │   │   │   │   ├── cs.js
│   │   │   │   │   │   ├── da.js
│   │   │   │   │   │   ├── de.js
│   │   │   │   │   │   ├── dsb.js
│   │   │   │   │   │   ├── el.js
│   │   │   │   │   │   ├── en.js
│   │   │   │   │   │   ├── es.js
│   │   │   │   │   │   ├── et.js
│   │   │   │   │   │   ├── eu.js
│   │   │   │   │   │   ├── fa.js
│   │   │   │   │   │   ├── fi.js
│   │   │   │   │   │   ├── fr.js
│   │   │   │   │   │   ├── gl.js
│   │   │   │   │   │   ├── he.js
│   │   │   │   │   │   ├── hi.js
│   │   │   │   │   │   ├── hr.js
│   │   │   │   │   │   ├── hsb.js
│   │   │   │   │   │   ├── hu.js
│   │   │   │   │   │   ├── hy.js
│   │   │   │   │   │   ├── id.js
│   │   │   │   │   │   ├── is.js
│   │   │   │   │   │   ├── it.js
│   │   │   │   │   │   ├── ja.js
│   │   │   │   │   │   ├── ka.js
│   │   │   │   │   │   ├── km.js
│   │   │   │   │   │   ├── ko.js
│   │   │   │   │   │   ├── lt.js
│   │   │   │   │   │   ├── lv.js
│   │   │   │   │   │   ├── mk.js
│   │   │   │   │   │   ├── ms.js
│   │   │   │   │   │   ├── nb.js
│   │   │   │   │   │   ├── ne.js
│   │   │   │   │   │   ├── nl.js
│   │   │   │   │   │   ├── pl.js
│   │   │   │   │   │   ├── ps.js
│   │   │   │   │   │   ├── pt-BR.js
│   │   │   │   │   │   ├── pt.js
│   │   │   │   │   │   ├── ro.js
│   │   │   │   │   │   ├── ru.js
│   │   │   │   │   │   ├── sk.js
│   │   │   │   │   │   ├── sl.js
│   │   │   │   │   │   ├── sq.js
│   │   │   │   │   │   ├── sr-Cyrl.js
│   │   │   │   │   │   ├── sr.js
│   │   │   │   │   │   ├── sv.js
│   │   │   │   │   │   ├── th.js
│   │   │   │   │   │   ├── tk.js
│   │   │   │   │   │   ├── tr.js
│   │   │   │   │   │   ├── uk.js
│   │   │   │   │   │   ├── vi.js
│   │   │   │   │   │   ├── zh-CN.js
│   │   │   │   │   │   └── zh-TW.js
│   │   │   │   │   ├── LICENSE.md
│   │   │   │   │   ├── select2.full.js
│   │   │   │   │   └── select2.full.min.js
│   │   │   │   └── xregexp/
│   │   │   │   │   ├── LICENSE.txt
│   │   │   │   │   ├── xregexp.js
│   │   │   │   │   └── xregexp.min.js
│   │   │   ├── actions.js
│   │   │   ├── autocomplete.js
│   │   │   ├── calendar.js
│   │   │   ├── cancel.js
│   │   │   ├── change_form.js
│   │   │   ├── collapse.js
│   │   │   ├── core.js
│   │   │   ├── inlines.js
│   │   │   ├── jquery.init.js
│   │   │   ├── nav_sidebar.js
│   │   │   ├── popup_response.js
│   │   │   ├── prepopulate_init.js
│   │   │   ├── prepopulate.js
│   │   │   ├── SelectBox.js
│   │   │   ├── SelectFilter2.js
│   │   │   └── urlify.js
│   │   └── .DS_Store
│   └── .DS_Store
├── templates/
│   ├── users/
│   │   └── index.html
│   ├── .DS_Store
│   ├── about.html
│   ├── calendar.html
│   ├── clients.html
│   ├── contact.html
│   ├── login.html
│   ├── payment.html
│   ├── profile.html
│   └── register.html
├── .DS_Store
├── .env
├── .gitignore
├── app.json
├── app.py
├── db.sqlite3
├── latest.dump
├── LICENSE.txt
├── manage.py
├── Procfile
├── README.md
├── requirements.txt
└── runtime.txt
```