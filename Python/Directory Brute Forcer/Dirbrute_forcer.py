import requests

status_codes = [200, 204, 301, 302, 307, 401, 403]

def addtofile(site_link, copy_results_to_filepath):
    with open(copy_results_to_filepath, "a") as file:
        file.write(f"{site_link}\n")

def brute_force(site_link, words_list_path, copy_results_to_filepath):

    with open(words_list_path, "r") as wordslist:
        try:
            for word in wordslist:
                formatted_link = f"{site_link}/{word.strip().lower()}"
                print(f"Trying: {formatted_link}")

                response_object = requests.get(formatted_link)

                if response_object.status_code in status_codes:
                    print(f"Found: {formatted_link}")
                    addtofile(formatted_link, copy_results_to_filepath)
                else:
                    print(f"Not found: {formatted_link}")

        except Exception as error:
            print(f"Error occurred: {error}")


# < ------------ NOTES ------------ >
# Website used to test the program: http://testphp.vulnweb.com

# Status Codes Guide
# 1XX -> informational
# 2XX -> success
# 3XX -> redirection
# 4XX -> client error
# 5XX -> server error

# printing the response object will show: <Response [status_code_here]>
# .status_code can be used to get the status code
# .get("<link>") tries to access the given link

# elements from a file will return "\n" with them, therefore makesure to .strip()