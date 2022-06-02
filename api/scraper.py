from utils.utils import get_soup, get_status


class HDD:
    @staticmethod
    def get_top_50():
        url = "https://hitsdailydouble.com/sales_plus_streaming"
        status = get_status(url)
        r = get_soup(url)

        # find tbody
        table = r.find("table", {"class": "hits_album_chart"})
        # get tr tags from table
        tr1 = table.find_all("tr", {"class": "hits_album_chart_header_full_alt1"})
        tr2 = table.find_all("tr", {"class": "hits_album_chart_header_full_alt2"})

        # get hdd chart status
        hdd_status = r.find("div", {"class": "hits_album_chart_version"}).span.text.split(" ")[1].strip()

        # get hdd chart date
        chart_date = r.find("div", {"class": "hits_album_chart_date"}).span.text.split("MARKETSHARE")[0].strip()

        # combine table rows header alt 1 and header alt 2 (since HDD has different classes for each)
        tr_all = []
        tr_all.extend(tr1)
        tr_all.extend(tr2)

        # get table data from tr tags
        combined_data = []
        for i in tr_all:
            # get td tags from tr tags
            td = i.find_all("td")
            data1 = []
            for span in td:
                # get span tags from td tags
                span = span.find_all("span")
                for j in span:
                    # get text from span tags
                    data1.append(j.text)

            if td[1].text.strip() == "--":
                lw = "none"
            else:
                lw = td[1].text.strip()

            if td[5].text.strip() == "--":
                change = "none"
            else:
                change = td[5].text.strip()

            artist = data1[0].split("|")[0].strip()
            album = data1[0].split("|")[1].strip()
            record_label = data1[1].strip()
            total_sales = td[4].text.strip()
            tw = td[2].text.strip()

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

        # sort data based on TW value
        combined_data.sort(key=lambda x: int(x["TW"]), reverse=False)

        data = {"status": status, "list_status": hdd_status, "chart_date": chart_date, "data": combined_data}

        if status != 200:
            raise Exception("API response: {}".format(status))
        return data


if __name__ == '__main__':
    hdd = HDD()
    print(hdd.get_top_50())
