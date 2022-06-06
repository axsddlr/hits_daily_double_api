import re

from utils.utils import get_soup, get_status


class HDD:
    @staticmethod
    def get_top_50():
        # This is getting the status of the HDD website and getting the soup of the HDD website.
        url = "https://hitsdailydouble.com/sales_plus_streaming"
        status = get_status(url)
        r = get_soup(url)

        # Finding the table with the class "hits_album_chart"
        table = r.find("table", {"class": "hits_album_chart"})

        # This is finding all the tr tags with the class "hits_album_chart_header_full_alt1" and
        # "hits_album_chart_header_full_alt2".
        tr = table.find_all("tr", {"class": re.compile("hits_album_chart_header_full_alt*")})

        # Getting the status of the HDD chart.
        hdd_status = r.find("div", {"class": "hits_album_chart_version"}).span.text.split(" ")[1].strip()

        # Getting the date of the HDD chart.
        chart_date = r.find("div", {"class": "hits_album_chart_date"}).span.text.split("MARKETSHARE")[0].strip()

        # Getting the data from the HDD website and putting it into a list.
        combined_data = []
        for i in tr:
            # Finding all the td tags from the tr tags.
            td = i.find_all("td")
            data1 = []
            for span in td:
                # Getting all the span tags from the td tags.
                span = span.find_all("span")
                for j in span:
                    # get text from span tags
                    data1.append(j.text)

            # This is checking if the value is "--" and if it is, it will set the value to "none".
            if td[1].text.strip() == "--":
                lw = "none"
            else:
                lw = td[1].text.strip()

            if td[5].text.strip() == "--":
                change = "none"
            else:
                change = td[5].text.strip()

            # Splitting the string at the "|" and getting the first value.
            artist = data1[0].split("|")[0].strip()
            # Splitting the string at the "|" and getting the second value.
            album = data1[0].split("|")[1].strip()
            # Getting the record label from the HDD website.
            record_label = data1[1].strip()
            # Getting the total sales from the HDD website.
            total_sales = td[4].text.strip()
            # Getting the current week value from the HDD website.
            tw = td[2].text.strip()

            # Appending the data to the list.
            combined_data.append(
                {
                    "LW": lw,
                    "TW": tw,
                    "Artist": artist,
                    "Album": album,
                    "record_label": record_label,
                    "total": total_sales,
                    "change": change,
                }
            )

        # Sorting the data based on the TW value.
        combined_data.sort(key=lambda x: int(x["TW"]), reverse=False)

        # Creating a dictionary with the keys "status", "list_status", "chart_date", and "data".
        data = {"status": status, "list_status": hdd_status, "chart_date": chart_date, "data": combined_data}

        # This is checking if the status code is not 200, it will raise an exception.
        if status != 200:
            raise Exception("API response: {}".format(status))
        return data

    @staticmethod
    def get_overall_streams():
        # This is getting the status of the HDD website and getting the soup of the HDD website.
        url = "https://hitsdailydouble.com/streaming_songs"
        status = get_status(url)
        r = get_soup(url)

        # Finding the table with the class "hits_album_chart"
        table = r.find("table", {"class": "hits_album_chart"})

        # Finding all the tr tags with the class "hits_album_chart_header_full_alt1" and
        # "hits_album_chart_header_full_alt2"
        tr = table.find_all("tr", {"class": re.compile("hits_album_chart_header_full_alt*")})

        # Getting the status of the HDD chart.
        hdd_status = r.find("div", {"class": "hits_album_chart_version"}).span.text.split(" ")[1].strip()

        # Getting the date of the HDD chart.
        chart_date = r.find("div", {"class": "hits_album_chart_date"}).span.text.split("MARKETSHARE")[0].strip()

        # Getting the data from the HDD website and putting it into a list.
        combined_data = []
        for i in tr:
            # Finding all the td tags from the tr tags.
            td = i.find_all("td")
            data1 = []
            for span in td:
                # Getting all the span tags from the td tags.
                span = span.find_all("span")
                for j in span:
                    # get text from span tags
                    data1.append(j.text)

            # This is checking if the value is "--" and if it is, it will set the value to "none".
            if td[0].text.strip() == "--":
                lw = "none"
            else:
                lw = td[0].text.strip()

            if td[5].text.strip() == "--":
                change = "none"
            else:
                change = td[5].text.strip()

            # Splitting the string at the "|" and getting the first value.
            artist = data1[0].split("|")[0].strip()
            # Splitting the string at the "|" and getting the second value.
            album = data1[0].split("|")[1].strip()
            # Getting the record label from the HDD website.
            record_label = data1[1].strip()
            # Getting the total sales from the HDD website.
            total_sales = td[4].text.strip()
            # Getting the current week value from the HDD website.
            tw = td[1].text.strip()

            # Appending the data to the list.
            combined_data.append(
                {
                    "LW": lw,
                    "TW": tw,
                    "Artist": artist,
                    "Album": album,
                    "record_label": record_label,
                    # "total": total_sales,
                    # "change": change,
                }
            )

        # Sorting the data based on the TW value.
        # combined_data.sort(key=lambda x: int(x["TW"]), reverse=False)

        # Creating a dictionary with the keys "status", "list_status", "chart_date", and "data".
        data = {"status": status, "list_status": hdd_status, "chart_date": chart_date, "data": combined_data}

        # This is checking if the status code is not 200, it will raise an exception.
        if status != 200:
            raise Exception("API response: {}".format(status))
        return data

    @staticmethod
    def get_new_album_releases():
        # This is getting the status of the HDD website and getting the soup of the HDD website.
        url = "https://hitsdailydouble.com/new_album_releases"
        status = get_status(url)
        r = get_soup(url)

        # Finding the table with the class "hits_album_chart"
        table = r.find("table", {"class": "hits_album_chart"})

        # Finding all the tr tags with the class "hits_album_chart_header_full_alt1" and
        # "hits_album_chart_header_full_alt2"
        tr = table.find_all("tr", {"class": re.compile("hits_album_chart_header_full_alt*")})

        # Getting the data from the HDD website and putting it into a list.
        combined_data = []
        for i in tr:
            # Finding all the td tags from the tr tags.
            td = i.find_all("td")
            data1 = []
            for span in td:
                # Getting all the span tags from the td tags.
                span = span.find_all("span")
                for j in span:
                    # get text from span tags
                    data1.append(j.text)

            # Splitting the string at the "|" and getting the first value.
            artist = data1[0].split("|")[0].strip()
            # Splitting the string at the "|" and getting the second value.
            album = data1[0].split("|")[1].strip()
            # Getting the record label from the HDD website.
            record_label = td[1].contents[2]
            # Getting the current week value from the HDD website.
            release_date = td[0].text.strip()

            # Appending the data to the list.
            combined_data.append(
                {
                    "artist": artist,
                    "album": album,
                    "release_date": release_date,
                    "record_label": record_label,
                }
            )

        # Creating a dictionary with the keys "status", "list_status", "chart_date", and "data".
        data = {"status": status, "data": combined_data}

        # This is checking if the status code is not 200, it will raise an exception.
        if status != 200:
            raise Exception("API response: {}".format(status))
        return data


if __name__ == '__main__':
    hdd = HDD()
    # Printing the data from the HDD website.
    print(hdd.get_new_album_releases())
