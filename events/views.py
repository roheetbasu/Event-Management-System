from django.shortcuts import render

halls = [
    {
       'hall_name' : 'Hall 1',
       'capacity' : 48
    },
    {
       'hall_name' : 'Hall 2',
       'capacity' : 100
    }
]
def home(request):
    context = { 'halls' : halls}
    return render(request, 'events/home.html', context)

def about(request):
    return render(request, 'events/about.html', {'title': 'About'})

