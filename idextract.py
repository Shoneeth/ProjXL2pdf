import re

def extract_file_id(url):
  """
  Extracts the file ID from a Google Drive link using regular expressions.

  Args:
      url: The Google Drive link as a string.

  Returns:
      The extracted file ID or None if not found.
  """
  # Look for "/file/d/" or "/open?id=" followed by alphanumeric characters
  match = re.search(r"(?:/file/d/|open\?id=)([\w_-]+)", url)
  if match:
    return match.group(1)  # Return the captured group (the file ID)
  else:
    return None

