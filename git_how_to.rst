Git How To
##########

.. code-block:: bash
   
   .PHONY: html
   html:
    $(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)
    @echo
    @echo "Build finished. The HTML pages are in $(BUILDDIR)."
 
Test

.. code-block:: bash
  :emphasize-lines: 3

  .PHONY: internalhtml
   internalhtml:
    $(SPHINXBUILD) -b html $(ALLSPHINXOPTS) -t Internal $(INTERNALBUILDDIR)
    @echo
    @echo "Build finished. The HTML pages are in $(INTERNALBUILDDIR)."

.. note:: This docker compose page.


