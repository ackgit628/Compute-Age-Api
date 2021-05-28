
def computeAge(bday, today):
    age = 0
    if bday.year > today.year:
        return JsonResponse("greetings time traveller", safe=False)
    if (bday.month < today.month) or (bday.month == today.month and bday.day <= today.day):
        age = today.year - bday.year
    if (bday.month > today.month) or (bday.month == today.month and bday.day > today.day):
        age = today.year - bday.year - 1

    return age