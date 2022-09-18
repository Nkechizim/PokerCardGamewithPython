release_dates = {
    "Python": 1991,
    "Java": 1995,
    "Ruby": 1995,
    "Go": 2007
}

more_release_dates = {
    "Python": 1998,
    "C++": 1999
}

release_dates.update(more_release_dates)
print(release_dates)
print(more_release_dates)

print()

release_dates = {
    "Python": 1991,
    "Java": 1995,
    "Ruby": 1995,
    "Go": 2007
}

more_release_dates = {
    "Python": 1998,
    "C++": 1999
}
more_release_dates.update(release_dates)
print(release_dates)
print(more_release_dates)