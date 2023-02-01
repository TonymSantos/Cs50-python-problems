#imprime sempre o mesmo 

def main():
    user_i = input("File name: ").lower()

    if ".gif" in user_i:
        f = "image/gif"
    elif ".jpg" in user_i or "jpeg" in user_i:
        f = "image/jpeg"
    elif ".png" in user_i:
        f = "image/png"
    elif ".pdf" in user_i:
        f = "application/pdf"
    elif ".txt" in user_i:
        f = "text/plain"
    elif ".zip" in user_i:
        f = "application/zip"
    else:
        f = "application/octet-stream"
        
    print(f)

while True:
    main()