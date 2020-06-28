  
# -*- coding: utf-8 -*-
"""
*************
Documentation
*************
This will add a special title to this section automatically :D 
"""

class MegaClass:
  """
  This is the class text
  """

  def __init__(self, input_: str):
    """
    :param [input_]: A character string that represents the filepath and filename of the file to open.
    :type [input_]: String
    """
    self.input_ = input_
  
  def imul(self) -> int:
    """
    This is the method text

    :return: Your number times 2
    :rtype: Int
    """
    return self.input_ * 2
