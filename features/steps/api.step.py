from behave import step
import requests
import json

#"" \
#"POST"
# origin https://learning.elucidat.com
# referer https://learning.elucidat.com/
# user-agent Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
#""
"""
    [
            {
                "actor":{},
                "context":{
                    "contextActivities":{
                        "parent":[{"id":"https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a"}],
                        "category":[{
                            "id":"https://elucidat.com",
                            "definition":{
                                "name":{"en-US":"Elucidat.com"},
                                "description":{"en-US":"Course lovingly crafted with the Elucidat.com rapid authoring tool"}
                            }
                        }]
                    },
                    "registration":"9eaae7b0-1081-11ef-82d0-024fe978e585"
                },
                "object":{
                    "objectType":"Activity",
                    "definition":{"type":"http://adlnet.gov/expapi/activities/course","name":{"en-US":"Finding the Truth"}},
                    "id":"https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a"
                },
                "verb":{
                    "id":"http://adlnet.gov/expapi/verbs/attempted",
                    "display":{"en-US":"attempted"}
                },
                "result":{
                    "extensions":{"https://xapi.elucidat.com/progress":0},
                    "completion":false,
                    "duration":"PT0S"
                },
                "timestamp":"2024-05-12T17:04:02.459Z"
            },
            {
                "actor":{},
                "context":{
                    "contextActivities":{
                        "parent":[{"id":"https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a"}],
                        "category":[{
                            "id":"https://elucidat.com",
                            "definition":{
                                "name":{"en-US":"Elucidat.com"},
                                "description":{"en-US":"Course lovingly crafted with the Elucidat.com rapid authoring tool"}
                            }
                        }
                        ]
                    },
                    "registration":"9eaae7b0-1081-11ef-82d0-024fe978e585"
                },
                "object":{
                    "objectType":"Activity",
                    "definition":{
                        "type":"http://activitystrea.ms/schema/1.0/page",
                        "name":{"en-US":"INTRODUCTION"}
                    },
                    "id":"https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a/5c9126fe3b767"
                },
                "verb":{
                    "id":"http://adlnet.gov/expapi/verbs/experienced",
                    "display":{"en-US":"experienced"}
                },
                "result":{
                    "extensions":{
                        "https://app.elucidat.com/xapi/progress":2.857142857142857
                    },
                    "completion":false
                },
                "timestamp":"2024-05-12T17:04:05.876Z"
            }
        ]}
)
"""
@Step('Send an API request to force completion to 100%')
def make_api_request(context):
    base_url = "https://api.elucidat.com/v4/usage/store?bms=1"
    res = requests.post(
        base_url,
        data=json.dump(data),
        headers=json.load({
            "Authorization": "Basic NTc0MTk3OTg5NGFkMDpXV3hHTWpOd1ZXZG1NWFpZU0daelowTjZlazVRTTJsaFdEZEZiRnBrWVhWU2EzQkdjbTFOVFZScGFsWlpXRGRJYkZrMFMyUk5kVlJEYjI5RVVHNURhbGxNVVdWNmVEZE9jeXRIWTFZd1JXNHlkRTkyS3pReU9YSjBhamhZTTJKQlkwSlFjSEl5ZGxZeWQxazk="
        }),
    )