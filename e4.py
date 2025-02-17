import webbrowser

user_termin = input('Enter a search term: ').replace(' ', '+')
webbrowser.open("https://www.google.com/search?q=" + user_termin)

