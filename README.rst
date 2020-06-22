=========================
sphinxcontrib-googlefonts
=========================

You can use Google Fonts for easy in sphinx documentation.

Overview
========

This is small sphinx-extension to provide feature for configuration of Google Fonts.
If you want use Google Fonts in sphinx documentation, you can realize by few codes.

Usage
=====

#. Install package
#. Configure your ``conf.py`` 
#. Declare fonts to use by you
#. Write style in your custom CSS.

Installation:

.. code-block:: bash

    pip install https://github.com/attakei-sandbox/sphinxcontrib-googlefonts/releases/download/v0.1.0/sphinxcontrib_googlefonts-0.1.0-py3-none-any.whl

Configure:

.. code-block:: python

    extensions = [
      "sphinxcontrib.googlefonts",
    ]

    # Example: use multiple fonts
    googlefonts_families = [
      "Roboto",
      "Noto Sans JP",
    ]

.. code-block:: css

    body {
      font-family: 'Roboto', sans-serif;
    }
    h1 {
      font-family: 'Noto Sans JP', sans-serif;
    }

Support fonts
=============

If you find fonts, go to `Google Fonts website <https://fonts.google.com>`_.

To do
=====

* Support any parameters of Google Fonts API.
* Shorthand config to apply fonts for simple selector
