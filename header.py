def get_header(request: str):
    """Function to get the headers from an HTTP request"""
    lines = request.split("\n")
    header = None
    for line in lines:
        if line.startswith("User-Agent:"):
            header = line.split(":", 1)[1].strip()
            break
    return header