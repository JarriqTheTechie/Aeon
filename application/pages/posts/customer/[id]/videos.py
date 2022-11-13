endpoint = "videos"
def default(id):
    # language=HTML prefix=<body> suffix=</body>
    string = f"""
        <b>Browsing videos for customer {id}</b>
    """
    return string
