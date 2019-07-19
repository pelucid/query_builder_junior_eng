# Day-in interview prep

### Project - Example of an Elasticsearch QueryBuilder API

Thanks for coming in for the day at Growth Intelligence. For the majority of the day you'll be working in this repo, on a query building API.

### Setup - Installing Python, Virtualenv

First, clone this repository to your computer via the links on the right (please use "Clone with SSH", creating a fork of the repository is not necessary). You will need to have SSH keys setup for your github account for this to work - we can set this up if you're not sure how. Please also ensure you have Python 2.7 installed.

Next, ensure that you have virtualenv installed. You can find installation instructions for `virtualenv` [here](https://virtualenv.pypa.io/en/latest/installation.html), and more general help with `pip` and Python package management [here](https://docs.python.org/2.7/installing/index.html). 

### Setup - Installing Project Requirements

When you have virtualenv installed, create a new Python environment and activate it by running:
```
virtualenv interview_env
source interview_env/bin/activate
```
Next, install some requirements by running: `make deps`. This may take a minute or two. When you're able to install the packages, you're all done!

### Checking you're done

First, add the newly cloned repo's path to your current PYTHONPATH environment variable by running this command:
```bash
export PYTHONPATH=/path/to/this/repo:$PYTHONPATH
```
When you have the dependencies installed, try the following command:

```bash
make run
```

You can then visit this URL `localhost:3031/v1/company_query_builder?revenue=20150101-20160101`


You should see the following output:
```json
{
  "query": {
    "filtered": {
      "filter": {
        "and": [
          {
            "term": {
              "status": 1
            }
          },
          {
            "nested": {
              "filter": {
                "bool": {
                  "must": [
                    {
                      "range": {
                        "financial_filters.revenue": {
                          "gte": 20150101,
                          "lte": 20160101
                        }
                      }
                    }
                  ]
                }
              },
              "path": "financial_filters"
            }
          }
        ]
      }
    }
  },
  "from": 0,
  "size": 50
}
```
