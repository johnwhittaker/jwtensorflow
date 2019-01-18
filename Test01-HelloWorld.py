# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 10:38:39 2019

@author: john_
"""

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
session = tf.Session()
print(session.run(hello))

