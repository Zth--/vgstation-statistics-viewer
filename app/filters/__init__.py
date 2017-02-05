"""Helpers for our Jinja2 templates."""
from app import app
import calendar


@app.template_filter('format_timestamp')
def format_timestamp(value, format='matchtime'):
    """Format textual timestamps into more readable timestamps."""
    if format == 'matchtime':
        # yyyy mm dd hh mm ss
        value = value.split('.')
        return "{} {} {}:{}".format(calendar.month_name[int(value[1])], int(value[2]), int(value[3]), value[4])
    elif format == 'shortmatchtime':
        value = value.split('.')
        return "{}/{} {}:{}".format(int(value[1]), int(value[2]), int(value[3]), value[4])
    elif format == 'hhmm':  # datetime hour/min
        value = value.split('.')
        return "{}:{}".format(value[4], value[5])


@app.template_filter('obj_successfail')
def obj_successfail(succeeded):
    """Return a styled span to show if an antag was successful or not.

    Keyword arguments:
    succeeded -- Boolean. Did the antag win?
    """
    if succeeded:
        return "<span class='objective success'>Success</span>"
    else:
        return "<span class='objective failure'>Failure</span>"


@app.template_filter('obj_pretty')
def obj_pretty(objective):
    """Make antag objectives pretty for template views."""
    if objective.objective_type == u'/datum/objective/assassinate':
        return 'Asassinate {} the {}.'.format(objective.target_name, objective.target_role)
    else:
        return objective.objective_desc
