from turtle import title
from .models import GeneralInformation, Carousel, Picture, Paragraph, Course, Staff


def data_processor(request):
    query = GeneralInformation.objects.all()[0]
    # carousel = Carousel.objects.all()
    # about1 = Picture.objects.get(title="about1")
    # choose1 = Picture.objects.get(title="choose1")
    # choose_p = Paragraph.objects.get(title="choose_p")
    # courses = Course.objects.all()
    # staffs = Staff.objects.all()
    return {
        'data' : query,
        # 'car1': carousel[0],
        # 'car2': carousel[1],
        # 'about1': about1,
        # 'choose1': choose1,
        # 'choose_p': choose_p,
        # 'courses': courses,
        # 'staffs': staffs,
    }