from django.shortcuts import render, redirect
from Base_App.models import BookTable, AboutUs, Feedback, ItemList, Items

def HomeView(request):
    items = Items.objects.all()
    item_list = ItemList.objects.all()
    reviews = Feedback.objects.all()
    return render(request, 'home.html', {'items': items, 'list': item_list, 'review': reviews})

def AboutView(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html', {'data': data})

def MenuView(request):
    items = Items.objects.all()
    item_list = ItemList.objects.all()
    return render(request, 'menu.html', {'items': items, 'list': item_list})

def BookTableView(request):
    if request.method == 'POST':
        name = request.POST.get('user_name', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()
        email = request.POST.get('user_email', '').strip()
        total_person = request.POST.get('total_person', '').strip()
        booking_date = request.POST.get('booking_data', '').strip()

        print(f"Received data: {name}, {phone_number}, {email}, {total_person}, {booking_date}")

        if name and phone_number and email and total_person and booking_date:
            if len(phone_number) == 10 and total_person.isdigit():
                data = BookTable(
                    Name=name,
                    Phone_number=phone_number,
                    Email=email,
                    Total_person=int(total_person),
                    Booking_date=booking_date
                )
                data.save()
                print("Booking saved successfully!")
                return redirect('Book_Table')  # Перенаправляем на ту же страницу после успешного бронирования
            else:
                print("Invalid phone number or total persons count.")
        else:
            print("Some fields are missing.")

    return render(request, 'book_table.html')

def FeedbackView(request):
    return render(request, 'feedback.html')
