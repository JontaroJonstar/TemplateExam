from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')



class Member:
    def __init__(self, id, name, join_at, picture_path):
        self.id = id
        self.name = name
        self.join_at = join_at
        self.picture_path = picture_path

member_list = [
    Member(0, 'Taro', '1900/07/12', 'img/snake.png'),
    Member(1, 'Jiro', '1900/05/11', 'img/jiro.jpg'),
    Member(2, 'Hanako', '1900/08/24', 'img/hanako.jpg'),
    Member(3, 'Yoshiko', '1900/11/04', 'img/yoshiko.jpg'),
    ]


def members(request):
    return render(request, 'members.html', context = {
        'members' : member_list,
    })


def member(request, id):
    return render(request, 'member_detail.html', context = {
        'member' : member_list[id],
    })