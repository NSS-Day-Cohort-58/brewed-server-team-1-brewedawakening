EMPLOYEES = [
    {
        "id": 1,
        "name": "Bilbo Baggins",
        "email": "ameron0@mashable.com",
        "hourlyRate": 11.50

    },
    {
        "id": 2,
        "name": "Damara Pentecust",
        "email": "dpentecust1@apache.org",
        "hourlyRate": 10.75

    },
    {
        "id": 3,
        "name": "Anna Bowton",
        "email": "abowton2@wisc.edu",
        "hourlyRate": 12.30

    },
    {
        "id": 4,
        "name": "Hunfredo Drynan",
        "email": "hdrynan3@bizjournals.com",
        "hourlyRate": 12.00

    },
    {
        "id": 5,
        "name": "Elmira Bick",
        "email": "ebick4@biblegateway.com",
        "hourlyRate": 12.30

    },
    {
        "id": 6,
        "name": "Bernie Dreger",
        "email": "bdreger5@zimbio.com",
        "hourlyRate": 11.50

    },
    {
        "id": 7,
        "name": "Rolando Gault",
        "email": "rgault6@google.com",
        "hourlyRate": 11.80

    },
    {
        "id": 8,
        "name": "Tiffanie Tubby",
        "email": "ttubby7@intel.com",
        "hourlyRate": 21.00

    },
    {
        "id": 9,
        "name": "Tomlin Cutill",
        "email": "tcutill8@marketwatch.com",
        "hourlyRate": 12.10

    },
    {
        "id": 10,
        "name": "Arv Biddle",
        "email": "abiddle9@cafepress.com",
        "hourlyRate": 13.00

    }
]


def get_all_employees():
    return EMPLOYEES


def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the employeeS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
