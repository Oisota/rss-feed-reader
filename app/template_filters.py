"""Custom Template Filters for Jinja"""

def date_filter(date_obj, format_str):
    """Format date"""
    return date_obj.strftime(format_str)

def register_filters(app):
    app.jinja_env.filters['date'] = date_filter