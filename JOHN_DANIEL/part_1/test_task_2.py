from feet import feet_to_meter
from task_3_func import pounds_to_kilogram
from task_4 import gratuity_calculator


def test_feet_to_meter():
	assert feet_to_meter(10) == 3.05


def test_pounds_to_kilogram():
	assert pounds_to_kilogram(120) ==  54.480000000000004

def test_gratuity_calculator():
	assert gratuity_calculator(23, 10) == 25.3
