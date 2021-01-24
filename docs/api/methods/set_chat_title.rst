############
setChatTitle
############

Returns: :obj:`bool`

.. automodule:: aiogram.methods.set_chat_title
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: bool = await bot.set_chat_title(...)


Method as object
----------------

Imports:

- :code:`from aiogram.methods.set_chat_title import SetChatTitle`
- alias: :code:`from aiogram.methods import SetChatTitle`

In handlers with current bot
----------------------------

.. code-block:: python

    result: bool = await SetChatTitle(...)

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: bool = await bot(SetChatTitle(...))

As reply into Webhook in handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    return SetChatTitle(...)