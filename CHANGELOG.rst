=============
Release Notes
=============


Version 1.0
-----------

1.0.1 2023-07-31
~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Fixes

- Bump python version to 3.8.15 since 3.7 is not officially supported any longer und thus causes
  problems with bioconda.
- Relax (sub)version pinning of several dependencies to enable building on bioconda.
- Fix failing publish action in CI.
- Fix a known security vulnerability (CVE-2022-21797) by updating joblib to 1.2.

1.0.0 2023-06-21
~~~~~~~~~~~~~~~~~~~~~~~~~

Initial release.
