from  models.workers import Person, Location

location_obj = Location(street="Kreschatik", city="Kyiv")

person_dict = {
    "first_name": "Bob",
    "surname": "Arum",# from my_course_notes.Lesson_10_notes.models.workers import Person, Location
    "age": 43,
    "experience": 20,
    "location": location_obj
}

Person(**person_dict).save()
