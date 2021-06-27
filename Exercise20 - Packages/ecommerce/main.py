# Remember the Hierarchy:
# Package - Module - Function

# Code Below is Example of Module-Based Call:
from ecommerce import shipping
shipping.calc_shipping()


# Code Below is Example of Function-Based Calling:
from ecommerce.shipping import calc_shipping
calc_shipping()

# If more than one Module, simply add function in xx separated by ",":
# from ecommerce.shipping import calc_shipping , xx, etc...
# Example:
# from ecommerce.shipping import calc_shipping , calc_tax, calc_discount


# Code Below is Example of whole Module-Based Calling:
import ecommerce.shipping
ecommerce.shipping.calc_shipping()
