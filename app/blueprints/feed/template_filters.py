"""Custom Template Filters for Jinja"""

def date_filter(date_obj, format_str):
    """Format date"""
    return date_obj.strftime(format_str)

def register_filters(bp):
    bp.add_app_template_filter(date_filter, 'date')