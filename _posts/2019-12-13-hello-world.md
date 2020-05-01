---
layout: post
title:  Template MarkDown Battlefield
author: Diego
description: My markdown and Jekyll battlefield.
---

Is it aliveeee?

# H1
## H2
### H3
#### H4
##### H5
###### H6




### Hello Latex

Note that this assumes the following delimiters appear in your HTML:

```html
$$\LaTeX code$$   (for display)
\\[\LaTeX code\\] (also for display)
\\(\LaTeX code\\) (for inline)
```


When \\( a \ne 0 \\), there are two solutions to \\( ax^2 + bx + c = 0\\).

$$\left(\sum_{i=1}^{n}{\left|a_i\right|}^p\right)^{1/p}$$


### Hello Python

    this = is
    is = 2
    a = code


```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

```python
s = "Python syntax highlighting"
print s
```


```
No language indicated, so no syntax highlighting.
But let's throw in a <b>tag</b>.
```

{% highlight python lineson %}
def total_factor_sum(no):
  sum= 0
  for i in range(1,no):
    if no%i==0:
      sum +=i
    else:
      pass
  return sum

for i in range(1,10000000):
  if i == total_factor_sum(total_factor_sum(i))  and i != total_factor_sum(i):
    print i, total_factor_sum(i)
{% endhighlight %}



```python
def total_factor_sum(no):
  sum= 0
  for i in range(1,no):
    if no%i==0:
      sum +=i
    else:
      pass
  return sum

for i in range(1,10000000):
  if i == total_factor_sum(total_factor_sum(i))  and i != total_factor_sum(i):
    print i, total_factor_sum(i)
```