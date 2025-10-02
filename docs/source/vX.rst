.. _vX_header:

vX (Deprecated)
===============

.. warning::
    **🚨 DEPRECATED**: The VX client and its methods are deprecated and will be removed in a future version.
    
    **👉 NEW**: Use the modern :doc:`Fundamentals` API instead for better performance and cleaner access to financial data.
    
    **Migration Guide**: See :doc:`Fundamentals` for migration examples and new endpoint documentation.

.. note::
    To call vX methods, use the vx class member on RESTClient.

    For example, :code:`financials = RESTClient().vx.list_stock_financials()`
    
    **⚠️ This will show deprecation warnings in your code.**

======================
List stock financials (Deprecated)
===================================

- `Stocks financials vX`_

.. automethod:: polygon.rest.VXClient.list_stock_financials

.. _Stocks financials vX: https://polygon.io/docs/stocks/get_vx_reference_financials
