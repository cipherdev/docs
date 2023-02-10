Git How To
==========

Git Commands
------------

Remove an file to Commit
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: file_rm

    git reset --soft HEAD~1  #or git reset --soft HEAD^

Then reset the unwanted files in order to leave them out from the commit::

    git reset HEAD path/to/unwanted_file

.. Note:: That since Git 2.23.0 one can (the new way): git restore --staged path/to/unwanted_file

Now commit again, you can even re-use the same commit message::

    git commit -c ORIG_HEAD  


