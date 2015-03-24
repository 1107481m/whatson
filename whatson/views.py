from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from whatson.forms import NewCalendarForm, NewEventForm, UserForm, EditEventForm, EditCalendarsForm
from whatson.models import PrivateCalendar, PrivateEvent, PublicEvent, PublicCalendar
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.template import RequestContext
from django.contrib.auth.models import User
from django.shortcuts import render_to_response

def index(request):
    #if request.user.is_authenticated:
        #return HttpResponseRedirect("/home/")
    response = render(request,'index.htm')
    return response


# New event form code must be included in home view for
# #add event date time application to function correctly
@login_required
def home(request):
    context_dict = {}

    calendars = PrivateCalendar.objects.filter(user=request.user)
    context_dict['calendars'] = calendars

    # New event form
    created = False
    if request.method == "POST":
        event_form = NewEventForm(request=request, data=request.POST, auto_id="event_id_%s")
        event_form.user = request.user
        if event_form.is_valid():
            # If successful save data
            event_form.instance.user = request.user
            event_form.save()
            created = True
        else:
            # If form ivalid print errors
            print event_form.errors
            created = "Error"

    else:
        event_form = NewEventForm(request=request, auto_id="event_id_%s")

    context_dict['event_form'] = event_form
    context_dict['created'] = created

    # Fetch public events
    publicEvents = PublicEvent.objects.all().order_by('?')[:3]
    context_dict['publicEvents'] = publicEvents
    return render(request, 'home.htm', context_dict)

@login_required
def calendar(request):
    return render(request, 'calendar.html')

@login_required
def edit_calendars(request):
    context_dict = {}

    calendar = PrivateCalendar.objects.get(user_id=request.user.id, id=request.GET['id'])
    context_dict['calendar'] = calendar

    if request.method == "POST":
        calendar.name = request.POST["name"]
        calendar.active = request.POST.get('active', False);
        calendar.save()
    return render(request, 'edit_calendars.html', context_dict)

@login_required
def get_events(request):
    context_dict = {}
    events = PrivateEvent.objects.filter(user_id=request.user.id)
    context_dict['events'] = events
    return render(request, 'get_events.html', context_dict)

@login_required
def export_ical(request):
    context_dict = {}
    events = PrivateEvent.objects.filter(user_id=request.user.id)
    context_dict['events'] = events
    return render(request, 'export_ical.html', context_dict)

@login_required
def export_googlecal(request):
    context_dict = {}
    events = PrivateEvent.objects.filter(user_id=request.user.id)
    context_dict['events'] = events
    return render(request, 'export_googlecal.html', context_dict)

def new_calendar(request):
    created = False
    # Check if the submit type is PoSt and if it is validate the form and save info
    if request.method == "POST":
        cal_form = NewCalendarForm(data=request.POST)
        cal_form.user = request.user
        if cal_form.is_valid():
            # If no errors then save the form
            cal_form.instance.user = request.user
            cal_form.save()
            created = True
        else:
            # Display errors
            print cal_form.errors
            created = "Error"

    else:
        cal_form = NewCalendarForm()

    return render(request, 'new_calendar.html', {'cal_form': cal_form, 'created': created})

@login_required
def new_event(request):
    created = False
    # If submit type is post and form data is valid then create new event else display errors
    if request.method == "POST":
        event_form = NewEventForm(request=request, data=request.POST, auto_id="event_id_%s")
        event_form.user = request.user
        if event_form.is_valid():
            event_form.instance.user = request.user
            event_form.save()
            created = True
        else:
            # Display errors
            print event_form.errors
            created = "Error"

    else:
        event_form = NewEventForm(request=request, auto_id="event_id_%s")

    return render(request, 'new_event.html', {'event_form': event_form, 'created': created})

@login_required
def edit_event(request):
    # Removes event with specified ID
    id = request.GET.get("id")
    PrivateEvent.objects.filter(id=id).delete()

    return render(request, 'edit_event.html')

def about(request):
    response = render(request, 'about.html')
    return response

def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request,
            'register.html',
            {'user_form': user_form, 'registered': registered} )

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponse("<b>You have been logged in! Transferring you...</b><script>window.location.replace(\"/home/\");</script>")
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')
