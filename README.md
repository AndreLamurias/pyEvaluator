# PyEvaluator

A library that helps you evaluate the performance of annotator systems, for example.

Imagine that you are developing a system to automaticaly detect mentions of animals in text. For testing this system you compare the terms annotated by your system with the terms that should be annotated (gold standard). Assume that you are doing this for just one document and that your gold standard is:

```python
gold_standard = ['dolphin', 'parrot', 'spider', 'gorilla', 'cats']
```

And that your system annotated the following terms:

```python
test_annotations = ['parrot', 'banana', 'gorilla', 'basket']
```

Then you can test your system this way:

```python 
from pyEvaluator.Evaluator import Evaluator

# Arguments should be sets
ev = Evaluator(gold_terms=set(gold_standard), pred_terms=set(test_annotations))

print "Precision: {}".format(ev.precision())
print "Recall: {}".format(ev.recall())
print "F1-Score: {}".format(ev.f1_score())
print
print "True Positives: {}".format(ev.true_positives())
print "False Positives: {}".format(ev.false_positives())
print "False Negatives: {}".format(ev.false_negatives())
```

The output will be:

```
Precision: 0.5
Recall: 0.4
F1-Score: 0.444444444444

True Positives: set(['gorilla', 'parrot'])
False Positives: set(['basket', 'banana'])
False Negatives: set(['cats', 'dolphin', 'spider'])
```

## Installation
```shell
pip install git+https://github.com/LLCampos/pyEvaluator
```








