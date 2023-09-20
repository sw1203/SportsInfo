#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

from importlib import import_module

def get_env(name):
    try:
        env_local = import_module('common.env_local')
        return getattr(env_local, name)
    except ImportError as e:
        if str(e.msg).startswith('No module'):
            # env_local이 없는 경우 env를 이용
            return globals()[name]
        raise
    except AttributeError:
        # env_local에 name이 없는 경우 env.name을 이용
        return globals()[name]
    # 그 외에는 env_local의 오류이고 심각한 상황을 발생시킬 수 있으므로
    # exception을 방치해서 프로그램 종료

# DB config
DB_CONFIG = {}

# googlesheet
