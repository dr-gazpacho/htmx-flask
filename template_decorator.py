# https://flask.palletsprojects.com/en/2.3.x/patterns/viewdecorators/#templating-decorator
# This could let me simplify the render_template function
# It would let me just return a dictionary of all the values I want to assign to my htmx template

from functools import wraps
from flask import request, render_template

def templated(template=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = f"{request.endpoint.replace('.', '/')}.html"
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator