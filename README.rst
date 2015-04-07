lisense
=======

    Sensible repository licensing for Humans
    
**Sir Isaac Newton once said that**
    *Open source simply isn't open source without a proper license. So add a license. Always.*

GitHub recently launched their `License API <https://developer.github.com/v3/licenses/>`__, it's still in preview stage though.
They also released a blog post showing `Open source license usage on GitHub.com <https://github.com/blog/1964-open-source-license-usage-on-github-com>`__, which is enough to convice you that why adding a license is 
`sine qua non <http://lmgtfy.com/?q=define+sine+qua+non>`__.
    

    *Newton and Open Source, Respect both, let us.*
    
    \- Yoda
    
lisense in action
~~~~~~~~~~~~~~~~~
.. figure:: https://raw.githubusercontent.com/pravj/lisense/master/docs/lisense.gif
   :alt: lisense


lisense. What?
~~~~~~~~~~~~~~
    lisense is a command-line tool which helps you license your projects.
- Lets you have a global configuration. Use your defaults, anywhere, anytime.
- Guides you about using a particular license, better than you uncle.
- And yes! Generates licenses.

lisense. Controls?
~~~~~~~~~~~~~~~~~~
    Generating a license is more easy than doing nothing.
- lisense list
    List all available licenses.
- lisense guide [license]
    Provide guidance about a license. Description, use cases etc.
- lisense setup
    Setup global lisense configurations. Default license and owner name.
- lisense new [license] --owner="OWNER NAME"
    Generates new license. Both the *license* and *owner* arguments are optional. Uses defaults when not supplied.

Automatic extra context variable handling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Almost all the licenses have two common fields in them, *owner* and *year*. Some of them have extra fields also. For example, the GPL-v2 license
has a field *description*, which asks for the description of the project.

Lisense uses *jinja2*'s low level meta API to parse the abstract syntax tree of the template and interactively asks users to fill
extra fields, if any.

So, you don't have to worry about it.

Dependencies
~~~~~~~~~~~~
- `docopt <https://github.com/docopt/docopt>`__ - command-line argument parsing
- `jinja2 <https://github.com/mitsuhiko/jinja2>`__ - generate licenses from license templates
- `xtermcolor <https://github.com/broadinstitute/xtermcolor>`__ - colorful messages on terminal

-----

Built with :two_hearts: by `Pravendra Singh <http://pravj.github.io>`__
