a = [1, 2.2, "3", "a"]

b = "foo"

c = 42

d = { "a":"b", "b":"c" }

e = True


| Uttrykk      | int | dict | None | (-error-) | list | str | bool | float |
|--------------|:---:|:----:|:----:|:---------:|:----:|:---:|:----:|:-----:|
| `f"{c}"`     |  o  |  o   |  o   |    o      |  o   |  o  |  o   |   o   |
| `e and not e`|  o  |  o   |  o   |    o      |  o   |  o  |  o   |   o   |
| `a[0]`       |  o  |  o   |  o   |    o      |  o   |  o  |  o   |   o   |
| `d["c"]`     |  o  |  o   |  o   |    o      |  o   |  o  |  o   |   o   |







a = [1, 2.2, "3", "a"]

b = "foo"

c = 42

d = { "a":"b", "b":"c" }

e = True


| Uttrykk      | int | dict | None | (-error-) | list | str | bool | float |
|--------------|:---:|:----:|:----:|:---------:|:----:|:---:|:----:|:-----:|
| `a in a`     |  o  |  o   |  o   |    o      |  o   |  o  |  o   |   o   |
| `a[0:1]`     |  o  |  o   |  o   |    o      |  o   |  o  |  o   |   o   |
| `b + "a[0]"` |  o  |  o   |  o   |    o      |  o   |  o  |  o   |   o   |


a = [1, 2.2, "3", "a"]

b = "foo"

c = 42

d = { "a":"b", "b":"c" }

e = True


| Uttrykk      | int | dict | None | (-error-) | list | str | bool | float |
|--------------|-----|------|------|-----------|------|-----|------|-------|
| `f"{c}"`     |     |      |      |           |      |  X  |      |       |
| `e and not e`|     |      |      |           |      |     |  X   |       |
| `a[0]`       |  X  |      |      |           |      |     |      |       |
| `d["c"]`     |     |      |      |     X     |      |     |      |       |



a = [1, 2.2, "3", "a"]

b = "foo"

c = 42

d = { "a":"b", "b":"c" }

e = True


| Uttrykk      | int | dict | None | (-error-) | list | str | bool | float |
|--------------|-----|------|------|-----------|------|-----|------|-------|
| `a in a`     |     |      |      |           |      |     |  X   |       |
| `a[0:1]`     |     |      |      |           |  X   |     |      |       |
| `b + "a[0]"` |     |      |      |           |      |  X  |      |       |