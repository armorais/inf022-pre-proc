schema = {
            "properties": { "kek" : { "properties": { "jej" : { "properties": {
                "lul": {
                    "mergeStrategy": "append"
                }
             }}}}, "bar" :{ "mergeStrategy": "append" }

            }
        }

from jsonmerge import Merger

base = {
        "foo": 1,
        "bar": [ "one" ],
        "kek" : { "jej" : [{ "lul": '1' }]  }
        }

head = {
         "bar": [ "two" ],
         "kek" : { "jej" : [{ "lul": '2' }]  },
         "baz": "Hello, world!"
    }

base["kek"]["jej"]["lul"] = []
head["kek"]["jej"]["lul"] = []
head["kek"]["jej"]["lul"].append(1)
base["kek"]["jej"]["lul"].append(2)

merger = Merger(schema)
result = merger.merge(base, head)
print(result)