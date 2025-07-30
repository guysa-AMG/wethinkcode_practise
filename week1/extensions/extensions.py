def determiner(fileName):
    mimes = {"jpg":"image/jpeg","jpe":"image/jpeg","gif":"image/gif","png":"image/png","pdf":"application/pdf","txt":"text/plain","zip":"application/zip"}
    try:
        ext = fileName.lower().split(".")[-1][:3]
    
        if ext in mimes:
            return mimes[ext]
    except IndexError:
        pass
    
    return "application/octet-stream"

value=input("File name: ")
mime_type=determiner(value)
print(mime_type)