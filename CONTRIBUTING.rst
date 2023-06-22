============
Contributing
============

Welcome to ``geno2phenoTB`` contributor's guide.

This document focuses on getting any potential contributor familiarized
with the development processes, but `other kinds of contributions`_ are also
appreciated.

If you are new to using git_ or have never collaborated in a project previously,
please have a look at `contribution-guide.org`_. Other resources are also
listed in the excellent `guide by FreeCodeCamp`_.

Please notice, all users and contributors are expected to be **open,
considerate, reasonable, and respectful**. When in doubt, `Python Software
Foundation's Code of Conduct`_ is a good reference in terms of behavior
guidelines.


Issue Reports
=============

If you experience bugs or general issues with ``geno2phenoTB``, please have a look
on the `issue tracker`_. If you don't see anything useful there, please feel
free to fire an issue report.

   .. tip::
      Please don't forget to include the closed issues in your search.
      Sometimes a solution was already reported, and the problem is considered
      **solved**.

New issue reports should include information about your programming environment
(e.g., operating system, Python version) and steps to reproduce the problem.
Please try also to simplify the reproduction steps to a very minimal example
that still illustrates the problem you are facing. By removing other factors,
you help us to identify the root cause of the issue.

Code and Documentation Contributions
=====================================

Submit an issue
---------------

Before you work on any non-trivial code contribution it's best to first create
a report in the `issue tracker`_ to start a discussion on the subject.
This often provides additional considerations and avoids unnecessary work.


Clone and set up the repository
-------------------------------

#. Create an user account on |the repository service| if you do not already have one.
#. Fork the project repository_: click on the *Fork* button near the top of the
   page. This creates a copy of the code under your account on |the repository service|.
#. Clone this copy to your local disk::

    git clone git@github.com:YourLogin/geno2phenoTB.git
    cd geno2phenoTB

#. Create an isolated `conda` environment with the required dependencies to avoid any problems with
   your installed Python packages::

    conda env create -f tests/g2p-test.yaml
    conda rename -n g2p-test g2p-dev
    conda activate g2p-dev

#. Next, run::

    pip install -U pip setuptools -e ".[dev]"

   to install further packages required for development and to enable importing the package under development in the Python REPL.

#. Install |pre-commit|_::

    pre-commit install

   ``geno2phenoTB`` comes with a lot of hooks configured to help the
   developer to check the code being written automatically.

Documentation Improvements
--------------------------

You can help to improve the ``geno2phenoTB`` docs by making them more readable and coherent, or
by adding missing information and correcting mistakes.

The ``geno2phenoTB`` documentation uses Sphinx_ as its main documentation compiler.
This means that the docs are kept in the same repository as the project code, and
that any documentation update is done in the same way was a code contribution.

reStructuredText_ is used.

   .. tip::
      Please notice that the `GitHub web interface`_ provides a quick way of
      propose changes in ``geno2phenoTB``'s files. While this mechanism can
      be tricky for normal code contributions, it works perfectly fine for
      contributing to the docs, and can be quite handy.

      If you are interested in trying this method out, please navigate to the
      ``docs`` folder in the source repository_, select the file for which you
      would like to propose changes, and click in the little pencil icon at the
      top, to open `GitHub's code editor`_. Once you finished editing the file,
      please write a message in the description field at the bottom of the page
      describing the changes you made and the motivations behind them
      and submit your proposal.

When working on documentation changes in your local machine, you can
compile them using::

    cd docs
    make html

while being in the `docs` directory.
Use Python's built-in web server for a preview in your web browser (``http://localhost:8000``)::

    python3 -m http.server --directory 'docs/_build/html'

When you're done editing, do::

    git add <MODIFIED FILES>
    git commit

to record your changes in git_.

Please make sure to see the validation messages from |pre-commit|_ and fix
any potential issues.


Code Contributions
------------------

#. Create a branch to hold your changes::

    git checkout -b my-feature-name

   and start making changes. **Never work on the main branch!**

#. Start your work on this branch. Don't forget to add docstrings_ to new
   functions, modules, and classes, especially if they are part of public APIs.

      .. important:: Don't forget to add unit tests and documentation in case your
         contribution adds an additional feature and is not simply a bugfix.

#. Add yourself to the list of contributors in ``AUTHORS.rst``.

#. While developing, you should regularly check that your changes don't break unit tests with::

    pytest .

#. Finally, check that your changes pass all unit and self tests with::

    geno2phenotb test -f # fast test
    geno2phenotb test -c # complete test

#. When you're done editing, do::

    git add <MODIFIED FILES>
    git commit

   to record your changes in git_.

   Please make sure to inspect the validation messages from |pre-commit|_ and fix
   any eventual issues.

   Moreover, writing a `descriptive commit message`_ is highly recommended.
   In case of doubt, you can check the commit history with::

    git log --graph --decorate --pretty=oneline --abbrev-commit --all

   to look for recurring communication patterns.

Isolated build testing
----------------------
In order to test that everything works in an isolated build, this project uses act_ to run
GitHub Actions locally.

Download and install Act from here: https://github.com/nektos/act and run::

    act --artifact-server-path ./build/

The first run takes a while, since a clean docker container has to be be downloaded (~12GB).

Submit your contribution
------------------------

#. If everything works fine, push your local branch to |the repository service| with::

    git push -u origin my-feature-name

#. Go to the web page of your fork and click |contribute button|
   to submit your changes for review.


.. <-- strart -->
.. |the repository service| replace:: GitHub
.. |contribute button| replace:: "Create pull request"

.. _repository: https://github.com/msmdev/geno2phenoTB
.. _issue tracker: https://github.com/msmdev/geno2phenoTB/issues
.. <-- end -->


.. |virtualenv| replace:: ``virtualenv``
.. |pre-commit| replace:: ``pre-commit``
.. |tox| replace:: ``tox``


.. _act: https://github.com/nektos/act
.. _black: https://pypi.org/project/black/
.. _CommonMark: https://commonmark.org/
.. _contribution-guide.org: https://www.contribution-guide.org/
.. _creating a PR: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
.. _descriptive commit message: https://cbea.ms/git-commit/
.. _docstrings: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
.. _first-contributions tutorial: https://github.com/firstcontributions/first-contributions
.. _flake8: https://flake8.pycqa.org/en/stable/
.. _git: https://git-scm.com
.. _GitHub's fork and pull request workflow: https://guides.github.com/activities/forking/
.. _guide by FreeCodeCamp: https://github.com/FreeCodeCamp/how-to-contribute-to-open-source
.. _Miniconda: https://docs.conda.io/en/latest/miniconda.html
.. _MyST: https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html
.. _other kinds of contributions: https://opensource.guide/how-to-contribute
.. _pre-commit: https://pre-commit.com/
.. _PyPI: https://pypi.org/
.. _PyScaffold's contributor's guide: https://pyscaffold.org/en/stable/contributing.html
.. _Pytest can drop you: https://docs.pytest.org/en/stable/how-to/failures.html#using-python-library-pdb-with-pytest
.. _Python Software Foundation's Code of Conduct: https://www.python.org/psf/conduct/
.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _tox: https://tox.wiki/en/stable/
.. _virtual environment: https://realpython.com/python-virtual-environments-a-primer/
.. _virtualenv: https://virtualenv.pypa.io/en/stable/

.. _GitHub web interface: https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files
.. _GitHub's code editor: https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files
