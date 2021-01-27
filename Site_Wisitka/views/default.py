from pyramid.view import view_config
from Site_Wisitka.registration.review_registrator import register_review
from ..registration.feedback_registrator import register_feedback


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def reviewer(request):
    review = None
    feedback = None

    if request.params.__contains__('review'):
        review = register_review(request)
    elif request.params.__contains__('feedback'):
        feedback = register_feedback()

    return {'project': 'Site_Wisitka',
            'review': review,
            'feedback': feedback}
