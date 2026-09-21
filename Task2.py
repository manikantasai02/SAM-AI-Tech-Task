import re

def validate_url_format(url):
    """Check if the URL has a valid format."""
    regex = re.compile(
        r'^(?:http|https)://'  # must start with http:// or https://
        r'(?:\w+\.)+\w+'       # domain name
        r'(?:[/?#]\S*)?$'      # optional path/query
    )
    return re.match(regex, url) is not None

def check_https(url):
    """Check if the URL uses HTTPS."""
    return url.startswith("https://")

def url_safety_checker(url):
    """Main function to check URL safety."""
    if not validate_url_format(url):
        return f"❌ Invalid URL format: {url}"
    
    if check_https(url):
        return f"✅ Safe: {url} uses HTTPS"
    else:
        return f"⚠️ Suspicious: {url} does not use HTTPS"

# Example usage
if __name__ == "__main__":
    urls = [
        "https://github.com/springboardmentor181/Metro-Crowd-Management-Team-2/branches",
        "https://supabase.com/dashboard/org/vdujpmsrenodkigjxqsu",
        "ftp://example.com",
        "https://secure-site.org/login"
    ]
    for u in urls:
        print(url_safety_checker(u))
