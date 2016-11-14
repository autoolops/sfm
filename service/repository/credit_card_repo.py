#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: suyuan
@license: 
@contact: suyuan@gmail.com
@site: https://github.com/su6838354/sfm
@software: PyCharm
@file: credit_card_repo.py
@time: 16/11/14 下午7:35
"""



from service.repository.base_repo import BaseRepo
import logging
from tornado.concurrent import run_on_executor


class CreditCardRepo(BaseRepo):
    TABLE_NAME = 'sfm_credit_card'

    def __init__(self):
        logging.info('init CreditCardRepo')

    def insert(self, user_id, card_id, amount):
        sql = """
            insert into {} set user_id=%s, card_id=%s, amount=%s, remain_amount=%s
        """.format(self.TABLE_NAME)
        r_count = self.db.execute_rowcount(sql, user_id, card_id, amount, amount)
        return r_count

    def select(self, user_id):
        sql = """
            select * from {} where user_id=%s
        """.format(self.TABLE_NAME)
        credit_card = self.db.get(sql, user_id)
        return credit_card

    def update(self, cost_amount, card_id):
        sql = """
            update {} set remain_amount=remain_amount+%s where card_id=%s
        """.format(self.TABLE_NAME)
        res = self.db.execute_rowcount(sql, cost_amount, card_id)
        return res
