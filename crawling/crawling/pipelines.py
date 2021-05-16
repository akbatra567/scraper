from myapi.models import Job


def clean_title(param):
    return str(param[0])


def clean_company(param):
    return str(param[0])


def clean_salary(param):
    return 21


def clean_location(param):
    return str(param[0])


def clean_url(param):
    return str(param[0])


class CrawlingPipeline:
    def process_item(self, item, spider):
        title = clean_title(item['title'])
        company = clean_company(item['company'])
        salary = clean_salary(item['salary'])
        location = clean_location(item['location'])
        url = clean_url(item['url'])

        Job.objects.create(
            title=title,
            company=company,
            salary=salary,
            location=location,
            url=url
        )
        return item
