def raiseError(errorMessage):
    raise errorMessage

try:
    raiseError("AAAAAAAAAA ERROR!!1!1!11")
except:
    print("Nie ma problemu, obsługujemy error ;)")