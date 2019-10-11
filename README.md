## Unit Testing Assignment

[![Build Status](https://travis-ci.com/patdpat/unittesting-patdpat.svg?branch=master)](https://travis-ci.com/patdpat/unittesting-patdpat)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub followers](https://img.shields.io/github/followers/patdpat.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/Naereen?tab=followers)

by Sidtipat 6110546046

## Test Cases for unique

Write a table describing your test cases.

| Test case                                          | Expected Result                               |
| -------------------------------------------------- | --------------------------------------------- |
| none check                                         | some list,not none                            |
| empty list                                         | []                                            |
| single items without duplicates in various order   | list with 1 item no duplication found         |
| single items with duplicates in various order      | list with 1 item no duplication found         |
| multiple items without duplicates in various order | list with multiple items no duplication found |
| multiple items with duplicates in various order    | list with multiple items no duplication found |
| list of unique 10000000 items                      | list of 10000000 items no duplication found   |

## Test Cases for Fraction

| Test case (**init**)             | Expected Result                             |
| -------------------------------- | ------------------------------------------- |
| test numerator                   | numerator encapsulate in self.numerator     |
| test denominator                 | denominator encapsulate in self.denominator |
| test for zero value in numerator | zero                                        |

| Test case(**str**)                               | Expected Result       |
| ------------------------------------------------ | --------------------- |
| postive numerator and negative denominator       | negative fraction     |
| numerator equal to zero                          | zero                  |
| positive numerator and positive denominator      | positive fraction     |
| negative numerator and 1 as denominator          | negative whole number |
| any integer as numerator and zero as denominator | nan(not a number)     |

| Test case(**eq**)                              | Expected Result                     |
| ---------------------------------------------- | ----------------------------------- |
| two exact fractions                            | True                                |
| same value fractions different expression      | True                                |
| different value fractions different expression | False                               |
| zero and zero different denominator            | True                                |
| any numerator with zero as denominator         | the value of fraction equals to nan |

| Test case (**add**)                                     | Expected Result             |
| ------------------------------------------------------- | --------------------------- |
| two positive fraction                                   | positive addition result    |
| one positive add with one negative                      | positive subtraction result |
| positive fraction and negative fraction with same value | zero                        |
| two negative fraction                                   | negative addition result    |
| negative fraction and positive fraction with same value | zero                        |

| Test case (**mul**)                                     | Expected Result                                  |
| ------------------------------------------------------- | ------------------------------------------------ |
| two positive fraction                                   | positive multiplication result                   |
| one positive add with one negative                      | negative multiplication result                   |
| positive fraction and negative fraction with same value | negative with power of 2 to the origina fraction |
| two negative fraction                                   | positive multiplication result                   |
| some fraction with zero                                 | zero                                             |
