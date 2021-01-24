##################
setStickerSetThumb
##################

Returns: :obj:`bool`

.. automodule:: aiogram.methods.set_sticker_set_thumb
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: bool = await bot.set_sticker_set_thumb(...)


Method as object
----------------

Imports:

- :code:`from aiogram.methods.set_sticker_set_thumb import SetStickerSetThumb`
- alias: :code:`from aiogram.methods import SetStickerSetThumb`

In handlers with current bot
----------------------------

.. code-block:: python

    result: bool = await SetStickerSetThumb(...)

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: bool = await bot(SetStickerSetThumb(...))

As reply into Webhook in handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    return SetStickerSetThumb(...)