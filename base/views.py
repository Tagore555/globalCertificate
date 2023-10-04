from .models import *
from django.shortcuts import render
from django.db.models import Q,F
#from .forms import DetailsForm

# Create your views here.
def home(request):
    """if request.method=='POST':
        if request.POST.get('rno') and request.POST.get('name') and request.POST.get('year') and request.POST.get('section') and request.POST.get('title') and request.POST.get('rno')!="" and request.POST.get('name')!="" and request.POST.get('year')!="" and request.POST.get('section')!="" and request.POST.get('title')!="":
            post=FullCollege()
            post.roll_number=request.POST.get('rno')
            post.student_name=request.POST.get('name')
            post.year=request.POST.get('year')
            post.section=request.POST.get('section')
            post.title=request.POST.get('title')
            post.save()
            return render(request,'base/home.html')
        else:
            return render(request,'base/home.html')
    else:
        return render(request,'base/home.html')"""
    

    if request.method == 'POST':
        rno = request.POST.get('rno')
        name = request.POST.get('name')
        year = request.POST.get('year')
        section = request.POST.get('section')
        title = request.POST.get('title')

        if rno and name and year and section and title and rno!="" and name!="" and year!="" and section!="" and title!="":
            r=True
            # Check if a record with the same values already exists
            obj, created = FullCollege.objects.get_or_create(
                roll_number=rno,
                student_name=name,
                year=year,
                section=section,
                title=title,
            )

            if created:
                # New record was created
                val="New record was created"
                return render(request, 'base/home.html',{"val":val,'r':r})
            else:
                # Record with the same values already existed
                val="Record with the same values already existed"
                return render(request, 'base/home.html',{"val":val,'r':r})
        else:
            # Some required fields were missing
            val="Some required fields were missing"
            return render(request, 'base/home.html',{"val":val,'r':r})
    else:
        r=False
        # Handle GET requests
        val="Handle GET requests"
        return render(request, 'base/home.html',{"val":val,'r':r})


def check(request):
    roll=request.POST.get('rno')
    na=request.POST.get('name')
    ye=request.POST.get('year')
    se=request.POST.get('section')
    tit=request.POST.get('title')
    form= FullCollege.objects.all()
    context = {'form': form, 'roll': roll, 'na': na, 'ye': ye, 'se': se, 'tit': tit}
    return render(request, 'base/check.html', context)
    #if roll!="" and se!="":
"""count = Details.objects.filter(rno__isnull=False).count()
        #count = Details.objects.filter(Q(roll_number="roll") and Q(section="na")).count()
        #count = Details.objects.filter(roll_number=F('section')).count()
        matching_records = Details.objects.filter(roll_number=F('section'))
        print(matching_records)

        # Count rows where 'roll_number' matches 'section'
        count = matching_records.count()
        print(count)
        context = {'form':form,'roll':roll,'na':na,'ye':ye,'se':se,'tit':tit,'count':count}
        return render(request,'base/check.html',context)
    else:
    
        context = {'form':form,'roll':roll,'na':na,'ye':ye,'se':se,'tit':tit}
        return render(request,'base/check.html',context)
"""
        #desired_value = roll  # Replace with the value of 'roll'
"""  desired_values = [roll, se]

        # Define a list of column names where you want to check for the value
        columns_to_check = ['roll_number', 'section']  # Replace with your column names

        # Create a dynamic Q object to construct the query
        query = Q()

        # Iterate through the list of columns and add conditions to the query for each desired value
        for column in columns_to_check:
            for value in desired_values:
                query != Q(**{f'{column}': value})

        # Count rows that meet the condition
        count = Details.objects.filter(query).count()

        context = {'form': form, 'roll': roll, 'na': na, 'ye': ye, 'se': se, 'tit': tit, 'count': count}
        return render(request, 'base/check.html', context)

    """







def edit(request, pk):
    student_id = Details.objects.get(roll_number=pk)
    print(student_id)
    form = DetailsForm(instance=student_id)
    
    if request.method == "POST":
        form = DetailsForm(request.POST, instance=student_id)
        if form.is_valid():
            form.save()
            return redirect('details')
    context = {'form':form}
    return render(request, 'base/edit.html', context)









































"""form = DetailsForm
    print(form)
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'base/home.html',context)
     rno=request.POST.get('rno')
    na=request.POST.get('name')
    ye=request.POST.get('year')
    se=request.POST.get('section')"""



"""if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            # Access cleaned_data after form validation
            rno = form.cleaned_data['rno']
            name = form.cleaned_data['name']
            year = form.cleaned_data['year']
            section = form.cleaned_data['section']
            
            # Create an instance of the model and save it
            post = Details(
                roll_number=rno,
                student_name=name,
                year=year,
                section=section
            )
            post.save()
            return render(request, 'base/home.html')
    else:
        # Handle GET request or other cases here
        form = DetailsForm()
    
    context = {'form': form}
    return render(request, 'base/home.html', context)"""
