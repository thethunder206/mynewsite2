from django.shortcuts import render
from email.message import EmailMessage
import ssl
import smtplib
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, "survey/base.html", {})

def re(request):
    return redirect('cdc.gov/mentalhealth/learn/index.htm')

def depression_survey_uwc(request):
    global final_amt, lst
    lst = []
    final_amt = 0
    lst.append(request.POST.get('name'))
    lst.append(request.POST.get('name1'))
    lst.append(request.POST.get('name2'))
    lst.append(request.POST.get('name3'))
    lst.append(request.POST.get('name4'))
    lst.append(request.POST.get('name5'))
    lst.append(request.POST.get('name6'))
    lst.append(request.POST.get('name7'))
    for i in lst:
        if type(i) == int or type(i) == str:
            final_amt += int(i)
    print(lst)
    print(final_amt)
    return render(request, "survey/depression(uwc).html", {})

def confirm(request):
    global body
    email_sender = "aaravsharma23@gmail.com"
    email_password = "drpf cqqm ypjq cmiq"
    email_receiver = "sharm50996@gapps.uwcsea.edu.sg"
    first = request.POST.get('first_name')
    grade = request.POST.get('grade')
    # subject = f"Depression Health Issue Customer - {first}"
    subject = f"Depression Health Issue Customer"

    # if final_amt == 8:
    #     body = f"""
    # Dear UWCSEA School Counsellors,
    # Student {first} from {grade} is suffering from a mental illness.
    # This student has shown minimal signs of depression, receiving a score of 8/32.
    #
    # Regards,
    # Mental Illness Website
    #             """
    # elif final_amt <= 18 and final_amt > 8:
    #     body = f"""
    # Dear UWCSEA School Counsellors,
    # Student {first} from {grade} is suffering from a mental illness.
    # This student has shown mild signs of depression, receiving a score of {final_amt}/32.
    #
    # Regards,
    # Mental Illness Website
    #             """
    # elif final_amt <= 25 and final_amt > 18:
    #     body = f"""
    # Dear UWCSEA School Counsellors,
    # Student {first} from {grade} is suffering from a mental illness.
    # This student has shown moderate signs of depression, receiving a score of {final_amt}/32.
    #
    # Regards,
    # Mental Illness Website
    #             """
    # elif final_amt > 26:
    #     body = f"""
    # Dear UWCSEA School Counsellors,
    # Student {first} from {grade} is suffering from a mental illness.
    # This student has shown severe signs of depression, receiving a score of {final_amt}/32.
    #
    # Regards,
    # Mental Illness Website
    #             """

    if final_amt == 8:
        body = f"""
Dear UWCSEA School Counsellors, 
A student is suffering from a mental illness.
This student has shown minimal signs of depression, receiving a score of 8/32.

Regards,
Mental Illness Website
            """
    elif final_amt <= 18 and final_amt > 8:
        body = f"""
Dear UWCSEA School Counsellors, 
A student is suffering from a mental illness.
This student has shown mild signs of depression, receiving a score of {final_amt}/32.
Please reach out to this student soon.

Regards,
Mental Illness Website
            """
    elif final_amt <= 25 and final_amt > 18:
        body = f"""
Dear UWCSEA School Counsellors, 
A student is suffering from a mental illness.
This student has shown moderate signs of depression, receiving a score of {final_amt}/32.
Please reach out to this student soon.

Regards,
Mental Illness Website
            """
    elif final_amt > 26:
        body = f"""
Dear UWCSEA School Counsellors, 
A student is suffering from a mental illness.
This student has shown severe signs of depression, receiving a score of {final_amt}/32.
Please reach out to this student ASAP.

Regards,
Mental Illness Website
            """

    em = EmailMessage()
    em['From '] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject

    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    print(request.POST.get(first))
    return render(request, "survey/yes.html", {})

def setup(request):
    return render(request, "survey/setup.html", {})

def thank(request):
    return render(request, "survey/thank.html", {})

def depression_survey_ww(request):
    global final_amt, lst
    lst = []
    final_amt = 0
    lst.append(request.POST.get('name'))
    lst.append(request.POST.get('name1'))
    lst.append(request.POST.get('name2'))
    lst.append(request.POST.get('name3'))
    lst.append(request.POST.get('name4'))
    lst.append(request.POST.get('name5'))
    lst.append(request.POST.get('name6'))
    lst.append(request.POST.get('name7'))
    for i in lst:
        if type(i) == int or type(i) == str:
            final_amt += int(i)
    print(lst)
    print(final_amt)
    return render(request, "survey/depression(ww).html", {})

def depression_questions(request):
    return render(request, "survey/depression-question.html", {})

def yes(request):
    return render(request, "survey/yes.html", {})

def no(request):
    return render(request, "survey/no.html", {})

def ww_no(request):
    return render(request, "survey/no.html", {})

def output_uwc(request):
    global data, add, final_amt
    for i in lst:
        if i == '0':
            data = "There has been some error while processing your data. If you have left some questions empty, please fill them in and try again!"
            add = ""
            check = "Would you like to share your results with the school counsellors?"
    if final_amt == 8 or final_amt == 9:
        data = "You appear to have minimal symptoms of depression."
        add = "Your results indicate that you have none, or very few signs of depression. These results are not meant to be a diagnosis. You can meet with a doctor or therapist to get a diagnosis and/or access therapy or medications. Sharing these results with someone you trust can be a great place to start"
        check = ""
    elif final_amt <= 18 and final_amt > 8:
        data = "You may be experiencing mild symptoms of depression. Consider seeking support."
        add = "Your responses indicate that you may be at risk of harming yourself. If you need immediate help, you can reach the Suicide & Crisis Lifeline by calling or texting 988 or using the chat box at 988lifeline.org. You can also text “MHA” to 741-741 to reach the Crisis Text Line. Warmlines are an excellent place for non-crisis support."
        check = "Would you like to share your results with the school counsellors?"
    elif final_amt <= 25 and final_amt > 18:
        data = "Your depression symptoms are moderate. It's advisable to consult a healthcare professional."
        add = "Your responses indicate that you may be at risk of harming yourself. If you need immediate help, you can reach the Suicide & Crisis Lifeline by calling or texting 988 or using the chat box at 988lifeline.org. You can also text “MHA” to 741-741 to reach the Crisis Text Line. Warmlines are an excellent place for non-crisis support."
        check = "Would you like to share your results with the school counsellors?"
    elif final_amt > 25:
        data = "Your depression symptoms are severe. Please seek immediate help."
        add = "Your responses indicate that you may be at risk of harming yourself. If you need immediate help, you can reach the Suicide & Crisis Lifeline by calling or texting 988 or using the chat box at 988lifeline.org. You can also text “MHA” to 741-741 to reach the Crisis Text Line. Warmlines are an excellent place for non-crisis support."
        check = "Would you like to share your results with the school counsellors?"
    print(final_amt)
    print(data)
    data = data
    return render(request, 'survey/depression(uwc).html', {'data': data, 'add': add, 'final_amt': final_amt, 'check': check})

def output_ww(request):
    global data, add, final_amt
    for i in lst:
        if i == '0':
            data = "There has been some error while processing your data. If you have left some questions empty, please fill them in and try again!"
            add = ""
            check = ""
    if final_amt == 8:
        data = "You appear to have minimal symptoms of depression."
        add = "Your results indicate that you have none, or very few signs of depression. These results are not meant to be a diagnosis. You can meet with a doctor or therapist to get a diagnosis and/or access therapy or medications. Sharing these results with someone you trust can be a great place to start"
        check = ""
    elif final_amt <= 18 and final_amt > 8:
        data = "You may be experiencing mild symptoms of depression. Consider seeking support."
        add = "Your responses indicate that you may be at risk of harming yourself. If you need immediate help, you can reach the Suicide & Crisis Lifeline by calling or texting 988 or using the chat box at 988lifeline.org. You can also text “MHA” to 741-741 to reach the Crisis Text Line. Warmlines are an excellent place for non-crisis support."
        check = "From your results, would you like to share your information with the school counsellors?"
    elif final_amt <= 25 and final_amt > 18:
        data = "Your depression symptoms are moderate. It's advisable to consult a healthcare professional."
        add = "Your responses indicate that you may be at risk of harming yourself. If you need immediate help, you can reach the Suicide & Crisis Lifeline by calling or texting 988 or using the chat box at 988lifeline.org. You can also text “MHA” to 741-741 to reach the Crisis Text Line. Warmlines are an excellent place for non-crisis support."
        check = "From your results, would you like to share your information with the school counsellors?"
    elif final_amt > 26:
        data = "Your depression symptoms are severe. Please seek immediate help."
        add = "Your responses indicate that you may be at risk of harming yourself. If you need immediate help, you can reach the Suicide & Crisis Lifeline by calling or texting 988 or using the chat box at 988lifeline.org. You can also text “MHA” to 741-741 to reach the Crisis Text Line. Warmlines are an excellent place for non-crisis support."
        check = "From your results, would you like to share your information with the school counsellors?"
    print(data)
    data = data
    return render(request, 'survey/depression(ww).html', {'data': data, 'add': add, 'final_amt': final_amt, 'check': check})
