# -*- coding: utf-8 -*-
"""
    templating
    ~~~~~~~~~~


"""

from flask.templating import _render
from flask.globals import _app_ctx_stack

def render(template_name_or_list, **context):
    ctx = _app_ctx_stack.top
    ctx.app.update_template_context(context)
    return _render(ctx.app.jinja_env.get_or_select_template(template_name_or_list),
                   context, ctx.app)