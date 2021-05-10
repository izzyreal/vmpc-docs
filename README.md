Documentation for VMPC2000XL: https://izmar.nl

[![Build Status](https://travis-ci.org/vmpc2000xl/docs.svg?branch=master)](https://travis-ci.org/vmpc2000xl/docs)

Credits
=======
The technical approach of this documentation is copied from [Conan C++ Package Manager docs](https://github.com/conan-io/docs>).

How to build
============

- Install python and [pip docs](https://pip.pypa.io/en/stable/installing/).
- Install the requirements (sphinx):

  `$ pip install -r requirements.txt`

- Build the documentation:

  `$ make html`

How to read the built docs
==========================

Open a browser and select the *_build/html/index.html* file.

Example:

`$ firefox _build/html/index.html`

How to contribute
=================

To make any contribution to VMPC2000XL documentation fork this repository and open a Pull Request.

Style Guidelines
----------------

These guidelines are just general good practices for the formatting and structure of the whole documentation and do not pretend to be a
stopper for any helpful contribution. Any contribution that may include relevant information for VMPC2000XL users will always be welcomed.

VMPC2000XL documentation is written in [reStructuredText](http://docutils.sourceforge.net/rst.html) and
follows [reStructuredText Markup Specification](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html).

[Quick reStructuredText](http://docutils.sourceforge.net/docs/user/rst/quickref.html) is also used for reference.

Any detail not covered by this guidelines will follow the aforementioned rules.

### Section titles

Use section titles in this level of importance:

```
Section Title
=============

Section Title
-------------

Section Title
+++++++++++++

Section Title
^^^^^^^^^^^^^
```

### Text emphasis/highlighting

- **Bold text** to highlight important text:

  ```
  **Demo recovery data:** Demo beats that are never modified by VMPC2000XL
  ```

- `Inline literals` to refer to file names, directory names, paths, terminal commands, keypresses, screen names, literal references to UI and LCD text and code:

  ```
  Click on the :code:`Options` button in the top-left and click :code:`Audio/MIDI Settings`.
  ```

### Indentation and line length

Make sure all indentation is done with spaces. Normally 2 space indentation for bulleted lists and 4 space indentation for code blocks. In some
cases a 3 space indentation is needed for reStructuredText specifics like toc-trees:

```
.. toctree::
   :maxdepth: 2

   introduction
   installation
```

The **maximum line length for documentation is 140 characters** except for lines inside code-blocks, external links or references.

Do not leave any unnecessary or trailing spaces.

### References

References are commonly used in the documentation and it's always a good way to highlight texts and give an implicit or explicit importance
to something.

#### Internal reference

Use an internal reference when you want to refer to a specific section in this documentation. Most of the sections have a reference mark
just before their names so you can reference it.

```
.. _manual_installation_for_ubuntu:

Manual installation (Ubuntu 18)
-------------------------------

...
```

To add a reference to the Manual installation (Ubuntu 18) section from another text:

```
If you have followed the recommendations of the :ref:`Manual installation (Ubuntu 18) <manual_installation_for_ubuntu>` section, ...
```

#### External references

Use external references like this:

```
Please refer to the `MPC2000XL manual <https://www.platinumaudiolab.com/free_stuff/manuals/Akai/akai_mpc2000xl_manual.pdf>`_ to see the details of this process.
```
