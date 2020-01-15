# from my_course_notes.Lesson_10_notes.models.workers import Person, Location
# print(sys.path)
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.workers import Person, Location
location_obj = Location(street="Kreschatik", city="Kyiv")
